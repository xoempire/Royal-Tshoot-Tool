import sys
import os
domain=input('Please enter the domain/Ip Address: ')
print('working on {domain}')
job=list(str(input("what do you want to do? ")))
def jping():
    ping=os.system("ping -c 4 " + domain)
    return ping
def jtraceroute():
    traceroute=os.system("traceroute " + domain)
    return traceroute
def jdig():
    dig=os.system("dig " + domain)
    return dig
def jwhois():
    whois=os.system("whois " + domain)
    return whois
def jnslookup():
    nslookup=os.system('nslookup ' + domain)
    return nslookup
def jttfb():
    import time
    from urllib import request
    opener = request.build_opener()
    request = request.Request(domain)
    request.add_header('user-agent', 'firefox')
    start = time.time()
    resp = opener.open(request)
    resp.read(1)
    ttfb = time.time() - start
    print("The TTFirst Byte of " +domain+" is: "+str(ttfb))
for i in job:
    if i=='0':
        jping()
    elif i=='1':
        jtraceroute()
    elif i=='2':
        jdig()
    elif i=='3':
        jwhois()
    elif i=='4':
        jnslookup()
    elif i=='5':
        domain='https://'+domain
        jttfb()
    else:
        print('fuck off')
        break 




