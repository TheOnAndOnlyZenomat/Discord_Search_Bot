import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time
from selenium import webdriver #imports the webdriver through selenium
from selenium.webdriver.common.keys import Keys #imports keystrokes for automated use through selenium
from selenium.webdriver.chrome.options import Options
import os


Bot_Prefix = ("?", "!")
client = Bot(command_prefix = Bot_Prefix)
bot=commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name='RickRoll')
async def on_message(ctx):
    await ctx.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@client.command(name='search')
async def on_message(ctx, *, arg): #checks the message fpr ctx (which channel, how activated) and stores the argument as a raw string
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors') #ignores certificate errors in automated use
        options.add_argument("--test-type")
        driver = webdriver.Chrome('F:/Downloads/chromedriver.exe', options = options) #path to the chromedriver.exe
        driver.get("https://www.youtube.de") #opens youtube.de
        element = driver.find_element_by_id("search") #finds the searchbar on youtube
        element.send_keys(arg, Keys.RETURN) #searches for the the searchitem specified as arg and presses Return
        time.sleep(1)
        a=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
        #line 33 defines "a" as the element "title"
        b=a.get_attribute('href') #stores the link of the first video as b
        await ctx.channel.send(b) #sends the link into the channel
        driver.quit() #closes the chrome window

client.run('')
