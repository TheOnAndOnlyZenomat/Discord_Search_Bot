import discord
from discord.ext.commands import Bot
from discord.ext import commands
import uyts

Bot_Prefix = ("?", "!")
client = Bot(command_prefix = Bot_Prefix)
bot=commands.Bot(command_prefix='?')

async def link(ctx, arg):
    search_resp = uyts.Search(arg)
    video = 'https://www.youtube.com/watch?v=' + search_resp.results[0].id
    await ctx.channel.send(video)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name='RickRoll')
async def on_message(ctx):
    await ctx.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@client.command(name='search')
async def on_message(ctx, arg): #checks the message for ctx (which channel, how activated) and stores the argument as a raw string
        await link(ctx, arg)

client.run('')
