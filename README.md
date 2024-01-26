## Web statement

This project is a website that allows you to keep track of student grades, view and edit them. Backend is implemented using the Django framework.

## Locally running

### Step 0. Setup environment variables in .env file
```
db_user=...
db_password=...
db_name=...
db_host=...
db_port=...
```

### Step 1. Install dependencies
```shell
pip install -r requirements.txt
```


### Step 2. Update database
```shell
python manage.py migrate
```

### Step 3. Run Django App
```shell
python manage.py runserver
```

## Migrations

### Make new migration
```shell
python manage.py makemigrations
```

### Pull new migrations to database:
```shell
python manage.py migrate
```


