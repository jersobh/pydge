# Pydge Framework

Pydge is a python 3.5+ framework using async.io, jinja2 and peewee ORM.

### Install

First install the requirements.txt

```sh
$ cd /path/to/pydge
$ pip install -r requirements.txt
#or sudo pip install -r requirements.txt
```
It will install all required python packages.

### Configure

You may need to adjust some settings based on your own enviroment. The /core/conf.py file holds those confs.

 DB = (string) Your db name
 DB_USER = (string) Your db's user
 DB_PASS = (string) Your db's password
 DB_PORT = (int) Your db's port, like 3306 (mysql) or 5432 (postgresql)
 DB_TYPE = (string) Possible options are: sqlite, mysql, postgresql
 APP_PORT = (int) The port used by your app. Default's 8080, so it can be accessed on http://localhost:8080
 GENERATE_MODELS = (bool) If is set True, then the models will be automagically generated. You may set False after running a first time, because you may not want to re-generate it each request.

### Run
Pydge requires python 3.5+. I'm on Arch linux, and I have python 3.6 installed.

```sh
$ python3.6 server.py
```

### Templating
Pydge uses jinja2 template engine. You can read the docs on [Templates](http://jinja.pocoo.org/docs/2.9/templates/) and [API](http://jinja.pocoo.org/docs/2.9/api/).

### Usage
Usage examples are inside the framework itself. Just follow the instructions on Examples menu.
