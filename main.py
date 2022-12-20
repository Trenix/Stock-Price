import requests
import bs4

def repeat():

    print('Please provide the abbreviated stock you want to check.')

    # Take abbreviated stock
    stock = input()

    # Ensures stock is not a number or special character
    if not stock.isalpha():
        print("Only letters are allowed.")
        print("-------------------------")

    else:
        # Generating the url
        url = "https://www.google.com/search?q=NASDAQ:" + stock

        # Sending HTTP request
        request_result = requests.get(url)

        # Pulling HTTP data from internet
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        tag = soup.find_all('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})

        # Attempting to clean data to provide result
        try:
            Stock_Cost = str(tag).split('AP7Wnd">')[-2].split(' ')[0]
            print('$' + Stock_Cost)
        except IndexError:
            print("Something went wrong, please try another stock.")
            print("-------------------------")

while True:
    repeat()