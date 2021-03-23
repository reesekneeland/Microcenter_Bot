import time
import random
import os
import discord
import sys
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display 

load_dotenv()
#display = Display(visible=0, size=(800, 600))         #uncomment if running on a displayless server
#display.start() 

def join_waitlist(f, l, p):
    # print("process started, waiting until morning")
    # time.sleep(23500)
    first = f
    last = l
    phone = p
    chrome_options = Options()
    #chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('proxy-server=' + get_proxy(0))
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36")
    chrome_options.add_argument("--disable-gpu")
    browser1 = webdriver.Chrome("./chromedriver_test", options=chrome_options)
    browser1.maximize_window()
    browser1.get('https://v2.waitwhile.com/welcome/microcenterstlo')
    chrome_options.add_argument('proxy-server=' + get_proxy(1))
    browser2 = webdriver.Chrome("chromedriver", options=chrome_options)
    browser2.maximize_window()
    browser2.get('https://v2.waitwhile.com/welcome/microcenterstlo')
    chrome_options.add_argument('proxy-server=' + get_proxy(2))
    browser3 = webdriver.Chrome("chromedriver", options=chrome_options)
    browser3.maximize_window()
    browser3.get('https://v2.waitwhile.com/welcome/microcenterstlo')
    chrome_options.add_argument('proxy-server=' + get_proxy(0))
    browser4 = webdriver.Chrome("chromedriver", options=chrome_options)
    browser4.maximize_window()
    browser4.get('https://v2.waitwhile.com/welcome/microcenterstlo')
    chrome_options.add_argument('proxy-server=' + get_proxy(1))
    browser5 = webdriver.Chrome("chromedriver", options=chrome_options)
    browser5.maximize_window()
    browser5.get('https://v2.waitwhile.com/welcome/microcenterstlo')
    time.sleep(5)
    waitlistOpen = False
    browserId = 1
    print("opened browsers")

    while(waitlistOpen == False):
        #try except block
        try:
        #identify element
            check = browser1.find_element_by_css_selector('body > app-root > welcome > div > div > section > div.ng-tns-c149-1.fontWhite > div.col-sm-10.custom-btn.d-flex.flex-column.ng-tns-c149-1 > div > button')
            s = check.text
            if(check.is_enabled()):
                check.click()
                time.sleep(1)
                waitlistOpen = True
                break
            else:
                print("Waitlist not open, waiting to add " + first + " " + last)
                waitlistOpen = False
                browser1.refresh()
                time.sleep(0.5)
        #NoSuchElementException thrown if not present
        except:
            print("Waitlist not open, waiting to add " + first + " " + last)
            waitlistOpen = False
            browser1.refresh()
            time.sleep(0.5)
        try:
        #identify element
            check = browser2.find_element_by_css_selector('body > app-root > welcome > div > div > section > div.ng-tns-c149-1.fontWhite > div.col-sm-10.custom-btn.d-flex.flex-column.ng-tns-c149-1 > div > button')
            s = check.text
            if(check.is_enabled()):
                check.click()
                browserId = 2
                time.sleep(1)
                waitlistOpen = True
                break
            else:
                print("Waitlist not open, waiting to add " + first + " " + last)
                waitlistOpen = False
                browser2.refresh()
                time.sleep(0.5)
        #NoSuchElementException thrown if not present
        except:
            print("Waitlist not open, waiting to add " + first + " " + last)
            waitlistOpen = False
            browser2.refresh()
            time.sleep(0.5)
        try:
        #identify element
            check = browser3.find_element_by_css_selector('body > app-root > welcome > div > div > section > div.ng-tns-c149-1.fontWhite > div.col-sm-10.custom-btn.d-flex.flex-column.ng-tns-c149-1 > div > button')
            s = check.text
            if(check.is_enabled()):
                check.click()
                browserId = 3
                time.sleep(1)
                waitlistOpen = True
                break
            else:
                print("Waitlist not open, waiting to add " + first + " " + last)
                waitlistOpen = False
                browser3.refresh()
                time.sleep(0.5)
        #NoSuchElementException thrown if not present
        except:
            print("Waitlist not open, waiting to add " + first + " " + last)
            waitlistOpen = False
            browser3.refresh()
            time.sleep(0.5)
        try:
        #identify element
            check = browser4.find_element_by_css_selector('body > app-root > welcome > div > div > section > div.ng-tns-c149-1.fontWhite > div.col-sm-10.custom-btn.d-flex.flex-column.ng-tns-c149-1 > div > button')
            s = check.text
            if(check.is_enabled()):
                check.click()
                time.sleep(1)
                browserId = 4
                waitlistOpen = True
                break
            else:
                print("Waitlist not open, waiting to add " + first + " " + last)
                waitlistOpen = False
                browser4.refresh()
                time.sleep(0.5)
        #NoSuchElementException thrown if not present
        except:
            print("Waitlist not open, waiting to add " + first + " " + last)
            waitlistOpen = False
            browser4.refresh()
            time.sleep(0.5)
        try:
        #identify element
            check = browser5.find_element_by_css_selector('body > app-root > welcome > div > div > section > div.ng-tns-c149-1.fontWhite > div.col-sm-10.custom-btn.d-flex.flex-column.ng-tns-c149-1 > div > button')
            s = check.text
            if(check.is_enabled()):
                check.click()
                time.sleep(1)
                browserId = 5
                waitlistOpen = True
                break
            else:
                print("Waitlist not open, waiting to add " + first + " " + last)
                waitlistOpen = False
                browser5.refresh()
                time.sleep(0.5)
        #NoSuchElementException thrown if not present
        except:
            print("Waitlist not open, waiting to add " + first + " " + last)
            waitlistOpen = False
            browser5.refresh()
            time.sleep(0.5)
    if(waitlistOpen == True):
        print("found opening, starting signup")
        print(browserId)
        time.sleep(2)
        if(browserId == 1):
            try:
                box1 = browser1.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                box1.click()
                time.sleep(0.2)
            except:
                time.sleep(3)
                try:
                    box1 = browser1.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    box1.click()
                    time.sleep(0.2)
                except:
                    time.sleep(3)
                    box1 = browser1.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    box1.click()
                    time.sleep(0.2)
            try:
                box2 = browser1.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            except:
                time.sleep(1)
                box2 = browser1.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            try:
                firstnamebox = browser1.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser1.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser1.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
            except:
                time.sleep(1)
                firstnamebox = browser1.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser1.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser1.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
        elif(browserId == 2):
            try:
                box1 = browser2.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                box1.click()
                time.sleep(0.2)
            except:
                time.sleep(3)
                try:
                    box1 = browser2.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    box1.click()
                    time.sleep(0.2)
                except:
                    time.sleep(3)
                    box1 = browser2.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    box1.click()
                    time.sleep(0.2)
            try:
                box2 = browser2.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            except:
                time.sleep(1)
                box2 = browser2.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            try:
                firstnamebox = browser2.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser2.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser2.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
            except:
                time.sleep(1)
                firstnamebox = browser2.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser2.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser2.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
        elif(browserId == 3):
            print("found the right browser")
            try:
                box1 = browser3.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                box1.click()
                time.sleep(0.2)
                print("check 1 succeded")
            except:
                print("check 1 failed, trying again")
                time.sleep(3)
                try:
                    box1 = browser3.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    box1.click()
                    time.sleep(0.2)
                    print("check 2 succeded")
                except:
                    print("check 2 failed, trying again")
                    time.sleep(3)
                    box1 = browser3.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    print("check 3 succeded")
                    box1.click()
                    time.sleep(0.2)
            try:
                box2 = browser3.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            except:
                time.sleep(1)
                box2 = browser3.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            try:
                firstnamebox = browser3.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser3.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser3.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
            except:
                time.sleep(1)
                firstnamebox = browser3.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser3.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser3.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
        elif(browserId == 4):
            print("found the right browser")
            try:
                box1 = browser4.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                box1.click()
                time.sleep(0.2)
                print("check 1 succeded")
            except:
                print("check 1 failed, trying again")
                time.sleep(3)
                try:
                    box1 = browser4.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    box1.click()
                    time.sleep(0.2)
                    print("check 2 succeded")
                except:
                    print("check 2 failed, trying again")
                    time.sleep(3)
                    box1 = browser4.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    print("check 3 succeded")
                    box1.click()
                    time.sleep(0.2)
            try:
                box2 = browser4.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            except:
                time.sleep(1)
                box2 = browser4.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            try:
                firstnamebox = browser4.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser4.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser4.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
            except:
                time.sleep(1)
                firstnamebox = browser4.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser4.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser4.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
        else:
            try:
                box1 = browser5.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                box1.click()
                time.sleep(0.2)
            except:
                time.sleep(3)
                try:
                    box1 = browser5.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    box1.click()
                    time.sleep(0.2)
                except:
                    time.sleep(3)
                    box1 = browser5.find_element_by_css_selector('#public-waitlist-service > div > div.d-flex.justify-content-end > section > div:nth-child(2) > div > button:nth-child(1)')
                    box1.click()
                    time.sleep(0.2)
            try:
                box2 = browser5.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            except:
                time.sleep(1)
                box2 = browser5.find_element_by_css_selector('#public-waitlist-party-size > section > div.row.justify-content-center.setww_001.setww-title > div.w-100 > button')
                box2.click()
                time.sleep(0.2)
            try:
                firstnamebox = browser5.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser5.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser5.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
            except:
                time.sleep(1)
                firstnamebox = browser5.find_element_by_css_selector('#name02')
                firstnamebox.send_keys(first)
                lastnamebox = browser5.find_element_by_css_selector('#name03')
                lastnamebox.send_keys(last)
                phonebox = browser5.find_element_by_css_selector('#phone01')
                phonebox.send_keys(phone)
                phonebox.send_keys(Keys.ENTER)
        
        time.sleep(20)
        browser1.quit()
        browser2.quit()
        browser3.quit()
        browser4.quit()
        browser5.quit()
        print("Waitlist open! " + first + " " + last + " has been added!")


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

TOKEN = TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)

    