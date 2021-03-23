import time
import random
import os
import discord
import sys
from dotenv import load_dotenv
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display 

load_dotenv()
#display = Display(visible=0, size=(800, 600))         #uncomment if running on a displayless server
#display.start() 

def join_waitlist(f, l, p):
    first = f
    last = l
    phone = p
    # chrome_options = Options()
    # #chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument('proxy-server=' + get_proxy(0))
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36")
    # chrome_options.add_argument("--disable-gpu")
    # browser1 = webdriver.Chrome("./chromedriver_test", options=chrome_options)
    browser1 = webdriver.Firefox(executable_path="./geckodriver")
    browser1.execute_script("Object.defineProperty(navigator, 'browser', {get: () => undefined})")
    browser1.maximize_window()
    browser1.get('https://v2.waitwhile.com/welcome/microcenterstlo')
    browser2 = webdriver.Firefox(executable_path="./geckodriver")
    browser2.execute_script("Object.defineProperty(navigator, 'browser', {get: () => undefined})")
    browser2.maximize_window()
    browser2.get('https://v2.waitwhile.com/welcome/microcenterstlo')
    time.sleep(7)
    waitlistOpen = False
    browserId = 1
    print("opened browsers")

    #opening master signup browser
    while(True):
        try:
            check = browser1.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')
            if(check.is_enabled()):                     
                check.click()
                time.sleep(4)
                break
            else:
                print("Waitlist not open, can't create master browser")
                time.sleep(1800)
                browser1.refresh()
        except:
            try:
                check = browser1.find_element_by_css_selector('body > app-root > welcome > div > div > section > div.ng-tns-c188-3.fontWhite > div.col-sm-10.custom-btn.d-flex.flex-column.ng-tns-c188-3 > div > button')
                s = check.text()
                if(check.is_enabled()):
                    check.click()
                    time.sleep(4)
                    break
                else:
                    print("Waitlist not open, can't create master browser")
                    time.sleep(1800)
                    browser1.refresh()
            except:
                print("ERROR: Can't find button")
                time.sleep(1800)
                browser1.refresh()
    try:
        box1 = browser1.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
        box1.click()
        time.sleep(2)
    except:
        print("Can't find box1")
    try:
        box2 = browser1.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
        box2.click()
        time.sleep(2)
    except:
        print("Can't find box2")
    try:
        firstnamebox = browser1.find_element_by_css_selector('#name02')
        firstnamebox.send_keys(first)
        lastnamebox = browser1.find_element_by_css_selector('#name03')
        lastnamebox.send_keys(last)
        phonebox = browser1.find_element_by_css_selector('#phone01')
        phonebox.send_keys(phone)
        print("successfully queued signup")
    except:
        print("Error, cant input info")

    print("beginning long sleep")
    time.sleep(64800) #18 hour sleep statement, the program assumes you will start it sometime in the morning while the waitlist is open, and then start checking
                      #for the following mornings signups.
    browser2.refresh()
    time.sleep(5)
    for x in range(5):
        try:
            while(waitlistOpen == False):
                #try except block
                try:
                #identify element
                    check = browser2.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')
                    if(check.is_enabled()):                     
                        waitlistOpen = True
                        break
                    else:
                        print("Waitlist not open, waiting to add " + first + " " + last)
                        waitlistOpen = False
                #NoSuchElementException thrown if not present
                except:
                    try:
                        check = browser2.find_element_by_css_selector('body > app-root > welcome > div > div > section > div.ng-tns-c188-3.fontWhite > div.col-sm-10.custom-btn.d-flex.flex-column.ng-tns-c188-3 > div > button')
                        if(check.is_enabled()):
                            waitlistOpen = True
                            break
                        else:
                            print("Waitlist not open, waiting to add " + first + " " + last)
                            waitlistOpen = False
                    except:
                        print("ERROR: Can't find button")
                        waitlistOpen = False
                        browser2.refresh()
                        time.sleep(5)
                
            if(waitlistOpen == True):
                print("found opening, finishing signup")
                t_end = time.time() + 30
                while(time.time() < t_end):
                    try:
                        submit = browser1.find_element_by_xpath('//*[@id="public-waitlist-confirm"]/div/div[2]/div[2]/form/div[1]/button')
                        submit.click()
                    except:
                        try:
                            done = browser1.find_element_by_xpath('//*[@id="public-waitlist-complete"]/div/div[1]/button')
                            print("signup complete!")
                            time.sleep(5)
                            break
                        except:
                            pass
                browser1.quit()
                browser2.quit()
                break
        except:
            waitlistOpen = False
            browser1.refresh()
            print("Error occurred, refreshing and trying again")
            time.sleep(2.3)
    else:
        print("Couldn't get through in 3 retries, exiting...")

def get_proxy(bot_id):
    lines = []
    try:
        f = open("./proxies.txt", "r")
        lines = f.readlines()
        if(not f.closed):
            f.close()
        if(bot_id >= len(lines)):
            return lines[0]
        new_lines = []
        for line in lines:
            if (line[-1] == "\n"):
                new_lines += [line[:-1]]
        lines = new_lines
        print(lines[bot_id] + "|")
        return lines[bot_id]
    except Exception as exn:
        print("Proxy file not found: " + str(exn))
        return ""


client = discord.Client()

def main():
    if(True):
        @client.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(client))
            print(sys.argv[1], sys.argv[2], sys.argv[3])
            channel = client.get_channel(int(sys.argv[4]))
            try:
                join_waitlist(sys.argv[1], sys.argv[2], sys.argv[3])
                await channel.send('<@' + str(sys.argv[5]) + "> " + str(sys.argv[1]) + " " + str(sys.argv[2]) + " has been added to the waitlist! Check your texts to see what position you are in line.")
            except:
                await channel.send('<@' + str(sys.argv[5]) + ">  An error occured, " + str(sys.argv[1]) + " " + str(sys.argv[2]) + " has not been added to the waitlist! Please try again and make sure you are using the input command correctly")
            sys.exit()
if __name__ == "__main__":
    main()

TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)

    