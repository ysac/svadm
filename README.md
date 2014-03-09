svadm
=====

This application is used to manage the server.
It is made with django is a python framework.

memo
====

% cd ~/work/svadm

runserver
% sudo python manage.py runserver 192.168.10.10:80

db
% python manage.py sql svinfo
% python manage.py syncdb

git
% git commit -a -m 'comment'
% git push -u origin master
