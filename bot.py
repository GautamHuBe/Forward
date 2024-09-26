import asyncio
from database import db 
from config import Config, temp
from pyrogram import Client, __version__
from pyrogram.raw.all import layer 
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait
from plugins import logger
from pyromod.helpers import ask

class Bot(Client): 
    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            bot_token=Config.BOT_TOKEN,
            plugins={"root": "plugins"},
            workers=100,
        )
        
    async def start(self):
        await super().start()
        me = await self.get_me()
        logger.info(f"{me.first_name} with for pyrogram v{__version__} (Layer {layer}) started on @{me.username}.")
        temp.ID = me.id
        temp.UNAME = me.username
        temp.NAME = me.first_name
        self.set_parse_mode(ParseMode.DEFAULT)
        text = "**๏[-ิ_•ิ]๏ bot restarted !**"
        logger.info(text)
        success = failed = 0
        users = await db.get_all_frwd()
        async for user in users:
           chat_id = user['user_id']
           try:
              await self.send_message(chat_id, text)
              success += 1
           except FloodWait as e:
              await asyncio.sleep(e.value + 1)
              await self.send_message(chat_id, text)
              success += 1
           except Exception:
              failed += 1 
    #    await self.send_message("venombotsupport", text)
        if (success + failed) != 0:
           await db.rmve_frwd(all=True)
           logger.info(f"Restart message status"
                 f"success: {success}"
                 f"failed: {failed}")

    async def stop(self, *args):
        msg = f"@{temp.UNAME} stopped. Bye."
        await super().stop()
        logger.info(msg)
   
