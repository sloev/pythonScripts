# -*- coding: utf-8 -*-
import mechanize
from bs4 import BeautifulSoup
	

browser=mechanize.Browser()
browser.set_handle_refresh(False) 
browser.set_handle_robots( False )
browser.addheaders = [('User-agent', 'Firefox')]

entries={}


letters=[u'a'.encode("utf-8"),u'b'.encode("utf-8"),
u'c'.encode("utf-8"),
u'd'.encode("utf-8"),
u'e'.encode("utf-8"),
u'f'.encode("utf-8"),
u'g'.encode("utf-8"),
u'h'.encode("utf-8"),
u'i'.encode("utf-8"),
u'j'.encode("utf-8"),
u'k'.encode("utf-8"),
u'l'.encode("utf-8"),
u'o'.encode("utf-8"),
u'm'.encode("utf-8"),
u'n'.encode("utf-8"),
u'o'.encode("utf-8"),
u'p'.encode("utf-8"),
u'q'.encode("utf-8"),
u'r'.encode("utf-8"),
u's'.encode("utf-8"),
u't'.encode("utf-8"),
u'u'.encode("utf-8"),
u'v'.encode("utf-8"),
u'x'.encode("utf-8"),
u'y'.encode("utf-8"),
u'z'.encode("utf-8"),
u'æ'.encode("utf-8"),
u'ø'.encode("utf-8"),
u"å".encode("utf-8")]

letterIndex=0;
currentLetter=letters[letterIndex]

def initLetter():
	browser.select_form(name='retskrivform')
	currentLetter=letters[letterIndex]
	entries[currentLetter]=[]
	
	browser['retskriv']=currentLetter
	browser.submit()
	

browser.open('http://www.dsn.dk/ro/ro.htm')
initLetter()

#count=0
with open("retskrivningsordbog.txt", 'w') as myfile:
    while(True):
        try :
            soup = BeautifulSoup(browser.response().read())
            numbers=soup.find('div',{'id':'buttons'}).find_all('div')
            for div in numbers:
                if not div.has_attr('align'):
                    print "%s: %s" %(currentLetter,div.text.strip())
            articles=soup.find('div',{'id':'articles'}).find_all('div')
            ent=[]
            for div in articles:
                tmp=div.find_all('b')
                tmp=tmp[0].text.strip('-')
                
                myfile.write("%s\n" % tmp.encode("utf-8")) # python will convert \n to os.linesep
                ent.append(tmp)
            entries[currentLetter]=entries[currentLetter]+ent
            
            browser.select_form(name='retskrivpaginering')
            browser.submit(name='switchpage', label='>')
   
        except Exception,err:
            print Exception,err
            letterIndex+=1
            if not letterIndex>len(letters)-1:
	            initLetter()
    	    else:
	            break
    myfile.close()