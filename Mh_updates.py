from datetime import date, datetime
import time
import telegram
import telepot
import requests
import json
import telegram
from bs4 import BeautifulSoup as bs
from telepot.loop import MessageLoop
import threading
import urllib3



print(date.today())
now = datetime.now()
print(now.strftime("%H:%M:%S"))
#old_news="old"
#print(old_news)

def GetNews2():
    response2 = requests.get("https://www.tv9marathi.com/coronavirus")
    soup2 = bs(response2.text, "html.parser")
    latest_news2 = soup2.find("div", class_="elementor-post__text")
    #op2 = (latest_news2.a.text)
    l = []
    for link in soup2.findAll('a'):
        o = (link.get('href'))
        l.append(o)
    # g = l.index(
    #   "https://www.tv9marathi.com/headlines/pwd-do-sasoon-hospital-work-in-world-record-time-says-ashok-chavan-206357.html")
    g = (l[68])
    return  str(g)

def GetNews():
    response = requests.get("https://www.indiatoday.in/coronavirus")
    soup = bs(response.text, "html.parser")
    # print(soup.prettify())
    latest_news = soup.find('div', class_='pollution-right')
    tx=latest_news.a.text.strip()
    x=[]
    for lin in soup.findAll('a'):
        y=(lin.get('href'))
        x.append(y)
    op = x[44]

    return   "https://www.indiatoday.in" +  str(op)

def GetCity():
    response = requests.get("https://api.covid19india.org/state_district_wise.json")
    r = response.json()
    res=''
    for i, j in r.items():
        #print(i,j)
        for k, l in j.items():
            if i == "Maharashtra":
                #print(k,l)
                for m, n in l.items():
                    # print(m,n)
                    # Dist.add(m)
                    for o, p in n.items():
                        if o == "confirmed":
                            res=res+ str(m)+'-'+str(p)+"\n"
    return "महाराष्ट्रातील  जिल्हानिहाय कोरोना ग्रस्त रुग्णांचा आकडा : " + "\n\n"  + res + "\n" + "*Other States=Patients belongs to OTHER THAN MAHARSHTRA*" + "\n" + "\n" + "*Unknown=DISTRICTS UNKNOWN*"

def GetState():
    response=requests.get("https://api.covid19india.org/data.json")
    data=response.json()
    #print(data)
    Active_All = 0
    Confirmed_all = 0
    statedata = data.get("statewise")
    for cov_data in statedata:
            #print(cov_data.get("state"),cov_data.get("active"),cov_data.get("confirmed")," deaths " ,cov_data.get("deaths"),cov_data.get("recovered"))
            if(cov_data.get("state") == 'Total'):
                return "India Covid-19 Tracker" +"\n" + "Confirmed :" + cov_data.get("confirmed") + "\n" + "Active :"  + cov_data.get("active") +"\n" + "Deaths :" +cov_data.get("deaths") + "\n" +"Recovered :" + cov_data.get("recovered")

#while True:

def sendmsg(msg):

    bot = telegram.Bot(token="")
    status = bot.send_message(chat_id="", text=msg,  parse_mode=telegram.ParseMode.HTML)

old_news="l"
on="k"
od="d"
old_data="D"
while True:
    try:
        new_news = GetNews2()
        if new_news != old_news:
            sendmsg(new_news)
            old_news = new_news
            print(new_news)
    except:
        print("error in tv 9")
        print(now.strftime("%H:%M:%S"))
    time.sleep(30)
    try:
        nn = GetNews()
        if nn != on:
            sendmsg(nn)
            on = nn
            print(nn)
    except:
        print("Error in india today")
        print(now.strftime("%H:%M:%S"))
    time.sleep(30)
    try:
        nd = GetCity()
        if nd != od:
            sendmsg(nd)
            od = nd
            print(nd)
    except:
        print("error in dist data")
        print(now.strftime("%H:%M:%S"))
    time.sleep(30)
    try:
        new_data = GetState()
        if new_data != old_data:
            sendmsg(new_data)
            old_data = new_data
            print(new_data)
    except:
        print("error in india data")
        print(now.strftime("%H:%M:%S"))
    time.sleep(30)












