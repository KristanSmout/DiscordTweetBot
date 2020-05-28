import sys,tweepy,tweepy.api,discord,time,os,discord
from discord.ext import tasks, commands
dir_path = os.path.dirname(os.path.realpath(__file__))
t = open(dir_path + '/Tokens.txt', 'r')
Tokens = t.read()
Tokens = Tokens.split(',')

#Populate your twitter API details below
consumer_key = Tokens[0]
consumer_secret = Tokens[1]
access_token_key = Tokens[2]
access_token_secret = Tokens[3]
discord_token = Tokens[4]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

client = discord.Client()

userID = "dividendcut"

f = open(dir_path + '/LastTweet.txt', 'r')

LastTweet = f.read()
Token = discord_token
client.run(discord_token)
#f.close()



@client.event
async def on_ready():
    print("Investment Bot Is Ready!")
    LastTweet = f.read()
    print('Read Tweet | ' + LastTweet)
    i = 0
    while(True):
        i = i + 1
        print('Loop: ' + str(i))
        tweets = api.user_timeline(screen_name=userID, 
                                    count=10,
                                    include_rts = False,
                                    tweet_mode = 'extended'
                                    )

        for info in tweets[:1]:
                # print(info.full_text)

                
            if(info.full_text != LastTweet):
                LastTweet = info.full_text
                f = open(dir_path + '/LastTweet.txt', 'w+')
                f.write(LastTweet)
                f.close()
                Channel = client.get_channel('715645031633125396')
                Channel.send(LastTweet)
        time.sleep(60)
    
