from instabot import Bot
import os

username = os.getenv('username')
password = os.getenv('password')

bot = Bot()

bot.login(username = "user",
		password = "pass")

# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("images/ellenvora-1024x1024.png",
				caption ="Stop Scrolling and Take a Break.")
