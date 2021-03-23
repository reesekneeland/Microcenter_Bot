import time
import random
import os
import discord
import subprocess
import shlex
import sys
import pause
import datetime
from datetime import date
from datetime import timedelta
from subprocess import Popen,PIPE
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display 

#display = Display(visible=0, size=(1024, 768)) 
#display.start() 
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    try:
        if '.joinwl' in msg.content.lower():
            text = msg.content
            args = text.split(' ')
            firstName = args[1]
            lastName = args[2]
            phoneNumber = args[3]
            discChannel = msg.channel.id
            discAuthor = msg.author.id
            print(firstName, lastName, phoneNumber, discChannel, discAuthor)
            await msg.delete()
            await msg.channel.send("Adding " + firstName + " " + lastName + " to the waitlist!")
            os.system('/home/reese/microcenter_bot/startmcbot.sh {} {} {} {} {}' .format(str(firstName), str(lastName), str(phoneNumber), str(discChannel), str(discAuthor))) 
    except:
        await msg.channel.send("An error occured! This person has not been added to the waitlist! Please try again and make sure you are using the input command correctly")
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)