import socket
import requests
import re
def main():
    filename="gdomains"
    contents=fileread(filename)
    regex = re.findall("^g.*",contents,re.MULTILINE)
    print (regex)
def fileread(filename):
    try:
        fileob=open(filename)
        content=fileob.read()
        fileob.close()
        return content
    except Exception,e:
        print str(e)
main()
