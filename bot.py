from telethon import TelegramClient, events, Button
from telethon.errors import ChatAdminRequiredError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.events import StopPropagation
import asyncio, os
from collections import defaultdict
import re

# إعداد البوت
bot = TelegramClient('roletmg', 29111381, "c86ad2e2fadf7016897e792c8e5f2be9")
CHANNEL_ID = -1002341857291 








@bot.on(events.NewMessage(pattern=r'^/start$'))
async def fuckers(event):
    try:
        await event.reply("اهلا بك في بوت روليت سراب\nاستطيع ادارة لك السحوبات والمكافات ، ابدأ الان!")
    except Exception as e:
        print(f"[!] Error: {e}")
















async def main():
    await bot.start(bot_token="8446898647:AAH4PSUezwgn1wTkrv36D32lo_eEdcoD2eI")
    print("bot fucking running ✅")
    
    try:
        # بدل run_until_disconnected استخدم هذه الطريقة
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("\n[!] Shutting down...")
        await bot.disconnect()
        print("[✔] Bot stopped cleanly.")

if __name__ == "__main__":
    task = asyncio.ensure_future(main())
    
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        task.cancel()

        asyncio.get_event_loop().run_until_complete(task)
