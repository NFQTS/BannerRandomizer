# BannerRandomizer
Randomizes your Twitter banner daily.

Please Note:
1.) I run this from inside my IDE (pycharm) so you may need to make some modifications if you want to run this in a more legitimate fashion (from an exe, or the terminal, etc...)
2.) This requires a Twitter Developer account with read/write permissions. Apply for "Elevated access"...
3.) You will need to create a python script named keys.py and store all of your Twitter developer authentication keys in a dictionary named keys for this to work. Otherwise you can store your authentication keys in the main script and edit the "API Authenitcation" portion of the script to call them, but be careful not to share the script with your keys in it...
4.) This script doesn't automatically identify image names yet... so they have to be manually entered as strings in the "images" list, for now.
5.) Image files must be placed in a folder named "images" located in the same directory as the script, unless you want to edit them.
6.) I use a .pkl file to store the date of the last banner change. This just makes it easy for me to run this once per day, but you can remove this entirely and use time.sleep delays to change your banner more frequently if you're willing to make some minor edits to remove the day check.
