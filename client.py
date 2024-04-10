import os
from telethon import TelegramClient, events
from datetime import datetime, timedelta
import re
from dotenv import load_dotenv

load_dotenv()
me = None
# Remember to use your own values from my.telegram.org!
client = TelegramClient('anon', os.getenv('API_ID'), os.getenv('API_HASH'))
bot = TelegramClient('bot', os.getenv('API_ID'), os.getenv('API_HASH')).start(bot_token=os.getenv('BOT_TOKEN'))


@client.on(events.NewMessage(chats=[int(os.getenv('CHAT_LISTEN_ID'))]))
async def handle_event(event):
    date_str =  (event.original_update.message.date+timedelta(hours=5, minutes=45)).strftime("%Y-%m-%d %H:%M")
    msg_str = event.original_update.message.message
    if re.search('[0-9]|bulk', msg_str, flags=re.IGNORECASE):
        await bot.send_message(int(os.getenv('CHAT_FORWARD_ID')), f"{date_str}->{msg_str}", silent=False)


async def main():
    me = await client.get_me()
    
with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()