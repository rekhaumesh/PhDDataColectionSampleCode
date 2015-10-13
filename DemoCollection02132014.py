'''
Created on Jun 30, 2013

@author: user
'''
import os
import json
import csv
import networkx
import sys
import getopt
import os
import re
import csv
import httplib, urllib2
import simplejson
import urllib2
import random
import time

from urllib2 import URLError
from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance
from datetime import datetime
from twython import Twython, TwythonError

""" Authentication Keys required for Twitter Authentication """
searchURL = "https://api.twitter.com/1.1/search/tweets.json?q=obama&count=2&result_type=popular"
CONSUMER_KEY= "uU0bI3LuQ5Moo7wdvIxQEw"
CONSUMER_SECRET= "4lo9zskxrPYecKSrMhWKYD1Cao1VvHtWUqdts6BKs"
ACCESS_TOKEN_KEY = "338855399-PFZntDQMPgcayof7EkIicmtZzlAV6xEPjtHwZ8PG"
ACCESS_TOKEN_SECRET = "rvwRY4izlOF1RHJDn5AiwWAOe6BsrixowVt5QzBEGE"

"""Initializing all the global variables used in the program """


"""DEFINE Ends here"""
"""TEMP defines - REMOVE AFTER FINAL Programing """

movie_file_path = 'D:/IIT Kharagpur/TwitterDataJuly2013/searchoptions/mobiles.txt'
locn_file_path = 'D:/IIT Kharagpur/TwitterDataJuly2013/searchoptions/locations.csv'


"""TEM Ends here  """

""" TWYTHON Programming """
""" Functions """

def start_time():
    str_time = time.clock()
    return str_time
    
def elapsed_time(st_time):
    cls_time = time.clock()
    total_time = cls_time - st_time
    print 'my program running for: ', total_time
    return total_time

def wait_15(wait_time):
    print 'sleeping now....'
    wait_time = int(wait_time)
    time.sleep(wait_time)
    return

def storing_tweets(f_mvie,f_loc,f_usr_name,f_usr_loc,f_usr_text,f_retws,f_flws,f_frds,f_posts):
    timestr = time.strftime("%Y%m%d")
    timestr_f = time.strftime("%Y%m%d-%H%M%S")
    tweetDir = 'D:/IIT Kharagpur/TwitterDataJuly2013/'+f_mvie+'/'+f_loc+'/'+timestr+'/'
    full_tweet_string = f_usr_name + ":" + f_usr_loc + ":" + f_usr_text + ":" + str(f_retws) + ":" + str(f_flws) + ":" + str(f_frds)
    if not os.path.isdir(tweetDir):
        os.makedirs(tweetDir)
        print "Tweet directory created"
    filename = tweetDir + 'day_' + str(int(random.random()*1000)) + '_' + timestr_f +'.txt'
    outfile = open(filename, 'wb')
    print full_tweet_string
    outfile.write(full_tweet_string)
    outfile.close()
        
    #except:
    #    print "Did not create TWeet directory"
    #    pass        

def mySearch(query,language,loc,sinId,maxId,restype,numbs):
    #from twython import Twython, TwythonError
    try:
        search_results = twitter.search(q=query,lang=language,geocode=loc,since_id=sinId, max_id=maxId,result_type=restype,count=numbs,include_entities=True)
        #print search_results
        #print search_results['search_metadata']['since_id']
        return search_results
    except TwythonError:
        print "search resulted None"
        pass
    except TypeError:
        print "search resulted None"
        pass
    #except (SSLError):
    #    print ' SSL Error', time.clock()
    #    pass
    except:
        print 'Search resulted None'
        pass
def read_movie_file(movie_file):
    try:
        movie_name = open(movie_file,'r')
        return movie_name
    except:
        print "FIle read error"
        exit

def read_location_file(locn_file):
    try:
        #locn_name = open(locn_file,'r')
        locn_name = csv.reader(open(locn_file,"rb"))
        return locn_name
    except:
        print "FIle read error"
        exit

        
def initialize_all():
    global s_sinID
    s_sinID = 0000000
    global s_maxID
    s_maxID = 1000000000000000000000
    #s_maxID = 351017381541318657000
    global s_type
    s_type ='recent'
    global s_count
    s_count = 100
    global s_lang
    s_lang = 'en'
    return

def initialize_mv(s_movie):
    global s_query
    s_query = s_movie
    #s_query = (s_movie + " " + "-RT")
    #USE THIS -RT filter only if you DO NOT want RTs. No RTs will appear at all 
    
def initialize_locn(s_locn):
    global s_location 
    s_location = s_locn[1] + "," + s_locn[2] + "," + s_locn[3]
    #s_location ='34.0522342,-118.2436849,200mi'
    

def myTweets(my_tws,mve,lc):
    ID=0
    tweet_count=0
    for sg_twt in my_tws['statuses']:
        try:
            tweet_count += 1
            try:
                usr_text = str(sg_twt['text'])
                try:    
                    RTcount= sg_twt['retweet_count']
                except:
                    print 'RT count error'
                    pass
                try:
                    """USER name, Location details """
                    usr_info = sg_twt['user']
                except:
                    print 'user info error'
                    pass
                try:
                    usr_name = usr_info['name']
                except:
                    print 'User name info error'
                    pass
                try:
                    usr_location = str(usr_info['location'])
                except:
                    print 'User location error'
                    pass
                try:
                    usr_fol_cnt = usr_info['followers_count']
                except:
                    print 'usr followers count error'
                    pass
                try:
                    usr_frd_cnt = usr_info['friends_count']
                except:
                    print 'user friends count error'
                    pass
                try:    
                    usr_msgs_post_cnt = usr_info['statuses_count']
                except:
                    print 'post count error'
                    pass
                try:
                    ID = sg_twt['id_str']
                    print ID
                except:
                    print 'since_ID error'
                    pass
                try:    
                    #print usr_name, ":", usr_location, ":",usr_text, ":", RTcount, ":", usr_fol_cnt,":" ,usr_frd_cnt, ":",usr_msgs_post_cnt 
                    storing_tweets(mve,lc,usr_name,usr_location,usr_text,RTcount,usr_fol_cnt,usr_frd_cnt,usr_msgs_post_cnt)
                except:
                    print "storing error"
                    pass
                
            except:
                print 'Tweet does not exist'
                sys.exc_clear()
                #pass
        except (TypeError,UnicodeEncodeError,TwythonError):
            print "empty object-no tweets at all"
            #pass
            continue
        #continue
    
    print 'ID', type(ID), ID
    return ID, tweet_count
    
"""Functions ends here"""

"""MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN starts here"""
""" Twitter Authentication """
from twython import Twython, TwythonError
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)
twitter.get_home_timeline()

"""Twitter Authentication Ends here"""
#s_sinID = 0000000
#s_maxID = 1000000000000000000000
#s_type ='recent'
#s_count = 100
#s_lang = 'en'
#Read movie file
for movie in read_movie_file(movie_file_path):
    #initialize_all()
    movie = movie.rstrip('\n')
    initialize_mv(movie)
    #s_query='The Heat'
    #read location file
    for loc in read_location_file(locn_file_path):
        initialize_all()
        initialize_locn(loc)
        #s_location = '51.509,-0.126,300mi' #London
        print "Tweets are from: ", s_query, "and", s_location, loc[0]
        each_ln_tw=0
        for i in range(1,11):
            print 'Before search sinID, maxID', s_sinID, s_maxID
            my_search_res = mySearch(s_query,s_lang,s_location,s_sinID,s_maxID,s_type,s_count)
            try:
                id, tw_cnt = myTweets(my_search_res,movie,loc[0])
                s_sinID = my_search_res['search_metadata']['since_id']
                print id
                s_maxID = int(id) - 1
                each_ln_tw=tw_cnt
                print 'set sinID, mxId for next search:', s_sinID, s_maxID
            except(TypeError):
                pass
            continue
        print "Total tweets per location per movie: ", each_ln_tw*i
        print datetime.now()
        time.sleep(50)
        print datetime.now()
        continue
    continue

