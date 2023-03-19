from plyer import notification
import time

notification_title = 'Drink Water'  
notification_message = 'This is a gentle reminder for you to drink water after every 2 hours interval.'

while True:
    notification.notify(  
        title = notification_title,  
        message = notification_message,  
        app_icon = None,  
        timeout = 10,  
        toast = False  
        )  
    time.sleep(2 * 60 * 60)