from django.shortcuts import render
import facebook
import requests

# Create your views here.
def display_post(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['created_time'])




def get_posts(request):
    access_token = 'EAACYred7iOsBAN4wuVM4K7oUGZAZBGTyCPaXGITx8QA6EUHO4ZB41cvDPazpWcJ9SOqLSu4xU96JPiBYvlFBlVmm4TXcbZA8ASTQP7XrT6If4ZBvdoZCFW6NGtDIQp8l6KlECZAZAtik5rUYCPnilfAtLxuJud5ySnbdV0QApjZCgJV985QLKiNJZC'
    # Look at Bill Gates's profile for this example by using his Facebook id.
    user = 'BillGates'

    graph = facebook.GraphAPI(access_token)
    args = {'fields' : 'likes, about, bio, name', }
    labourparty = graph.get_object('labourparty', **args)
    print format(labourparty['about'])
    context_dict = {'labourparty':labourparty}

    return render(request, 'facebook/posts.html', context=context_dict)
