import asyncio
from config import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins import logger
     
import time as tm
from database import db 
from .test import parse_buttons

STATUS = {}

async def handle_force_sub(client, message):
 try:
    uid = message.from_user.id
    buttons = []
    if Config.FSUB_CHANNELS:
       for channel in Config.FSUB_CHANNELS:
           chat = await client.get_chat(channel)
           text = "**🔒 Join The Channels Below To Use Me 🔒**\n"
           try:
               await client.get_chat_member(chat_id=channel, user_id=uid)
           except UserNotParticipant:
               invite_link = await client.export_chat_invite_link(chat_id=channel)
               buttons.append([InlineKeyboardButton(f"Join {chat.title}", url=invite_link)])
       return text, buttons
 except Exception as e:
     logger.error('fsub', exc_info=True)
     return await srm(client, message, f"Got An Error - {str(e)}")

async def srm(c, m, text, photo=None, video=None, markup=None, reply_id=None, delete=20, iscall=False, **kwargs):
 try:
   replymarkup = None if markup is None else InlineKeyboardMarkup(markup)
   mid = m.message.id if iscall else m.id
   replyid = mid if reply_id is None else reply_id
   tosend = m.message.chat.id if iscall else m.chat.id
   if photo:
      my = await c.send_photo(
          chat_id=tosend,
          photo=photo,
          caption=text,
          reply_to_message_id=mid,
          reply_markup=replymarkup,
          **kwargs
      )
   elif video:
       pass
       
   else:
      my = await c.send_message(
          chat_id=tosend,
          text=text,
          reply_to_message_id=mid,
          reply_markup=replymarkup,
          **kwargs
      )
   if delete:
      await delete_msg([my, m], dt=delete)
 except:
   LOGGER.error('srm', exc_info=True)
     
async def delete_msg(msg_list: list, dt=10):
    async def _delete_messages():
        try:
            await asyncio.sleep(dt)
            for msg in msg_list:
                if msg:
                    try:
                        await msg.delete()
                        LOGGER.info("Message Deleted Succefully...")
                    except Exception as e:
                        pass 
        except Exception as e:
            pass
    asyncio.create_task(_delete_messages())
    

class STS:
    def __init__(self, id):
        self.id = id
        self.data = STATUS
    
    def verify(self):
        return self.data.get(self.id)
    
    def store(self, From, to,  skip, limit):
        self.data[self.id] = {"FROM": From, 'TO': to, 'total_files': 0, 'skip': skip, 'limit': limit,
                      'fetched': skip, 'filtered': 0, 'deleted': 0, 'duplicate': 0, 'total': limit, 'start': 0}
        self.get(full=True)
        return STS(self.id)
        
    def get(self, value=None, full=False):
        values = self.data.get(self.id)
        if not full:
           return values.get(value)
        for k, v in values.items():
            setattr(self, k, v)
        return self

    def add(self, key=None, value=1, time=False):
        if time:
          return self.data[self.id].update({'start': tm.time()})
        self.data[self.id].update({key: self.get(key) + value}) 
    
    def divide(self, no, by):
       by = 1 if int(by) == 0 else by 
       return int(no) / by 
    
    async def get_data(self, user_id):
        bot = await db.get_bot(user_id)
        k, filters = self, await db.get_filters(user_id)
        size, configs = None, await db.get_configs(user_id)
        if configs['duplicate']:
           duplicate = [configs['db_uri'], self.TO]
        else:
           duplicate = False
        button = parse_buttons(configs['button'] if configs['button'] else '')
        if configs['file_size'] != 0:
            size = [configs['file_size'], configs['size_limit']]
        return bot, configs['caption'], configs['forward_tag'], {'chat_id': k.FROM, 'limit': k.limit, 'offset': k.skip, 'filters': filters,
                'keywords': configs['keywords'], 'media_size': size, 'extensions': configs['extension'], 'skip_duplicate': duplicate}, configs['protect'], button
        
