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

# tDate = datetime.date.today()# + datetime.timedelta(days=1)
# dateStr = str(tDate)
# year = dateStr[0:4]
# day = dateStr[5:7]
# month = dateStr[8:10]
# print(dateStr + year + day + month)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if '.joinwaitlist' in msg.content.lower():
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
        #pause.until(datetime(year, day, month, 9))
        os.system('/home/reese/personal_projects/microcenter_bot/startmcbot.sh {} {} {} {} {}' .format(str(firstName), str(lastName), str(phoneNumber), str(discChannel), str(discAuthor))) 
        #await msg.channel.send(firstName + " " + lastName + " has been added to the waitlist! Check your texts to see what position you are in line.")
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)