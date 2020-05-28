import sys,tweepy,tweepy.api,discord,time,os,discord
from discord.ext import tasks, commands

discord_token = 'NzE1NjQyOTkwOTExMTYwMzQw.XtAS2g.XU4a242fVmlP-XHjQXIIPgUs7DM'
client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(int(715645031633125396))
    await channel.send('Hello')


client.run(discord_token)