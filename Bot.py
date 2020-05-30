#Author:       Kristan Smout
#description : Discord bot to read last tweet from user and send it to a discord server. Has restart support to not double send tweets
#date :        28/05/2020

import sys,tweepy,tweepy.api,discord,time,os,discord
from discord.ext import tasks, commands

dir_path = os.path.dirname(os.path.realpath(__file__))
t = open(dir_path + '/Tokens.txt', 'r')
Tokens = t.read()
Tokens = Tokens.split(',')
discord_token = Tokens[4]
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    t = open(dir_path + '/Tokens.txt', 'r')
    Tokens = t.read()
    Tokens = Tokens.split(',')

    consumer_key = Tokens[0]
    consumer_secret = Tokens[1]
    access_token_key = Tokens[2]
    access_token_secret = Tokens[3]

    print(Tokens[0])
    print(Tokens[1])
    print(Tokens[2])
    print(Tokens[3])

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)

    userID = "dividendcut"
    userID2 = "dividendhike"
    f = open(dir_path + '/LastTweet.txt', 'r')
    f2 = open(dir_path + '/LastTweet2.txt', 'r')
    LastTweet = f.read()
    LastTweet2 = f2.read()



    print('client Ready')
    print('Read Tweet | ' + LastTweet)
    print('Read Tweet | ' + LastTweet2)

    i = 0
    while(True):
        i = i + 1
        print("Loop: " + str(i))           
        tweets = api.user_timeline(screen_name=userID, count=10, include_rts = False, tweet_mode = 'extended')
        for info in tweets[:1]:
            if(info.full_text != LastTweet):
                LastTweet = info.full_text
                f = open(dir_path + '/LastTweet.txt', 'w+')
                f.write(LastTweet)
                f.close()
                channel = client.get_channel(int(708242642714099743))
                await channel.send('Dividend Decreased/Removed')
                await channel.send('```diff\n' + '-' + LastTweet + '```')
        
        tweets2 = api.user_timeline(screen_name=userID2, count=10, include_rts = False, tweet_mode = 'extended')
        for info in tweets2[:1]:
            if(info.full_text != LastTweet2):
                LastTweet2 = info.full_text
                f2 = open(dir_path + '/LastTweet2.txt', 'w+')
                f2.write(LastTweet2)
                f2.close()
                channel = client.get_channel(int(708242642714099743))
                await channel.send('Dividend Increased/Enabled')
                await channel.send('```diff\n' + '+' + LastTweet + '```')
        time.sleep(60)

client.run(discord_token)