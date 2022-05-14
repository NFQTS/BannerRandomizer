import tweepy
import random
import datetime
import time
import pickle
from keys import keys

# Api Authentication
client_id = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
bearer_token = keys['bearer_token']
headers = {"Authorization": "Bearer {}".format(bearer_token)}
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# variable to track the date of the last banner change
last_change = 0

# loads the last known banner change date if one exists
try:
    a_file = open("last_change.pkl", "rb")
    last_change = pickle.load(a_file)
    a_file.close()
except:
    print("Couldnt find save data")


def find_day():
    """Finds the current day and returns the day of the month"""
    day = datetime.datetime.today().day
    print(day)
    return day


def banner_change():
    """Randomly selects an image from the list of banner images and replaces your Twitter banner through the Twitter API."""

    # list of images to choose from
    images = ['no rugrets.png', 'plague banner.jpg', 'plagueglad.jpg', 'PlagueSun.jpg', 'The Plague.png']

    # randomizes the selection, but CAN choose the same one multiple times in a row...
    random_image = images[random.randint(0, len(images) - 1)]
    print(random_image)
    print(f"Changing banner to {random_image}")
    image_file = f"images/{random_image}"

    # updates your Twitter banner through the API
    api.update_profile_banner(filename=image_file)


def save_data():
    """Saves the date when a banner is changed."""
    print("Saving Data...")
    a_file = open("last_change.pkl", "wb")
    pickle.dump(last_change, a_file)
    a_file.close()


while True:
    current_day = find_day()
    if current_day != last_change:
        banner_change()
        last_change = current_day
    else:
        print("It's not a new day yet")
    save_data()
    # banner_change() # use just this if you want to swap banners every 30 minutes, make sure to comment out the previous code in this while loop!
    time.sleep(1800) # makes the program run about every 30 minutes

