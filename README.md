# GitAPI
Django Wrapper for Git Search(User) API


## Installation
- Clone the repo
- Create virtual environment for python3 and activate it.
- Install packages listed in requirements.txt. Also ensure mysql-dev(el) is installed.
- Create a MySQL database and user specified in the GitApi/settings.py file (Or change database config accordingly).
- Create a file named `.env` in root project directory and store values for SECRET_KEY(Django secret key) and  user_auth & token_auth(GitHub username and GitHub Personal access token)
- Make migrations 
- Run server

## Usage
- Use `localhost:8000/search` to search users on GitHub and add them to the database.
- To access adminpanel use `http://127.0.0.1:8000/users/`.




