#cs3130 Assignment 6
#Janelle Montgomery

#The purpose of this assignment is to use requests to get html information from a website. We will then scrap
#certain information from the website. I have chosen to use BeautifulSoup4 to scrape the information from
#the website. The website at hand is : www.theglobeandmail.com/globe-investor.

import requests
import main
from bs4 import BeautifulSoup


r = requests.get('http://www.theglobeandmail.com/globe-investor/')
data = r.text #html code form the website
soup = BeautifulSoup(data) #make the soup!

#checks the selection made from the main.py screen
def begin():
    while True:
        selection = main.display_menu()
        if selection == 1:
            sptsx()
        elif selection == 2:
            five()
        elif selection == 3:
            dowjones()
        elif selection == 4:
            nasdag()
        elif selection == 5:
            cadusd()
        elif selection == 6:
            gold()
        elif selection == 7:
            wti()
        elif selection == 8:
            leave()
        else:
            print('Your choice is not valid, Try again :)')

#prints the s&p tsx from above website
def sptsx():
    
    t = soup.find("div", {"data-id":"593253"})
    print("S&P TSX " + t.div.text,t.span.text,t.span.next_element.next_element.next_element.next_element
          +" last updated "+t.span.next_element.next_element.next_element.next_element.next_element.next_element)
    print("\n")

#prints the s&p 500 from above website   
def five():
    
    f = soup.find("div",{"data-id":"575769"})
    print("S&P 500 " + f.div.text,f.span.text,f.span.next_element.next_element.next_element.next_element
          +" last updated "+f.span.next_element.next_element.next_element.next_element.next_element.next_element)
    print("\n")

#prints the dow jones from above website    
def dowjones():
    
    d = soup.find("div",{"data-id":"599362"})
    print("Dow Jones " + d.div.text,d.span.text,d.span.next_element.next_element.next_element.next_element
          +" last updated "+d.span.next_element.next_element.next_element.next_element.next_element.next_element)
    print("\n")

#prints the nasdag from above website
def nasdag():
    
    n = soup.find("div",{"data-id":"579435"})
    print("Nasdag "+n.div.text,n.span.text,n.span.next_element.next_element.next_element.next_element
          +" last updated "+n.span.next_element.next_element.next_element.next_element.next_element.next_element)
    print("\n")

#prints the cadusd from above website
def cadusd():
    
    c = soup.find("div",{"data-id":"Currencies"})
    print("CAD/USD "+c.span.text,c.span.next_element.next_element.next_element.next_element.next_element.next_element,
          c.span.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element+" last updated "+
          c.span.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element)
    print("\n")

#prints the gold from above website   
def gold():
    
    g = soup.find("div",{"data-id":"Commodities"})
    print("Gold "+g.span.text,g.span.next_element.next_element,g.span.next_element.next_element.next_element.next_element.next_element,
          g.span.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element+ " last updated "+
          g.span.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element)
    print("\n")

#prints the wti crude from above website   
def wti():
    
    g = soup.find('div',{"data-id":"Commodities"})
    print(g.span.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.
          next_element.next_element.next_element.next_element.next_element.next_element.next_element,g.span.next_element.next_element.
          next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.
          next_element.next_element.next_element.next_element.next_element,g.span.next_element.next_element.next_element.next_element.next_element.
          next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.
          next_element.next_element.next_element.next_element,g.span.next_element.next_element.next_element.next_element.next_element.next_element.
          next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.
          next_element.next_element.next_element.next_element.next_element.next_element.next_element+" last updated "+g.span.next_element.next_element.
          next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.
          next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element)
    print("\n")
    
def leave():
    print("Goodbye :)")
    exit(0)
    

if __name__ == '__main__':
    begin()
