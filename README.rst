=====================
Python in your Docker
=====================

This is an example on how to use my docker image:

`SkiftCreative/gunicorn <https://hub.docker.com/r/skiftcreative/gunicorn>`_

In this repo, there is an example on deploying both flask (a very popular wsgi
framework, and falcon (a fask framework focused on building restful api's). The
falcon example should also work fine with the
`hug framework <https://github.com/timothycrosley/hug>`_ as well

For each, simple copy the ``flask`` or ``falcon`` directories into a new project,
or copy the contents into an existing one to use. All you need to do is update
the ``supervisor.conf`` if needed but should be ready to go in most cases.

These images do however, assume a few things.

1) It will create the directory ``/deploy/app`` and a few files will be placed
into ``/deploy`` and your ``app`` directory will be pushed into ``/deploy/app`` with
the ``requirements.txt`` located at /deploy/app/requirements.txt`. which would be
automatic if your is already in your ``app/`` directory.

2) The gunicorn config file is located at '/deploy/gunicorn_conf.py` and you
only need to add your own if you do not want the defaults. The file is included
with the repo to show what is used by default. To include your own, simply
uncomment the proper lines in the ``Dockerfile``

3) Doesnt use a webserver. I specifically dont use a webserver here such as
``nginx`` or ``apache``. Currently I use the new
`Docker Cloud <http://cloud.docker.com>`_ system and simply configure my nginx
service to accept a reverse proxy from an ``app`` host that is generated when
linking the containers. The image I use is
`jwilder/nginx-proxy <https://github.com/jwilder/nginx-proxy>`_. But you could
easily configure it any way needed. You could also easily add ``nginx`` into your
apps dockerfile as well.


CONTRIBUTING
------------
If you have any other examples on usage, feel free to submit a PR on your use
case and I would love to add it. I am also open to submitting issues if you find
a bug

`Docker Supervisor Issues <https://github.com/SkiftCreative/docker-supervisor/issues>`_
`Docker Gunicorn Issues <https://github.com/SkiftCreative/docker-gunicorn/issues>`_
