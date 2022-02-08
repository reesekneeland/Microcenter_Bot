import time
import random
import os
import discord
import sys
import threading
import multiprocessing
import signal
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display 

def sigint_handler(sig = None, sig2 = None):
    print("\nClosing...")
    try: browser1.close()
    except: pass
    try: browser2.close()
    except: pass
    exit(0)

def refresh1():
    browser1.refresh()

def refresh2():
    browser2.refresh()

def join_waitlist(f, l, p, b):
    first = f
    last = l
    phone = p
    browserId = b
    print("beginning signup")
    if(browserId == 1):
        t_end = time.time() + 3
        while(time.time() < t_end):
            try:
                box2 = browser1.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                continue
            except:
                pass
            try:
                firstnamebox = browser1.find_element_by_css_selector('#name02')
                lastnamebox = browser1.find_element_by_css_selector('#name03')
                phonebox = browser1.find_element_by_css_selector('#phone01')
                firstnamebox.clear()
                lastnamebox.clear()
                phonebox.clear()
                lastnamebox.send_keys(last)
                firstnamebox.send_keys(first)
                phonebox.send_keys(phone)
                break
            except:
                pass
        else:
            return 0
        t_end = time.time() + 30
        while(time.time() < t_end):
            try:
                submit = browser1.find_element_by_xpath('//*[@id="public-waitlist-confirm"]/div/div[2]/div[2]/form/div[1]/button')
                submit.click()
            except:
                try:
                    done = browser1.find_element_by_xpath('//*[@id="public-waitlist-complete"]/div/div[1]/button')
                    print("signup complete!")
                    return 1
                except:
                    pass
        else:
            return 0
        
    elif(browserId == 2):
        t_end = time.time() + 3
        while(time.time() < t_end):
            try:
                box2 = browser2.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                continue
            except:
                pass
            try:
                firstnamebox = browser2.find_element_by_css_selector('#name02')
                lastnamebox = browser2.find_element_by_css_selector('#name03')
                phonebox = browser2.find_element_by_css_selector('#phone01')
                firstnamebox.clear()
                lastnamebox.clear()
                phonebox.clear()
                lastnamebox.send_keys(last)
                firstnamebox.send_keys(first)
                phonebox.send_keys(phone)
                break
            except:
                pass
        else:
            return 0
        t_end = time.time() + 30
        while(time.time() < t_end):
            try:
                submit = browser2.find_element_by_xpath('//*[@id="public-waitlist-confirm"]/div/div[2]/div[2]/form/div[1]/button')
                submit.click()
            except:
                try:
                    done = browser2.find_element_by_xpath('//*[@id="public-waitlist-complete"]/div/div[1]/button')
                    print("signup complete!")
                    return 1
                except:
                    pass
        else:
            return 0
    print("Waitlist open! " + first + " " + last + " has been added!")                

def scan_waitlist(f, l, p):

    first = f
    last = l
    phone = p
    waitlistOpen = False
    errCount = 0

    while(errCount <= 5):
        try:
            while(True):
                loop1 = time.time() + 3
                while(time.time() < loop1):
                    try:
                        box1 = browser1.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                        box1.click()
                        waitlistOpen = True
                        print("joining waitlist in browser1")
                        break
                    except:
                        pass
                    try:
                        check = browser1.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')
                        if(check.is_enabled()): 
                            print("clicking join in browser1")                    
                            check.click()
                            continue
                        else:
                            print("Waitlist not open in browser1, waiting to add " + first + " " + last)
                    except:
                        print("Can't find button in browser1")
                if(waitlistOpen == True):
                    if(join_waitlist(first, last, phone, 1) == 1):
                            print("Joined waitlist! " + first + " " + last + " has been added!")
                            return 1
                    else:
                        errCount += 1
                proc2 = multiprocessing.Process(target=refresh2, args=())
                try:
                    proc2.terminate()
                except:
                    print("unable to terminate proc2")
                proc1 = multiprocessing.Process(target=refresh1, args=())
                proc1.start()
                loop2 = time.time() + 3
                while(time.time() < loop2):
                    try:
                        box1 = browser2.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                        box1.click()
                        print("joining waitlist in browser2")
                        waitlistOpen = True
                        break
                    except:
                        pass
                    try:
                        check = browser2.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')
                        if(check.is_enabled()):                     
                            print("clicking join in browser2")                    
                            check.click()
                            continue
                        else:
                            print("Waitlist not open in browser2, waiting to add " + first + " " + last)
                    except:
                        print("Can't find button in browser2")
                if(waitlistOpen == True):
                    if(join_waitlist(first, last, phone, 2) == 1):
                            print("Joined waitlist! " + first + " " + last + " has been added!")
                            return 1
                    else:
                        errCount += 1
                try:
                    proc1.terminate()
                except:
                    print("unable to terminate proc1")
                proc2.start()

        except:
            errCount += 1
            browser1.refresh()
            browser2.refresh()
            print("Error occurred, refreshing and trying again, error count: " + str(errCount))
            time.sleep(2.5)
    else:
        print("Couldn't get through in 5 retries, exiting...")
        return 0

    
signal.signal(signal.SIGINT, sigint_handler)
load_dotenv()
#display = Display(visible=0, size=(800, 600))         #uncomment if running on a displayless server
#display.start() 

browser1 = webdriver.Firefox(executable_path="./geckodriver")
browser1.execute_script("Object.defineProperty(navigator, 'browser', {get: () => undefined})")
browser1.maximize_window()
browser1.get('https://v2.waitwhile.com/welcome/microcenterstlo')
browser2 = webdriver.Firefox(executable_path="./geckodriver")
browser2.execute_script("Object.defineProperty(navigator, 'browser', {get: () => undefined})")
browser2.maximize_window()
browser2.get('https://v2.waitwhile.com/welcome/microcenterstlo')
print("opened browsers")
time.sleep(3)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(sys.argv[1], sys.argv[2], sys.argv[3])
    channel = client.get_channel(int(sys.argv[4]))
    try:
        if(scan_waitlist(sys.argv[1], sys.argv[2], sys.argv[3]) == 1):
            await channel.send('<@' + str(sys.argv[5]) + "> " + str(sys.argv[1]) + " " + str(sys.argv[2]) + " has been added to the waitlist! Check your texts to see what position you are in line.")
        else:
            await channel.send('<@' + str(sys.argv[5]) + ">  Waitlist process timed out after 5 retries, " + str(sys.argv[1]) + " " + str(sys.argv[2]) + " has not been added to the waitlist! Please try again.")
    except:
        await channel.send('<@' + str(sys.argv[5]) + ">  An error occured, " + str(sys.argv[1]) + " " + str(sys.argv[2]) + " has not been added to the waitlist! Please try again and make sure you are using the input command correctly")
    sys.exit()

TOKEN = TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)

    
