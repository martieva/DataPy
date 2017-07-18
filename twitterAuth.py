from tweepy import OAuthHandler

def authenticate():
    consumer_key = 'GFsey33HimW9TvQXgMytM5BHP'
    consumer_secret = 'cFVwnOpTOVeT8XnfmCBQFEZ76NNk5ERPeV9gRibNfYo31BOATv'

    access_token = '817403502255370242-ZRLI7aRhGzrufdIpQng173HvX6ISB5I'
    access_token_secret = '3KbIMDCPv0boDVUHHZVHRqZKbFNe7sZv4pIn4CEMF0q7J'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth
