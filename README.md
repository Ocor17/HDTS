# HDTS
web-based hard drive tracker system
### To run the application


    Install the application libraries
    -1. pip install -r requirements.txt
    -2. cd HDTS-Django/
    -3. python manage.py runserver
    
## Infomation 
### Folders within HDTS-Django
- Inventory: Contains files needed to add and edit hard drives in the system.
- Accounts: Contains files needed for authentication and to save information about the user.
- Logs: Contains the log
- Media: Contains images to be displayed by the system.
- Register: Contains files used to register new users to the system.
- Request: Contains files used to allow requests to be created and edited in the database.
- Static: Contains CSS and JS files for the user view.

### Web Pages
- Maintainers webpages folder: Inventory/templates/Inventory  
- Requestor webpages folder: request/templates/request 

### Objects
- Hard Drive Model: Inventory/model.py  
- Request Model: request/model.py

### NOTICE
- User needs a Mongo database running to operate
- User needs to define Mongo settings under Databases
    - Engine: djongo
    
