from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, 'pages/home.html')
def tweet_list_view(request, *args, **kwargs):
    print(args, kwargs)
    qs=Tweet.objects.all()
    tweet_list=[{"id":x.id,"content":x.content} for x in qs]

    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args, kwargs)
    """
    USING REST API VIEW
    Allows your app to be consumed by javascript,swift,ruby etc because it returns Json data
    """
    data = {
        "id": tweet_id,

    }
    status = 200
    try:

        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404

    return JsonResponse(data, status=status)
