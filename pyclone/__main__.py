from colorama import Fore, Back, Style
import sys
import argparse
import datetime
from dateutil import relativedelta
from pyfiglet import Figlet
from selenium import webdriver
import time
import sys
import os


def main():
    f = Figlet(font='stop')
    print( f.renderText('pyclone'))
    parser = argparse.ArgumentParser(description='Automate daily stuff')
    parser.add_argument(
        'action', choices=['daysincompany', 'paper'], help='get duration in company')
    parser.add_argument("value",
                        help="value of 2nd argument")

    args = parser.parse_args()
    if args.action == "daysincc":
        days_in_company()
    elif args.action == "paper":
        read_paper(args.value)
    else:
        print('Not supported')


def read_paper(ptype=''):
    if(ptype == 'bul'):
        url = 'https://www.readwhere.com/newspaper/deshonnati/Buldhana-Live/560?refquery=buldhana%20live'
    elif(ptype == 'ak'):
        url = 'https://www.readwhere.com/newspaper/deshonnati/Akola-Main/557?refquery=deshonnati%20akola'
    elif(ptype == 'lk'):
        url = 'https://www.readwhere.com/newspaper/loksatta/loksatta-pune/643'
    else:
        print('Paper not found')
        sys.exit()
    # Replace executable_path with your gecodriver path
    browser = webdriver.Firefox(
        executable_path=r'G:\\Coding_Ground\\git\\geckodriver')
    browser.get(url)
    browser.maximize_window()
    time.sleep(0.1)
    read_btn = browser.find_element_by_xpath(
        "/html/body/div[4]/div/div/div[3]/div/div[2]/div[1]/div[3]/a")
    read_btn.click()
    time.sleep(0.1)
    skip_btn = browser.find_element_by_xpath('//*[@id="skip-area-id"]')
    skip_btn.click()
    time.sleep(0.1)
    zoom_btn = browser.find_element_by_xpath(
        '/html/body/div[7]/div[1]/div[1]/div[4]/div/button[1]')
    zoom_btn.click()


def days_in_company():
    today = datetime.date.today()
    # Replace date with your joining date
    joining_day = datetime.date(2018, 12, 12)
    diff = relativedelta.relativedelta(today, joining_day)
    years = diff.years
    months = diff.months
    days = diff.days

    print(Fore.GREEN + 'You are in ABC org since {} years {} months {} days'.format(
        years, months, days) + Style.RESET_ALL)


if __name__ == '__main__':
    main()