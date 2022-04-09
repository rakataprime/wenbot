"""
Example Usage:

random_user
      !echo something

echo_bot
      something
"""

import simplematrixbotlib as botlib
import pandas as pd 

creds = botlib.Creds("https://matrix.org", "@sockpuppetarmy:matrix.org", "NOTPASSWORD")
bot = botlib.Bot(creds)
PREFIX = ''


@bot.listener.on_message_event
async def echo(room, message):
      match = botlib.MessageMatch("gm", message, bot, PREFIX)
      if match.is_not_from_this_bot() and match.prefix(): 
            if match.command( "gm"):
                  await bot.api.send_text_message(room.room_id, "gm")
            if match.command( "juno"):
                  df = pd.read_html("https://coinmarketcap.com/currencies/juno/", )
                  juno_price = df[0].iloc[0,1]
                  await bot.api.send_text_message(room.room_id, f"juno price is {juno_price}" )
            if match.command( ""):
                  df = pd.read_html("https://coinmarketcap.com/currencies/juno/", )
                  juno_price = df[0].iloc[0,1]
                  await bot.api.send_text_message(room.room_id, f"juno price is {juno_price}" )

bot.run()
