Pitch Application
#### Author
Vincent Kipkirui 

## Description
This is an application that allows user to use one minute to make a pitch and allow other users to vote ad give feedback on the pitch created.
As a user of the web application you will be able to:
1. user authentication user registration and login.
2. User creating a pitch
3. Ability to comment to the created pitch


## Setup and installations
1. Clone Project to your machine
2. Activate a virtual environment on terminal: `source venv/bin/activate`
3. Install all the requirements found in requirements file.
4. On your terminal run `python3.8 manage.py server`

  
## Specifications
1. user Authentication
2.  crating a pitch  
### Prerequisites
* python3.8
* virtual environment
* pip
#### Clone the Repo and rename it to your suitable name of your choice.
bash
git clone https://github.com/jepkess/Pitch-App.git

#### Initialize git and add the remote repository
bash
git init

bash
git remote add origin https://github.com/jepkess/Pitch-App.git

#### Create  the virtual environment
bash
python3.8-venv venv
## Activating the environment.
bash
source venv/bin/activate

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
#### Make and run migrations
bash
python3.8 manage.py check
python manage.py makemigrations 
python3.8 manage.py sqlmigrate 
python3.8 manage.py migrate

#### Run the app
bash
python3.8 manage.py runserver

Open [localhost:5000](http://127.0.0.1:5000)
## Testing the Application
`python3.8 manager.py test`
## Technologies used
1.  python 3.8 version
2. Flask
3.  Boostrap
4.  HTML
5. CSS

## live link
[view](https://pitchapplication.herokuapp.com)

### Licence
This project is under the  [MIT](LICENSE.md) licence