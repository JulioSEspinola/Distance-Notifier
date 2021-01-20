import requests
import smtplib

#API key
api_file = open("apiKey.txt", "r")
api_key = api_file.read()
api_file.close()

#home address input
start = input("Enter a starting point address: \n")

#work adress input
end = input("Enter destination adress: \n")
#base url
url =("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&")

#get response
response = requests.get(url + "origins=" + start + "&destinations= " + end + "&key=" + api_key)

#return time as text and seconds
time = response.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = response.json()["rows"][0]["elements"][0]["duration"]["value"]

#print the total travel time
print("\nThe total travel time from " + start + " to " + end + " is", time)

#check if the time is more tha 30 minutes
if (seconds > 1800):
    #get sender email
    sender = input(str('enter your email: '))
    password = input(str("pLease enter your password: "))
    receiver = input(str('enter recipient eamil: '))
    message = input(str("Enter message:"))

    #create SMTP sessions
    server = smtplib.SMTP('smtp.gmail.com', 587)

    #Starts TLS for security
    server.starttls()

    #Cheks if the password is correct
    if(password == False):
        password = input(str("Incorrect password. Please enter password one more time: "))
    
    #authentication
    server.login(sender,password)
    print("Login Sucess")

    #send the email
    server.sendmail(sender,receiver, message)
    print("Email has been sent to", receiver)
    server.quit()
 