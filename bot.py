"""
Example Usage:

random_user
      !echo something

echo_bot
      something
"""

import simplematrixbotlib as botlib
import pandas as pd 
import subprocess, aiofiles

creds = botlib.Creds("https://matrix.org", "@sockpuppetarmy:matrix.org", "YOUSHALLNOTPASS")
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
            if match.command("get contract"):
                  subprocess.run(["junod",  "query", "wasm", "code", f"{match.event.body().replace("get contract ", " ").replace(" ", "")}", "example.wasm", "--node", "https://rpc-juno.nodes.guru:443", "--chain-id" , "juno-1"])
                  
                  file_stat = await aiofiles.stat("example.wasm")
                  async with aiofiles.open("example.wasm", "r+b") as f:
                        resp, maybe_keys = await bot.api.async_client.upload(
                              f,
                              content_type="text/plain",
                              filename="example.wasm",
                              filesize=file_stat.st_size()
                        )


bot.run()
