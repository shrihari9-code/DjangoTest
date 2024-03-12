# Create a virtual environment (optional but recommended):

```shell
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

# install dependencies:

```shell
pip install -r project/requirements.txt
```

# Run database migrations

```shell
python manage.py makemigrations
python manage.py migrate
```

# Start the development server:

```shell
python manage.py runserver
```

# To clear the DB

```shell
python manage.py flush
```
