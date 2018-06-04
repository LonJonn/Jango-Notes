#Jango Notes
Notes made in Django
>by Justin and Leon

###Cloning Repo
`git clone git@github.com:LonJonn/Jango-Notes.git`

###Setup Dev

1. Open terminal `control + ~`

2. Set Python Env `source jangoEnv/bin/activate` 

3. change directory `cd jangoMain`

4. start server `python manage.py runserver`

5. Open `http://localhost:8000` in browser

###Making changes to DB and Models
If you make a change to a model
>for e.g. added a new model to *app*

1. `python manage.py makemigrations *app*`

2. `python manage.py migrate`