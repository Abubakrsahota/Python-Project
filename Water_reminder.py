import time 
from plyer import notification
while True:
    print("Take some water")
    notification.notify(
        title="Drink Water",
        message="It's time to drink water, stay hydrated!",
    )
    time.sleep("time you want to wait in seconds")  # Replace with the desired wait time in seconds






