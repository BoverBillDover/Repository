import smtplib, ssl
import getpass
import requests
import time



#message 1
port = 465
sender_email = "boverbilldover@gmail.com"
receiver_email = "2622716383@tmomail.net"



#encryption
context = ssl.create_default_context()




print("press ctrl+c to stop the program")

#while loop
while True:
    #get stock price
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"

    querystring = {"region":"US","lang":"en","symbols":"MSFT"}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "2c5243b3c1msh76c87b8516fffcfp17b2cajsn45f3d1ae655d"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    x = response.json()

    price = x['quoteResponse']['result'][0]['regularMarketPrice']

    z = round(price-0.5)

    #message 1
    subject = 'Stock info'
    body1 = f"the price for Microsoft stock is currently over the price of {price-0.01}!"

    message1 = f"Subject:{subject}\n\n{body1}"

    password = "Theethan225"


    #message 2
    body2 = f"the price for Mircrosoft stock has currently dropped under the price of {price+0.01}"

    message2 = f"Subject:{subject}\n\n{body2}"


    #check price
    if price >= z+1:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("boverbilldover@gmail.com", password)
            server.sendmail(sender_email, receiver_email, message1)
        print("Message sent")
        z = z+1

    if price <= z:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("boverbilldover@gmail.com", password)
            server.sendmail(sender_email, receiver_email, message2)
        print("Message sent")
        z = z-1

    print(f"price is currently {price}")
    time.sleep(600)
