# Kalendarz adwentowy (nazwa robocza albo nie)

## How to install
1. Download repo, 
2. Initialize virtual environment in it: `python -m venv env`,
3. Run that venv: `source env/bin/activate`(MAC),/ 
    WINDOWS google say `\env\Scripts\activate.bat` if it doesnt work do it `cd env` `cd Scripts` `activate`
4. Install dependencies: `pip install -r requirements.txt`,
5. (optional) Change database settings in settings.py if you want to use different (non-sqlite) db backend, 
6. Migrate database: `python manage.py migrate`,
7. To run dev server: `python manage.py runserver`

### with Docker
1. Download repo
2. Run docker-compose up in it
3. Ready. Thing is accessible at localhost:8000. Stopping and starting containers again results in making whole new migrations and reseting database (sqlite) content. 

## Tips for devs

### Dumping pip installations into the file
If you installed new pip dependency you need to allow others to know about it. To do so it is best to save all requirements
in one file, which in this case in named `requirements.txt`. You can do this by typing following command: 

`pip freeze > requirements.txt`
