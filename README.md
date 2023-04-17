# Movies Website for COSC 381
## Steps for starting the website (development mode)

1. Create a virtual environment in the root directory: `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Initialize the database: `flask --app movieswebsite init-db` After the database is initialized, the database file is at: `instance/movieswebsite.sqlite`
5. Start the website: `flask --app movieswebsite run --debug`
6. The webpage can be checked at: http://127.0.0.1:5000/movies/
7. To stop the app, hit: `ctrl + c`
8. If the virtual environment is no longer needed, it can be deactivated by `dactivate`
