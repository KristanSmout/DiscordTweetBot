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
    f = open(dir_path + '/LastTweet.txt', 'r')
    LastTweet = f.read()



    print('client Ready')
    print('Read Tweet | ' + LastTweet)

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
                channel = client.get_channel(int(715645031633125396))
                await channel.send('```' + LastTweet + '```')
        time.sleep(60)

client.run(discord_token)