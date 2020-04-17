from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def bataoMujhe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "G://saurav//CoronaProject//virus.ico",
        timeout = 80
    )


def getData(url):
    gd = requests.get(url)
    return gd.text


if __name__ == "__main__":
    while True:
        myHtmlData = getData("https://www.mohfw.gov.in/")

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()

        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
        'Chhattisgarh', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
        'Karnataka', 'Kerala', 'Ladakh', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland#',
        'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telengana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh',
        'West Bengal']

        for item in itemList[0:34]:
            dataList = item.split('\n')

            if dataList[1] in states:
                nTitle = 'Cases of CoVid-19'
                nText = f"State : {dataList[1]}\nConfirmed Cases : {dataList[2]}\nCured : {dataList[3]}\nDeath : {dataList[4]}"
                bataoMujhe(nTitle, nText)
                time.sleep(3)
        time.sleep(3600)
