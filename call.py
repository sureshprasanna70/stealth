import socket
import requests
import re
import json
from collections import Counter
import pygal
def main():
    filename="domains"
    contents=fileread(filename)
    sites = re.findall(r"^g.*",contents,re.MULTILINE)
    ips=findips(sites)
    geoloc=findgeoloc(ips)
    split = [tuple(l) for l in geoloc]
    counts = {}
    s=""
    multipie_chart = pygal.Pie()
    multipie_chart.title = 'Demographic distribution of IPS '
    for t in split:
        counts[t] = 1 + counts.get(t, 0)
    for t,n in counts.items():

        s=""
        for i in t:
            s+=i
        multipie_chart.add(s,n)
    multipie_chart.render_to_png(filename='bar_chart.png')
    html=multipie_chart.render();
    f=open('graph.html','w')
    f.write(html)
    f.close()
def fileread(filename):
    try:
        fileob=open(filename)
        content=fileob.read()
        fileob.close()
        return content
    except Exception,e:
        print str(e)

def findips(sites):
    ips=[[] for i in range(len(sites))]
    for i in range(len(sites)):
        try:
            print str(i)+" "+sites[i]
            ips[i]=socket.gethostbyname(sites[i])
        except Exception,e:
            ips[i]='nil'
    print ips
    return ips 
def findgeoloc(ips):
    countrycode=[[] for i in range(len(ips))]
    for i in range(len(ips)):
        try:
           url="http://telize.com/geoip/"
           if ips[i] != "nil":
              response=requests.get(url+ips[i])
              stringjson=unicode(response.text)
              responsejson=json.loads(stringjson)
              countrycode[i]=responsejson['country_code']
              logstring=str(i)+" "+ips[i]+" "+responsejson["country_code"]
              print logstring
           else:
             print 'nil ip'
        except Exception,e:
            print "exception"
            print str(e)
    return countrycode
main()
