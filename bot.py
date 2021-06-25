from instabot import Bot
import os

# create log directory
if os.path.isdir('Logs/') == False:
    os.mkdir('Logs')

username = os.getenv('username')
password = os.getenv('password')
print(username)

bot = Bot()

bot.login(username = 'juicebyjustin',
		password = '2HpNCJqmeGsg8Bnm9msuFLBFqmrUfiZxPAR7HsGGnWNFEvsw7JNiNGas2iHuhmjhWuJhAM6Je')

# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("images/ellenvora-1024x1024.png",
				caption ="Stop Scrolling and Take a Break.")
