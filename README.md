# flask-structure
FLASK is a micro framework. But you can do bg projects on FLASK. The flexibility is awesome. But there are no defined structure. I had hard time figuring one out. So, after hundreds of articles I have come up with this structure. This structure was followed for an AI based NLU API microservice project. I am uploading the basic structure to start up any FLASK project.   You can call it, the basic skeleton of a FLASK project for maintainable big applications.


# Getting up and running with the application

1. git clone https://github.com/anuragbhattacharjee/flask-structure.git
2. python3 -m venv {your-app-name}-venv
3. source {your-app-name}-venv/bin/activate
4. pip install -r requirements.txt
5. flask run

# To update requirements.txt: 
    pip freeze > requirements.txt
    More info: https://pip.pypa.io/en/stable/reference/pip_freeze/


# If environment varibales aren't set in your machine you can do any of the following:
  1. Set Env varibales:
      For Mac/Linux:
        export FLASK_ENV=development
        export FLASK_DEBUG=1
      For windows:
        set FLASK_ENV=development
        set FLASK_DEBUG=1 
  2. By using python-dotenv ( recommended )
          i. pip install python-dotenv
         ii. create a .flaskenv file in your project
        iii. in .flaskenv:
                FLASK_ENV=development
                FLASK_DEBUG=1
  Check if environement variables are set properly:
      For Linux:
        printenv FLASK_ENV
        printenv FLASK_DEBUG
 

# .gitignore
I have added all the to .gitignore so that the repository don't get bloated. It's a standard practice. Please add all these to your .gitignore:

{your-app-name}-venv

__pycache__

.flaskenv

*.log

*.pot

*.pyc

*/*/*/__pycache__/

*/*/__pycache__/

*/__pycache__/

