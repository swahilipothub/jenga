# README #

### What is this repository for? ###

* The project is about sending messages to multiple recipients (bulk sms)
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Download the project or clone from the repo
* Do a pip install -r requirements.txt to install dependencies
* You should have an africastalking account https://africastalking.com/.
  get your API key and username from your account
* Create a secrets.py file on the same directory as settings.py and add the following

SECRET = os.environ.get(
    'SECRET_KEY', "your project's secret key")

USERNAME = "your username"
APIKEY   = "your api key"


* Run python manage.py migrate
* Run python manage.py runserver

### To Do List ###

* Project documentation
* Add email backend - Ziri
* Change to PEP8 format - Brighton
* Add search functionality
* Admin dashboard - for charts, graphs
* import contacts from csv, excel

### Issues ###

* Caching
* Rename apps a.k.a remove sph_ from the app names

### Who do I talk to? ###

* Repo owner/admin @athmanziri, @bmwasaru
* Team contacts @ckchivatsi

### Site URL ###
http://jenga-io.herokuapp.com/
