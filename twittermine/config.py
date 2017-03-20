import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = 'iYhNLVyxxiVKuPlMBu3KGRIg5'
        consumer_secret = 'Uh0u2IxifhJF9Z5oRCrwVrUScnGvg3jF7MN46M6rAEcd5TUGkB'
        access_token = '242622210-ZBHnSG3yQ0ymPWm8chqmuFI7F9LGu58Gw1kyn3xL'
        access_secret = 'NWhAbuuViOH2asxjhziElLwiwm9W1JV2lxcDrWFx0GPcY'
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client