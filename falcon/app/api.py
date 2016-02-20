import hug

from .resources import part_1


@hug.get('/')
def say_hi():
    return "Hi from root"


@hug.extend_api()
def with_other_apis():
    return [part_1]
