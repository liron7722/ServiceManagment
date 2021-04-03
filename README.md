# ServiceManagment‏
Made by Liron Revah - used python3  
Made to sync service registration on the main db

#### Environment Variables to create
- NAME <Service Name>
- TYPE <Service type>
- ENV <Environment type>
- PORT <Service Port>
- DB_URI <General db uri>


#### if you want virtual environment run:
###### In Windows
- python -m venv venv
- venv\Scripts\activate
###### In Linux
- python3 -m venv venv
- source venv\Scripts\activate

#### Install the requirements packages
- pip install -r requirements.txt (In Windows)
- pip3 install -r requirements.txt (In Linux)

#### Run the script:
- python main.py (In Windows)
- python3 main.py (In Linux)
- pm2 start main.py --name service_manager --interpreter python3  (With PM2 manager)