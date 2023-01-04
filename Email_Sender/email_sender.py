from email.message import EmailMessage
import dotenv
import os
import ssl
import smtplib
import time
import random
import pytz
import datetime




# Loads the env file in the root directory
dotenv.load_dotenv()

# Retrieves email sender, receiver and password from the .env file. Prints an error message (ValueError) in the terminal if it fails
try:
    email_password = os.environ['PASSWORD']
    email_sender = os.environ['SENDER']
    email_receiver = os.environ['RECEIVER']
except KeyError:
    # Password not found in the .env file
    raise ValueError("Password not found in the .env file")

# Returns a random message from the list of messages
def get_random_message():
  messages = [
    "Coding once a day keeps the doctor away! Well, not really, but it's still good for you!",
    "All day I dream about code! Well, night. But you get the point, right? Time to get after it!",
    "Don't let your skills rust-learn Rust instead!",
    "Use it or lose it. It's time to code.",
    "Today is a great day to code! Why not challenge yourself to learn something new?",
    "Time to write something BLAZINGLY FAST!",
    "Today is a great day to learn some TypeScript!",
    "Remember to sign up for neetcode! You want to make the big bucks, right?",
  ]
  body = random.choice(messages)
  return body

  # Day, email subject and body
day = 1
subject = 'Reminder to code everyday for 100 days'
body = f" (Welcome to day {day} of 100 days of coding!)" + get_random_message() 

#Specifies the timezone
timezone = pytz.timezone('US/Eastern')


def send_reminder(message, recipient, day):

    print("Sending reminder to", recipient)
    print(message)
    msg = EmailMessage()

    msg['subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(message)


# Creates a secure SSL context, then logs into the email sender, then sends the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())


while day <= 100:
    
    # Get the current time in the specified time zone
    local_time = datetime.datetime.now(timezone)

  # Checks if it is after midnight, if it is, send the email
    if local_time.hour >= 0 and local_time.hour < 6:
     send_reminder(body, email_receiver, day)
    time.sleep(86400) # pause for 86400 seconds (1 day)
    day += 1

  # If it's not after midnight, wait for 1 hour and check again
    time.sleep(3600)