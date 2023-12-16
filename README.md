## Locally running

### Step 1. Setup environment variables 
```
db_user=...
db_password=...
db_name=...
db_host=...
db_port=...
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
