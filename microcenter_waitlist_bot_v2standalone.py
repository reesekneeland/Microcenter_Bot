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
display = Display(visible=0, size=(800, 600))         #uncomment if running on a displayless server
display.start() 

def join_waitlist(f, l, p):
    first = f
    last = l
    phone = p
    # chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument('proxy-server=' + get_proxy(0))
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36")
    # chrome_options.add_argument("--disable-gpu")
    # print("added arguments")
    # browser = webdriver.Chrome("./chromedriver_test", options=chrome_options)
    # options = Options()
    # options.add_argument('marionette')
    # # print("added arguments")
    browser = webdriver.Firefox(executable_path="./geckodriver")
    browser.execute_script("Object.defineProperty(navigator, 'browser', {get: () => undefined})")
    browser.maximize_window()
    print("opened browser")
    browser.get('https://v2.waitwhile.com/welcome/microcenterstlo')
    time.sleep(5)
    waitlistOpen = False
    browserId = 1
    print("opened browsers")

    for x in range(5):
        try:
            while(waitlistOpen == False):
                #try except block
                try:
                #identify element
                    try:
                        box1 = browser.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                        box1.click()
                        waitlistOpen = True
                        break
                    except:
                        pass
                    check = browser.find_element_by_css_selector('body > app-root > welcome > div > div > section > div.ng-tns-c149-1.fontWhite > div.col-sm-10.custom-btn.d-flex.flex-column.ng-tns-c149-1 > div > button')
                    if(check.is_enabled()):                     
                        check.click()
                        continue
                    else:
                        print("Waitlist not open, waiting to add " + first + " " + last)
                        waitlistOpen = False
                #NoSuchElementException thrown if not present
                except:
                    try:
                        check = browser.find_element_by_xpath('/html/body/app-root/welcome/div/div/section/div[2]/div[3]/div/button')
                        if(check.is_enabled()):
                            check.click()
                            continue
                        else:
                            print("Waitlist not open, waiting to add " + first + " " + last)
                            waitlistOpen = False
                    except:
                        print("Can't find button")
                        waitlistOpen = False
                        continue
                
            if(waitlistOpen == True):
                print("found opening, starting signup")
                t_end = time.time() + 2
                while(time.time() < t_end):
                    try:
                        box2 = browser.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                        box2.click()
                        break
                    except:
                        pass
                t_end = time.time() + 2
                while(time.time() < t_end):
                    try:
                        firstnamebox = browser.find_element_by_css_selector('#name02')
                        firstnamebox.send_keys(first)
                        break
                    except:
                        pass
                lastnamebox = browser.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                t_end = time.time() + 30
                while(time.time() < t_end):
                    try:
                        submit = browser.find_element_by_xpath('//*[@id="public-waitlist-confirm"]/div/div[2]/div[2]/form/div[1]/button')
                        submit.click()
                    except:
                        try:
                            done = browser.find_element_by_xpath('//*[@id="public-waitlist-complete"]/div/div[1]/button')
                            print("signup complete!")
                            time.sleep(5)
                            break
                        except:
                            pass
                
                browser.quit()
                print("Waitlist open! " + first + " " + last + " has been added!")
                break
        except:
            waitlistOpen = False
            browser.refresh()
            print("Error occurred, refreshing and trying again")
            time.sleep(2.3)
    else:
        print("Couldn't get through in 5 retries, exiting...")

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

    