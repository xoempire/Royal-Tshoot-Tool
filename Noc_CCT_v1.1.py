import sys
import os
import requests
import time
import random
from flask import Flask

app = Flask(__name__)


@app.route('/lunch')
def index():
    data = jturn()
    return f"<p>{data[0]}</p><p>{data[1]}</p><p>{data[2]}</p>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Red = "\033[31m"


def jtshoot():
    domain = input(f'{bcolors.BOLD}{bcolors.FAIL}Please enter the domain Address: {bcolors.ENDC}{bcolors.ENDC}')
    ssly = input(
        f'{bcolors.OKBLUE}Press{bcolors.ENDC} {bcolors.WARNING}"s"{bcolors.ENDC}{bcolors.OKBLUE} for Https and {bcolors.ENDC}{bcolors.WARNING}"p"{bcolors.ENDC}{bcolors.OKBLUE}for Http{bcolors.ENDC}')
    if ssly == 's':
        httpy = 'https://' + domain
    elif ssly == 'p':
        httpy = 'http://' + domain
    else:
        domain = domain
    print(f"{bcolors.WARNING}working on{bcolors.ENDC} {bcolors.OKGREEN}{domain}{bcolors.ENDC}")
    print(
        f"{bcolors.HEADER}Press '0' for Ping\nPress '1' for Traceroute\nPress '2' for Dig\nPress '3' for Whois\nPress "
        f"'4' for Nslookup\nPress '5' for TTFB\nPress '6' for Response Headers\n\nWhat do you want to do? "
        f"{bcolors.ENDC}")
    job = list(str(input(" ")))

    def jping():
        ping = os.system("ping -c 4 " + domain)
        return ping

    def jtraceroute():
        traceroute = os.system("traceroute " + domain)
        return traceroute

    def jheader():
        d = dict(requests.get(httpy).headers)
        for x, o in d.items():
            if x.startswith('AR'):
                print(f"{bcolors.OKCYAN}{x, o}{bcolors.ENDC}")

    def jdivider(thejob):
        title = 'This part is for ' + thejob
        line = '======================================================================='
        return print(f"{bcolors.WARNING}{title}\n{line}{line}\n{line}{line}{bcolors.ENDC}")

    def jdig():
        dig = os.system("dig " + httpy)
        return dig

    def jwhois():
        whois = os.system("whois " + domain)
        return whois

    def jnslookup():
        nslookup = os.system('nslookup ' + httpy)
        return nslookup

    # def jbrowser():
    #     driver = webdriver.Firefox()
    #     driver.implicitly_wait(0)
    #     driver.get(f"{httpy}")
    def jttfb():
        from urllib import request
        opener = request.build_opener()
        request = request.Request(httpy)
        request.add_header('user-agent', 'firefox')
        start = time.time()
        resp = opener.open(request)
        resp.read(1)
        ttfb = time.time() - start
        print("Time To First Byte of " + httpy + " is: " + str(ttfb))

    for i in job:
        if i == '0':
            thejob = 'Ping'
            jdivider(thejob)
            jping()
        elif i == '1':
            thejob = 'Traceroute'
            jdivider(thejob)
            jtraceroute()
        elif i == '2':
            thejob = 'Dig'
            jdivider(thejob)
            jdig()
        elif i == '3':
            thejob = 'Whois'
            jdivider(thejob)
            jwhois()
        elif i == '4':
            thejob = 'Nslookup'
            jdivider(thejob)
            jnslookup()
        elif i == '5':
            thejob = 'TTFB'
            jdivider(thejob)
            jttfb()
        elif i == '6':
            thejob = 'Response Header'
            jdivider(thejob)
            jheader()
        else:
            print('fuck off')
            break


def jturn():
    Callcenter = ['Ali', 'Masomeh', 'Reza']
    rand_item = random.sample(Callcenter, 3)
    order_list = []
    for item in rand_item:
        order_list.append(item)
    return order_list


def firstfunc():
    mainfunc = input(
        f'{bcolors.OKBLUE}"Press"{bcolors.ENDC}{bcolors.WARNING}"1"{bcolors.ENDC}{bcolors.OKBLUE}For Using the Tshoot tool{bcolors.ENDC}\n{bcolors.OKBLUE}Press{bcolors.ENDC}{bcolors.WARNING}"2"{bcolors.OKBLUE}To See whose turn is it{bcolors.ENDC}\n\n{bcolors.OKCYAN}What do you wnant to do?{bcolors.ENDC}')
    if mainfunc == '1':
        jtshoot()
    elif mainfunc == '2':
        jturn()
    else:
        print(f'\n{bcolors.Red}You choose poorly! Try again{bcolors.ENDC}\n')


# firstfunc()

if __name__ == '__main__':
    app.run(debug=True)
