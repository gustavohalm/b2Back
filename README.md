# b2Back

### Ubuntu
 *(if you had python 2 in your's python command replace with python3 and pip for pip3)*
  #### Checking Python version
  ``` 
    python --version #should be 3.x
  ``` 
  #### Clone the Repsitory
  ``` 
  git clone https://github.com/gustavohalm/b2Back.git 
  ```
  
  #### Installing Dependencies and Migrate the Application's
  ```
  pip install -r requirements.txt
  python manage.py makemigrations && python manage.py migrate
  ```
  #### Running the Application's test's 
  ```
  python manage.py test
  ```  
  #### Running the Application's 
  ```
  python manage.py runserver
  ```
  
