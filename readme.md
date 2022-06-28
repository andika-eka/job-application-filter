<h1 align="center">
    Job Application filter
</h1>


 **Requirement**:
1. python:  
    web:  
    * django : https://www.djangoproject.com/  
      ```pip install Django==4.0.5```

    * mysql client : https://pypi.org/project/mysqlclient/   
        ```pip install mysqlclient```

    * django widget_tweaks :https://pypi.org/project/django-widget-tweaks/
        ```pip install django-widget-tweaks```
    
    solr:  
    * pysolr : https://pypi.org/project/pysolr/  
    ``` pip install pysolr```

    
    PDF:
    * FPDF : https://pypi.org/project/fpdf2/  
    ``` pip install fpdf2```

    * PyPDF2  :https://pypi.org/project/PyPDF2/  
    ```pip install PyPDF2```

2. mysql

3. apache solr
***
<br/>   

**How to clone:**  
1. Prepare the above requrements
2. Clone this repository
3. activate mysql and create new database
   ```sql
   mysql -u root

   CREATE DATABASE databasename
   ```
1. put database in *cvFilter/settings.py*
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
2. create secret key from https://djecrety.ir/ and put in in cvFilter/settings.py
    ``` python 
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-fgqs6&nz7wfk1vk=*qd$n@-zk#wgtyw(ur^4-1v=wmi2i@w#_d'
    ```

1. Make your migrations
    ``` 
    python manage.py makemigrations
    python manage.py migrate
    ```
2. Create a new superuser
    ``` 
    python manage.py createsuperuser
    ```
1. let the show begin
    ``` 
    python manage.py runserver
    ```

    ***

<br/>  

**How to generate fake data (for testing):**  
1. Delete all applicants data.  
    go  to  project root directory and run the following command 
    ```
    python manage.py migrate applicant zero
    python manage.py migrate applicant 
    ```
2. Delete all pdf file in ./media/documents/
3. go to applicant/fixture/ run the following command  
    ``` 
    python data_generator.py numberOfInstances
    ```
4. go  to  project root directory and run the following command 
    ```
    python manage.py loaddata applicant/fixture/applicants.json
    ```
5. Examine
 