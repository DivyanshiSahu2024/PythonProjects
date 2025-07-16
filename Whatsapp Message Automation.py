'''
TWILIO
1.TWILIO CLIENT SET UP 
2. USER INPUT 
3. SCHEDULING LOGIC
4. SEND MESSAGE

'''
#Step  1: install required libraries 
from twilio.rest import Client
from datetime import datetime, timedelta
import time
#Step 2: twilio credentials 
account_sid='enter you accountsid here'
auth_token='enter your credentials here'
client=Client(account_sid,auth_token)
#Step 3:
def send_whatsapp_message(recipient_num,message_body):
    try:
        message=client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_num}'
            )
        print(f'Message sent successfully ! Messsage SID{message.sid}')
    except Exception as e:
        print('An error occurred')

#step4 user input
name=input("Enter the recipient name= ")
recipient_num=input('Enter recipient whatsapp number with country code:')
message_body=input(f'Enter the message you want to send to {name}:')
#Step 5- parse date/time and calculate delay
date_str=input('enter the date to send the message (YYYY-MM-DD):')
time_str=input('enter the time to send the message(HH:MM in 24 hour format):')
#datetime
scheduled_datetime=datetime.strptime(f'{date_str}{time_str}',"%Y-%m-%d %H:%M")
current_datetime=datetime.now()
#Calculate delay
time_difference=scheduled_datetime-current_datetime
delay_seconds=time_difference.total_seconds()

if delay_seconds<=0:
    print('The specified time is in the past, please enter a future date and time:')
else :
    print("Message to be sent to {name} at {scheduled_datetime}.")

#Wait until the scheduleed time
time.sleep(delay_seconds)

#Send the message 
send_whatsapp_message(recipient_num,message_body)
