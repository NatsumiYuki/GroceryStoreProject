# 🛒 Building a Wish List App with Django

### Project Overview

I'm developing a full-featured Wish List web application using:
  - Backend: Django (Python)
  - Frontend: HTML, CSS, JavaScript
  - Database: MySQL
  - Additional: Bootstrap for responsive design

color pallet: https://coolors.co/e1b5b9-f8c7cc-81a684-6c9778-57886c-466060-0e0f19

### Here's a breakdown of how Django works:
### 1.0 Setting up enviroment

Create a Virtual Environment.
```
python -m venv my_env
```
Activate the Virtual Environment
```
my_env\Scripts\activate
```
Install Django
```
pip install Django
```
Create Django Project
```
django-admin startproject myproject .
```
Run Development Server
```
python manage.py runserver
```

When starting your project you'll get the following files:

```
myproject/          # Root project directory
├── manage.py       # Command-line utility
└── myproject/      # Project package (Python package)
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

### 1.1 Manage.py
This is Django remote control.
- You use it to:
- Run the server
- Create apps
- Apply database migrations
- Create users
- Run Django commands

### 1.2 Settings.py
One of the most important files in Django, it's like a central command center.
It stores all configuration of your project:
- Database settings
-Installed apps
- Middleware
- Security keys
- Allowed hosts
- Static & Media files
- Templates

### 1.3 Urls.py
Controls routing / where each URL should go.
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]
```
### 1.4 asgi.py / wsgi.py 
These files connect your Django app to a server (rarely use these files).
- wsgi.py → used for normal HTTP servers
- asgi.py → supports async operations like WebSockets

### 2.0 Django Apps — The Building Blocks
Inside a project you create apps
Each app is like a module:
- blog
- users
- products
- payments
- api

Each app is independent, which makes Django scalable.

### 2.1 Models.py
Where you define database tables using Python classes.
```
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
```
🌟 This is Django’s ORM (Object Relational Mapping).

resuming Instead of writing SQL manually, you describe the table in Python, and Django builds it. (It can also be linked with MySQL or any other Database)

### 2.2 Views.py
Contains the logic of your app.
```
def home(request):
    return render(request, 'home.html')
```
Views are like the brain of your website, they decide what to show and how to respond.

### 2.3 urls.py inside the app

You create this manually.
```
urlpatterns = [
    path('', views.home),
]
```
This connects URLs → Views just inside the app.

### 2.4 Admin.py
Connects your models to Django’s Admin interface.
```
admin.site.register(Product)
```

### 2.5 migrations/
This folder stores database change history.
Every time you change a model:
```
python manage.py makemigrations
python manage.py migrate
```
Django updates the database automatically.

### 3 Templates - Frontend
Templates use Django’s own syntax:
- {{ }} → variables
- {% %} → logic

### 4. Static & Media Files
myapp/ static/ css  js  images/
Media files:

Uploads from users (profile pictures, documents, etc.).
Both are configured in settings.py.

### 6. The Django Request Lifecycle

    User Request
         |
         v
      URLconf
         |
         v
        View  <----->  Model (Database)
         |
         v
     Template
         |
         v
    HTTP Response






