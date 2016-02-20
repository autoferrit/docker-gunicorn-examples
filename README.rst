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


1. It will create the directory ``/deploy/app`` and a few files will be placed
into ``/deploy`` and your ``app`` directory will be pushed into ``/deploy/app`` with
the ``requirements.txt`` located at /deploy/app/requirements.txt`. which would be
automatic if your is already in your ``app/`` directory.


2. The gunicorn config file is located at '/deploy/gunicorn_conf.py` and you
only need to add your own if you do not want the defaults. The file is included
with the repo to show what is used by default. To include your own, simply
uncomment the proper lines in the ``Dockerfile``

3. Doesnt use a webserver. I specifically dont use a webserver here such as
``nginx`` or ``apache``. Currently I use the new
`Docker Cloud <http://cloud.docker.com>`_ system and simply configure my nginx
service to accept a reverse proxy from an ``app`` host that is generated when
linking the containers. The image I use is
`jwilder/nginx-proxy <https://github.com/jwilder/nginx-proxy>`_. But you could
easily configure it any way needed. You could also easily add ``nginx`` into your
apps dockerfile as well.


USAGE
*****


Each of the root directories represents an example for the framework the
directory is named for. Each has a ``Makefile`` to help get started.

REQUIREMENTS
************
In order to get these working inside of docker, you need to have docker runnin
on the target machine. If local, then you need docker-toolbox on windows and OSX
or simply docker installed on a linux environment (docker-toolbox is also
available on linux). Once you are able to run commands such as ``docker ps``
that means you are good to go.

To start, all you need to do is ``cd`` into an example directory, and run the
commands:


``make build``


then

``make run``


and if you are using docker-toolbox your app is available at
``http://192.168.99.100:5000/``

If you are running this without docker, you should be able to run the app with
gunicorn and supervisor easily. You can see the example ``supervisord.conf``
and ``gunicorn_conf.py`` files for examples, as well as the parent docker
images. You can also create an issue to ask a question if you like.


CONTRIBUTING
------------
If you have any other examples on usage, feel free to submit a PR on your use
case and I would love to add it. I am also open to submitting issues if you find
a bug

`Docker Supervisor Issues <https://github.com/SkiftCreative/docker-supervisor/issues>`_

`Docker Gunicorn Issues <https://github.com/SkiftCreative/docker-gunicorn/issues>`_
