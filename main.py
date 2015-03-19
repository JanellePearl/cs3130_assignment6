#cs3130 Assignment 6
#Janelle Montgomery

#The purpose of this assignment is to use requests to get html information from a website. We will then scrape
#certain information from the website. I have chosen to use BeautifulSoup4 to scrap the information from
#the website. The website at hand is : www.theglobeandmail.com/globe-investor.

def display_menu():
    print("--")
    print("Market information\n")
    print("Select one of the following:\n")
    print("1) S&P TSX")
    print("2) S&P 500")
    print("3) Dow Jones")
    print("4) Nasdag")
    print("5) CAD/USD")
    print("6) Gold")
    print("7) WTI Crude")
    print("8) Quit\n")
    print("Option?\n")
    print("--\n")
    
    #checks to see if option was a number in the appropriate range
    done = False
    while done == False:
        try:
            selection = int(input())
            print("\n")
            done = True
            
        except ValueError:
            print("You must input a number.")
            return -1
            
        except Exception:
            print("Please enter a valid number.")
            return -1

        if not selection in range(1,9):
            print("Your choice must be in the range of 1 to 8")

    return selection
