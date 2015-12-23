from django.shortcuts import render

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage



def index(request):

    return render(request, 'index.html')


def push(request):

    redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
    message = RedisMessage('Hello World')
    # and somewhere else
    redis_publisher.publish_message(message)

    return render(request, 'push.html')

