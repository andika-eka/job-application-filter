# Job Application filter

**requrement:**  
1. python:  
    web:  
    * django : https://www.djangoproject.com/  
      ```pip install Django==4.0.5```

    * mysql client : https://pypi.org/project/mysqlclient/   
        ```pip install mysqlclient```
    
    solr:  
    * pysolr : https://pypi.org/project/pysolr/  
    ``` pip install pysolr```

    * django-haystack  : https://pypi.org/project/django-haystack/  
    ``` pip install django-haystack```
    
    PDF:
    * FPDF : https://pypi.org/project/fpdf2/  
    ``` pip install fpdf2```

    * PyPDF2  :https://pypi.org/project/PyPDF2/  
    ```pip install PyPDF2```

2. mysql

3. apache solr

**How to clone:**
1. Prepare the above requrements
2. Clone this repository
3. activate mysql and create new database
   ```sql
   mysql -u root

   CREATE DATABASE databasename
   ```
4. put database in *cvFilter/settings.py*
   ```python
   DATABASES = {
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'cvFilter',  
        'USER':'root',  
        # 'PASSWORD':'mysql',  
        'HOST':'localhost',  
        'PORT':'3306'  
        }
    }
    ```
5. create secret key from https://djecrety.ir/ and put in in cvFilter/settings.py
    ``` python 
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-fgqs6&nz7wfk1vk=*qd$n@-zk#wgtyw(ur^4-1v=wmi2i@w#_d'
    ```

6. Make your migrations
    ``` 
    python manage.py makemigrations
    python manage.py migrate
    ```
7. Create a new superuser
    ``` 
    python manage.py createsuperuser
    ```
8. let the show begin
    ``` 
    python manage.py runserver
    ```