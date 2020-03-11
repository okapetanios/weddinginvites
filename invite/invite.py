import os
import json
import time
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from twilio.rest  import Client

#Message your attendees from a spreadsheet

json_key = json.load(open('client_secret.json'))#add file name for the json created for the spread sheet
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
wks = gc.open("wedding_invites") #add workbook name here
wks_attendees = wks.get_worksheet(1) #attendees worksheet

ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_PER']
AUTH_TOKEN = os.environ['TWILIO_ACCOUNT_TOKEN_PER'] 

client = Client(ACCOUNT_SID, AUTH_TOKEN) 
     
for num in range(3,60):  #to iterate between guests, amend this based total
    print "sleeping for 2 seconds"
    time.sleep(2) #adding a delay to avoid filtering
    
    guest_number = wks_attendees.acell('B' +str(num)).value
    guest_name = wks_attendees.acell('A'+str(num)).value
    
    if not  guest_number:
        print guest_name + ' telephone number empty not messaging'
        wks_attendees.update_acell('E'+str(num), '0') #set number to 0
    
    else:
        print  'Sending message to ' + guest_name
        client.messages.create(
            to="+1" + guest_number, 
            from_="+1"+"2403033692", #your twilio number here
            body= "Dear "+ guest_name + ", Please join us in celebrating the marriage of Eric Egan and Lillian Gaines on:\n\nSaturday, the 2nd of May, 2020. \n\nPlease follow the link to our website for all necessary information and to RSVP by March 15.\n\ntheknot.com/lilliananderic\n\nPlease contact Lillian or Eric with any questions.\n\n" + u"\u2B50" + u"\u2B50" + u"\u2B50" + u"\u2B50" + u"\u2B50" + u"\u2B50" + u"\u2B50" + u"\u2B50",  
            #body ="Hello you lovely people, tomorrow is the big day!!\n\nPost code for the venue: CM6 1RQ\n\nArrival time one thirty for a two o'clock ceremony.\n\nIt is a cash bar, so please bring sufficient money with you as there is no nearby cash machine.\n\nIt might be raining at some point in the day, so an umbrella might be required.\n\nThe venue is non smoking, due to the thatched buildings.\n\nWe could not be more excited that you are joining us for our special day and looking forward to sharing great food and good times!\n\nTom & Lauren",
        )
        #int(wks_attendees.acell('E' + str(num)).value)
        wks_attendees.update_acell('E'+str(num), float(wks_attendees.acell('E' + str(num)).value) + 1) #increment the message count row
else:                  # else part of the loop
   print 'finished'
