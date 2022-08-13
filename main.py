import requests
import json
import time

print("Welcome to Gaft v1.0.0. Developed by Koky and Sully")

myName = input("What is your name? ")
myEmail = input("What is your email? ")
myMessage = input("What is your message? ")
myPhone = input("What is your phone number? ")
rentalprice = int(input("How much are you looking to pay? "))

allAdds = []

def sendEmail(ListingID):
    headers = {
    'Host': 'gateway.daft.ie',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'platform': 'iOS',
    'Accept': 'application/json',
    'brand': 'daft',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Daft.ie/0 CFNetwork/1335.0.3 Darwin/21.6.0'
    }

    url = "https://gateway.daft.ie/old/v1/reply"
    # data = '{"name":"name","tcAccepted":true,"email":"he1llo@gmail.com,"message":"agagag","adId":4001666,"phone":"085811463112"}'
    data = '{"name":"' + str(myName) + '","tcAccepted":true,"email":"' + str(myEmail) + '","message":"' + str(myMessage) + '","adId":' + str(ListingID) + ',"phone":"' + str(myPhone) + '"}'

    # data = {
    #     "name": myName,
    #     "tcAccepted":"true",
    #     "email": myEmail,
    #     "message": myMessage,
    #     "adId":ListingID,
    #     "phone": myPhone,
    # } 
    # print(data)


    response = requests.post(url, headers=headers, data=data)
    #jsonresp = response.json()
    print(response.text)


def getListing():
    headers = {
    'Host': 'gateway.daft.ie',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'platform': 'iOS',
    'Accept': 'application/json',
    'brand': 'daft',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Daft.ie/0 CFNetwork/1335.0.3 Darwin/21.6.0'
    }
    url = "https://gateway.daft.ie/old/v1/listings"
    data = '{"section":"residential-to-rent","geoFilter":{"storedShapeIds":["33"],"name":"location","geoSearchType":"STORED_SHAPES","mapView":false},"filters":[{"values":["published"],"name":"adState"}],"paging":{"pageSize":50},"ranges":[{"name":"rentalPrice","to":"' + str(rentalprice) + '","from":""}],"sort":"publishDateDesc"}'

    # print(data)

    response = requests.post(url, headers=headers, data=data)
    jsonresp = response.json()
    listings = jsonresp['listings']

    for x in listings:
        ListingID = x['listing']['id']
        time.sleep(5) # 10 second sleep to avoid spam
        if ListingID not in allAdds:
            print("New Listing found: ", ListingID)
            sendEmail(ListingID)
            allAdds.append(ListingID)

    time.sleep(600) # 10 minute sleep to avoid spam
    print("No new listings found, refreshing.")
    getListing()

    # TODO: Add method to print number of beds and bathrooms


# print('Listing ID:' + ' ' + str(x['listing']['id']) + ' Price: ' + x['listing']['price'])
getListing()

