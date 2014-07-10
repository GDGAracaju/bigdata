from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(['Copa', 'Mundo', '2014']) # let's define all words we would like to have a look for
    #tso.setLanguage('de') # we want to see German tweets only
    tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '{digite}',
        consumer_secret = '{digite}',
        access_token = '{digite}',
        access_token_secret = '{digite}'
     )

    for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
        print tweet
        #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)