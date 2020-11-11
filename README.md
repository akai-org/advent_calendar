# Backend to advent calendar

## How to install
1. Download repo, 
2. Initialize virtual environment in it: `python -m venv env`,
3. Run that venv: \
    LLINUX or MAC `source env/bin/activate`, \
    WINDOWS google say `\env\Scripts\activate.bat` if it doesnt work do it `cd env` `cd Scripts` `activate` `cd ..` `cd ..`
4. Install dependencies: `pip install -r requirements.txt`,
5. Create a new file such as `.env.example` in `advent_calendar` and chance his name to `.env`
6. Create a new secret key: `python generateSecretKey.py`
7. Copy it and paste it into `advent_calendar / .env` up to SECRET_KEY \
    e.g. `SECRET_KEY=n-9#+mf&sziujs^g1!+liv5gn@%0*)7dp)gtm^16eqyl+bvjlr`
8. (optional) Change database settings in settings.py if you want to use different (non-sqlite) db backend, 
9. Make migrations: `python manage.py makemigrations`,
10. Migrate database: `python manage.py migrate`,
11. Create admin: `python manage.py createsuperuser`,
12. To run dev server: `python manage.py runserver`

### with Docker
1. Download repo
2. Run docker-compose up in it
3. Ready. Thing is accessible at localhost:8000. Stopping and starting containers again results in making whole new migrations and reseting database (sqlite) content. 

## Tips for devs

### Dumping pip installations into the file
If you installed new pip dependency you need to allow others to know about it. To do so it is best to save all requirements
in one file, which in this case in named `requirements.txt`. You can do this by typing following command: 

`pip freeze > requirements.txt`

## Deploy Nginx
- install Nginx, download app
- nginx configuration, **remember to change server_name**: 
```
server {
    listen 80;
    server_name HOSTNAME_HERE;

    location / {
        include proxy_params;
        proxy_pass http://localhost:8000;
    }
}
```
- ln -s do enabled,
- wszystko dalej jak w *how to install*,
- allowed hosts - add host
- if table doesnt exist: `python manage.py makemigrations; python manage.py migrate`
- create admin: `python manage.py createsuperuser` and follow instructions

### Adresses api
-/api/tasks/all/     __get all tasks 
-`/api/tasks/all/id/`     __get one task by id

-/api/tasks/now/     __get all tasks with taskDate <= today
-`/api/tasks/now/id/`    __get one tasks by id (only with taskDate <= today)

-/api/tasks/answer     __post userAnswer and check if it is correct (return true or false)

-/api/today/     __get today's date

-/admin/     __admin panel

Api is sort by taskDay.
