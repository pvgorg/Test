from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client
from datetime import datetime
import random
import pytz

#os.system("pip install apscheduler && pip install datetime && pip install pyrogram && pip install pytz && pip install time && pip install random && pip install requests && pip install json ")

api_id = 13969248
api_hash = "6e7fe82b1a542bcd0fe485d944d2397a"
bot = Client("my_account", api_id=api_id, api_hash=api_hash)
admin = 6269236660

fonts = {
    'Font1' : { '0': '𝟎','1': '𝟏','2': '𝟐','3': '𝟑','4': '𝟒','5': '𝟓','6': '𝟔','7': '𝟕','8': '𝟖','9': '𝟗' },
    'Font2' : { '0': '𝟘','1': '𝟙','2': '𝟚','3': '𝟛','4': '𝟜','5': '𝟝','6': '𝟞','7': '𝟟','8': '𝟠','9': '𝟡' },
    'Font3' : { '0': '⓪','1': '①','2': '②','3': '③','4': '④','5': '⑤','6': '⑥','7': '⑦','8': '⑧','9': '⑨' },
    'Font4' : { '0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵','6': '⁶','7': '⁷','8': '⁸','9': '⁹' },
    'Random' : 'Random'
}

FONT = "Font4" # انتخاب فونت از لیست بالا

async def TimeName():
    tz = pytz.timezone("Asia/Tehran")
    now = datetime.now(tz)
    if ( now.strftime("%S") == "00") :

        number = now.strftime("%H:%M")

        if FONT == "Random":
            
            try:
                selected_font = random.choice(list(fonts.keys()))
                tz = pytz.timezone("Asia/Tehran")
                now = datetime.now(tz)
                current_time = now.strftime("%H:%M")

                converted_time = ''.join([fonts[selected_font].get(char, char) for char in current_time])

                await bot.update_profile(last_name=converted_time)
            except :
                pass
        else:
            number_unicode = ''.join([fonts[FONT][c] if c in fonts[FONT] else c for c in str(number)])
            await bot.update_profile(last_name=number_unicode)


async def TimeBio():
    tz = pytz.timezone("Asia/Tehran")
    now = datetime.now(tz)
    if ( now.strftime("%S") == "00") :
        # عددی که می‌خواهی چاپ کنه
        number = now.strftime("%H:%M")

        if FONT == "Random":
            
            try:
                selected_font = random.choice(list(fonts.keys()))
                tz = pytz.timezone("Asia/Tehran")
                now = datetime.now(tz)
                current_time = now.strftime("%H:%M")

                converted_time = ''.join([fonts[selected_font].get(char, char) for char in current_time])
            except :
                pass
            await bot.update_profile(bio="Time Now : "+converted_time)


        else:
            number_unicode = ''.join([fonts[FONT][c] if c in fonts[FONT] else c for c in str(number)])
            await bot.update_profile(bio="Time Now : "+number_unicode)



scheduler = AsyncIOScheduler()
scheduler.add_job(TimeName, "interval", seconds=1)
scheduler.add_job(TimeBio, "interval", seconds=1)


print('bot is run')
scheduler.start()
bot.run()
