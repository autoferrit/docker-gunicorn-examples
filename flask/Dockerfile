FROM skiftcreative/gunicorn:latest

# for proxies: "unix:/deploy/run/gunicorn.sock"
# ENV GUNICORN_BIND='0.0.0.0:5000'

COPY app /deploy/app

RUN pip3 install -U -r /deploy/app/requirements.txt

# uncomment to use your own supervisord.conf
# default will work for flask easily
# COPY supervisord.conf /etc/supervisord.conf

# if you need your own gunicorn_conf.py, uncomment this line
# COPY gunicorn_config.py /deploy/

WORKDIR /deploy/app
