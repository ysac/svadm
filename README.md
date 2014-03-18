# svadm

This application is used to manage the server.
It is made with django is a python framework.


# TODO

* [x] add role field
* [x] add IPv4/v6 address field
* [x] add LB field
* [x] add comment field
* add VIP class
* create view
* create import batch
* create export batch
* directory setting in templates/*


# memo

## Environment

* VirtualBox + vagrant
* CentOS 6.5
* python 2.6.6
* Django1.6.2

## Workdir

```
% cd ~/work/svadm
```

## Testserver

```
% sudo python manage.py runserver 192.168.10.10:80
```

## Test access

* http://192.168.10.10/
* http://192.168.10.10/admin

## DB

```
% python manage.py sql svinfo
% python manage.py syncdb
```

* db export / inport
```
% python manage.py dumpdata svinfo > dump.json
% python manage.py flush
% python manage.py syncdb
% python manage.py createsuperuser
% python manage.py loaddata dump.json

```

## Git

```
% git add .
% git commit -a -m 'comment'
% git push -u origin master
% git push
```

## Reference

* <http://docs.djangoproject.jp/en/latest/contents.html>
* <http://codechord.com/2012/01/readme-markdown/>


