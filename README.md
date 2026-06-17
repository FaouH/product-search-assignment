# Product Search Assignment
Hester Faou - June 16th, 2026

This is a Django application for a cafe website which lets users search and filter products by description, category, and tags.

## Features

* Search products by name or description
* Filter products by category
* Filter products by one or multiple tags
* Combine search and filters together

## Assumptions

* Search matches either product name or description
* Tag filtering supports multiple selections; results will include only products that match all selected tags.
* Category and tag filters can be combined with search

## Tech Stack

* Django
* SQLite
* Bootstrap 4

## Setup Instructions

1. Clone repository

```bash
git clone https://github.com/FaouH/product-search-assignment.git
cd product-search-assignment
```

2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser

```bash
python manage.py createsuperuser
```

6. Run server

```bash
python manage.py runserver
```
Open the main application in browser: 
```
http://127.0.0.1:8000/
```

7. Access the Django admin:

```
http://127.0.0.1:8000/admin
```


## Running Tests

```bash
python manage.py test
```

## Database/sample data
A pre-populated db.sqlite3 file is included in this repository to demonstrate the sample dataset that was created through the Django admin interface, as required by the assignment.

