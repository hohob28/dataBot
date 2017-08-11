import os
import sys
import datetime
from argparse import ArgumentParser
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler


from flask import Flask, request, abort
from linebot import (
                     LineBotApi, WebhookParser
                     )
from linebot.exceptions import (
                                InvalidSignatureError, LineBotApiError
                                )
from linebot.models import (
                            MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage
                            )

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

my_group_id = os.getenv('GROUP_ID', None)
if my_group_id is None:
    print('GROUP_ID as environment variable.')
    sys.exit(1)

image1 = os.getenv('IMAGE1', None)
if image1 is None:
    print('IMAGE1 as environment variable.')
    sys.exit(1)

image2 = os.getenv('IMAGE2', None)
if image2 is None:
    print('IMAGE2 as environment variable.')
    sys.exit(1)

image3 = os.getenv('IMAGE3', None)
if image3 is None:
    print('IMAGE3 as environment variable.')
    sys.exit(1)

image4 = os.getenv('IMAGE4', None)
if image4 is None:
    print('IMAGE4 as environment variable.')
    sys.exit(1)

image5 = os.getenv('IMAGE5', None)
if image5 is None:
    print('IMAGE5 as environment variable.')
    sys.exit(1)

image6 = os.getenv('IMAGE6', None)
if image6 is None:
    print('IMAGE6 as environment variable.')
    sys.exit(1)

image7 = os.getenv('IMAGE7', None)
if image7 is None:
    print('IMAGE7 as environment variable.')
    sys.exit(1)

image8 = os.getenv('IMAGE8', None)
if image8 is None:
    print('IMAGE8 as environment variable.')
    sys.exit(1)

image9 = os.getenv('IMAGE9', None)
if image9 is None:
    print('IMAGE9 as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)



## simulate day
#my_date = date.today()
#
## Start the scheduler
#sched = BlockingScheduler()
#@sched.scheduled_job('interval', seconds=1)
#def timed_job():
#    print('This job is run every 1 seconds.')
#
##@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
##def scheduled_job():
##    print('This job is run every weekday at 10am.')
#
##sched.configure(options_from_ini_file)
#sched.start()




## Schedules job_function to be run once each minute
#sched.add_job(checkAndSend,  second='5')

# simulate day
my_date = date.today()


# Start the scheduler
sched = BlockingScheduler()
@sched.scheduled_job('interval', seconds=5)
def checkAndSend():
    global my_date
    date_string = my_date.strftime('%Y-%m-%d')
    print(date_string)
    try:
        #I just want my group to receive msg
        
        line_bot_api.push_message(my_group_id, TextSendMessage(text=date_string))
#        line_bot_api.push_message(my_group_id, ImageSendMessage(original_content_url='https://image.ibb.co/mjCpra/S_75849824.jpg', preview_image_url='https://image.ibb.co/mjCpra/S_75849824.jpg'))
    except LineBotApiError as e:
        abort(400)
    my_date += datetime.timedelta(days=1)




#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
#def scheduled_job():
#    print('This job is run every weekday at 10am.')

#sched.configure(options_from_ini_file)
sched.start()

