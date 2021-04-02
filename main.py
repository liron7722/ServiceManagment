import schedule
from os import environ
from time import sleep
from requests import get
from pymongo import MongoClient
from pymongo.mongo_client import database
from pymongo.errors import ServerSelectionTimeoutError, DuplicateKeyError


ENV = environ.get('ENV') or 'Development'
NAME = environ.get('NAME') or 'Unlisted'
TYPE = environ.get('TYPE') or 'Unlisted'
IP = get('https://api.ipify.org').text
PORT = environ.get('PORT') or 'Unlisted'
DB_URI = environ.get('DB_URI') or 'Unlisted'


class ServiceManagement:
    client: MongoClient = None

    def __init__(self):
        self.establish_db_connection()

    def establish_db_connection(self) -> None:
        try:
            self.client = MongoClient(DB_URI)  # establish connection
            print('db establish connection')
        except ServerSelectionTimeoutError:
            message = 'db connection Timeout:\n' \
                      'For Cloud - check for if this machine ip is on whitelist\n' \
                      'For Local - check if the machine is running or if ports are blocked'
            print(message)

    @staticmethod
    def is_document_exist(collection: database.Collection, fil: dict) -> bool:
        cursor = collection.find(fil)
        try:
            cursor.next()
            flag = True
        except StopIteration:
            flag = False
        print(f'Document {"Not " * (not flag)}exist')
        return flag

    def post_service(self) -> None:
        if self.client is None:
            return None
        info = {
            'name': NAME,
            'type': TYPE,
            'env': ENV,
            'ip': IP,
            'port': PORT
        }
        fil = {'name': NAME, 'type': TYPE}
        db = self.client.get_database(name='service')
        collection = db.get_collection(name=TYPE)
        self.push_to_db(collection=collection, info=info, fil=fil)

    def push_to_db(self, collection: database.Collection, info: dict, fil: dict = None) -> None:
        if fil is not None and self.is_document_exist(collection=collection, fil=fil):
            try:
                collection.update_one(filter=fil, update={"$set": info})
                print('updated document in the collection')
            except DuplicateKeyError:
                print('document is already in the collection')
        else:
            collection.insert_one(document=info)
            print('insert document to collection')


def run() -> None:
    service_manager = ServiceManagement()
    job = service_manager.post_service
    schedule.every(60).seconds.do(job)
    while True:
        schedule.run_pending()
        sleep(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
