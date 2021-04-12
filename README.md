# ServiceManagment‏
Made by Liron Revah - used python3  
Made to sync service registration on the main db

#### Environment Variables to create
- NAME - Service Name
- TYPE - Service type
- ENV - Environment type
- PORT - Service Port
- DB_URI - General db uri


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

#### Run the script with process manager:
- pm2 start main.py --name service_manager --interpreter python3  (With PM2 manager)

(With Supervisor)
- sudo apt install supervisor
- sudo touch /var/log/service/script.err.log
- sudo touch /var/log/service/script.out.log
- sudo nano /etc/supervisor/conf.d/script.conf  
	[program:ServiceManager]  
	directory=/home/ubuntu/ServiceManagment/  
	command=python3 main.py  
	user=ubuntu  
	autostart=true  
	autorestart=true  
	stopasgroup=true  
	killasgroup=true  
	stderr_logfile=/var/log/service/script.err.log  
	stdout_logfile=/var/log/service/script.out.log  
- sudo supervisorctl reload