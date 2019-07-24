# Django : 

### getting started with django (for windows): 

download chocolaty : 

open you CMD by right click and `Run as administrator`

copy and paste the following to download the windows package manager : 

```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```
*then to download python*

run `choco download python`


---

*for using another great command toll download Cmder from [here](https://cmder.net/), download it and exctract it to your Dev folder*

run Cmder and to check if installed correctly run `python --version`


---

1. set up project folders : 

CD into a Dev folder , and then mkdir a new project folder and then CD into it 

2. ``` pip install virtualenv ```

3. ``` virtualenv <venv> ```

4. ``` <venv>\Scripts\activate ```

5. ``` pip install django ```

6. ``` django-admin startproject <project_name> ```

*if you want to run the project CD into it and then* ``` python manage.py runserver ```

7. cd into the project folder and ``` python manage.py migrate ```

8. ``` pip freeze > requirements.txt ```

9. ``` pip install -r requirements.txt ```

10. `notepad .gitignore` then add the content to the gitginore file 

11. `git init`

*if first time to use git :*
`git config --global user.email "email@email.com"`
`git config --global user.name "username"`

12. `git add .` to add it to a local branch 

13. `git commit -m "message" `

14. to add to a remote repo, create a repo and then `git remote add origin https://github.com/kurdi89/Django.git` 

15. to push for the first time : `git push -u origin master` 

*for later changes use :*
`git status`, `git add .`, `git push`


### to start an app : 

16. `python manage.py startapp <app_name>`

17. register the app in the INSTALLED_APPS array in the settings.py

18. create a basic view   

19. in the *view.py* inside the app folder add : 
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("<h1> Hello</h1>")
```
and in the *urls.py* file in the project folder add : 
```python
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.test, name='test')
]
```
now visit *localhost:8000/hello/* you should see an HTTP response of "Hello".

### Creating a tamplate and passing contexts : 
20. create a *template* folder inside each app you create to handle all the templates, this folder should contain all the HTML files, 
in the app folder change the *view.py* to :

``` python 
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    context = {
        "title" : "First Django app",
        "msg" : "Enjoy coding with Django",
    }
    return render(request, "index.html", context)
```
create *index.html* file in the template folder inside the app as : 

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{title}}</title>
</head>
<body>
    {{msg}}
</body>
</html>
```
and the *urls.py* in the main project should remain the same.
visit, *localhost:8000/hello*

--- 

### list view of a dictionary : 

21. update the views file and add : 
```python
def list_view(request):
    context = {
        "object_list": [
            {
                "title":"some title",
                "body":"some body description",
            },
            {
                "title":"some title",
                "body":"some body description",
            },
            {
                "title":"some title",
                "body":"some body description",
            },
        ],
        "title" : "this is the page title",
        "content" : "this should be a body for the page",
    }
    return render(request, 'list_page.html', context)
``` 
update the *urlspatters* in urls.py to : 
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.test, name='test'),
    path('list-view/', views.list_view, name='list_view')
]
```
create an HTML page for the list view in the template folder name it _list_view.html_: 
```HTML 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{ title }}</title>
</head>
<body>
    {{  content  }} <br>

    the list : <br> 

    {%  for article in object_list  %}
        {{article.title}}: <br>
        {{article.body}} <br>
    {%  endfor  %}
</body>
</html>
```
visit : *localhost:8000/list-view*

---
### Creating databses models : 

22. in your app, find *models.py* file and add your model like : 
``` python
class Book(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField()
    published_on = models.DateField() #auto_now_add=True 
    author = models.CharField(max_length=120)
    pages = models.PositiveIntegerField() #only positive numbers allowed
    def __str__(self):
        return self.title
```
*always remember to make migrations after each time you create/update your database models, usually when you update it asks for 2 questions, set default manually*

23. run `python manage.py makemigrations` then `python manage.py migrate`

24. register your model in your app folder, find _admin.py_ and add:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```
---
### Create an admin user : 

25. run `python manage.py createsuperuser` , enter username, email, password

your model should be registered for the admin panel, visit `localhost:8000/admin/` to confirm.

### migrating to a database, SQL or Postgres : 
for _Postgres_ , in settings.py, add the following in the DATABASES array and comment the sqlite3 option,
*( important : you should already have postgres and pgadmin already installed on your machine)*

*to use _Postgres_ database you will also need to install python package named : psycopg2*

- run only if you want to use Postgres : `pip install psycopg2` then `pip freeze > requirements.txt` to add it to the list of requirments

```
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'Cool',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': 'localhost',
    'PORT': '',
}

```
---
##### Create a super user for accessing the admin panel at *localhost:8000/admin*
in the project folder 

---
## Cloning a repo : 

- `cd <directory>`

- install venv : ` virtualenv <venv> ` and ` <venv>\Scripts\activate `

- clone the repo : `git clone <link>` 

- `pip install -r requirements`
