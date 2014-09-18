from twython import Twython

TWITTER_APP_KEY = 'NdVsX7fpoa9cih1B9izrPtXvi' #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'K6ypL0i89Rmt2jyvGeMsHELBbASQ7FBo3sPZQjNK0WBI52m0mM' 
TWITTER_ACCESS_TOKEN = '2791249638-PtuD99YkHrIWgstyXETODGT9OqtAKcd9kPP0udA'
TWITTER_ACCESS_TOKEN_SECRET = 'dJTEUNTzpUtPdfwOp9J2hwzmhVVMZGhsQItVgyIfzEFs9'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#festember',   #**supply whatever query you want here**
                  count=10)

tweets = search['statuses']

for tweet in tweets:
  print tweet['id_str'], '\n', tweet['text'], '\n\n\n'