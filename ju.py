from telethon import TelegramClient, events
import asyncio

api_id = 3716204
api_hash = '11cd035693085ec9ec794a1ce7e9c9a3'

my_channel_id = -1001552880572
channels = [-1001540692412]

client = TelegramClient('myGrab', api_id, api_hash)
print("GRAB - Started")


@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message)
 
client.start()
client.run_until_disconnected()
