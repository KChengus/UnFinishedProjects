from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import Client
from time import sleep

url = "https://marknad.sgs.se/pgSearchResult.aspx#seekAreaMode=simple&type=standard&search=y&page=1&syndicateNo=1&objectMainGroupNo=1&rent=0;25000&area=0;150&advertisement=-1&marketPlaces=100,103,102"

# Load up Chrome and pull up the website
browser = webdriver.Chrome(executable_path="C:\\Users\\kevin\\OneDrive\\Dokument\\quickAccess\\chromedriver")
browser.get(url)
sleep(2)

# <--------------------------------Settings-------------------------------->

# Your Account SID
account_sid = "ACf6fc51ba23fd487225896dc38b49e662"
# Your Auth Token
auth_token  = "741958edd4a20c5dbbce5ea94287f4c5"

# <--------------------------------Functions-------------------------------->

def send(mes):
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_='whatsapp:+14155238886', body='{}'.format(mes), to='whatsapp:+46763107889')
    print(message.sid)

def search():
    browser.refresh()
    print("search")
    for _ in range(20):
        sleep(1)
        
    table = browser.find_elements(By.TAG_NAME, 'table')
    if len(table) <= 0: return
    appartments = table[0].find_elements(By.TAG_NAME, 'tr')
    for appartment in appartments:
        txt = appartment.text
        if txt not in unique_address:
            unique_address.append(txt)
            print(txt)
            send(txt)
        
unique_address = list()

while True:
    search()