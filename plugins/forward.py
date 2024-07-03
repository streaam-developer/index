from pyrogram import Client, filters, errors
from info import ADMINS, FORWARD_CHAT, DOMAIN
from utils import get_all_files
import asyncio

@Client.on_message(filters.command('forward') & filters.private & filters.incoming & filters.user(ADMINS))
async def forward(client, message):
    msg = await message.reply("Processing...")
    files = get_all_files()
    for file in files:
        try:
            await client.send_message(chat_id=FORWARD_CHAT, text=f"📂<b>Fɪʟᴇ Nᴀᴍᴇ : </b>{file.file_name}\n\n<b>Fɪʟᴇ Sɪᴢᴇ</b> : {file.file_size}\n\n<b>Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ</b> : {DOMAIN}{file._id}")
            await asyncio.sleep(1)
        except errors.FloodWait as e:
            await asyncio.sleep(e.value)
            await client.send_message(chat_id=FORWARD_CHAT, text=f"📂<b>Fɪʟᴇ Nᴀᴍᴇ : </b>{file.file_name}\n\n<b>Fɪʟᴇ Sɪᴢᴇ</b> : {file.file_size}\n\n<b>Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ</b> : {DOMAIN}{file._id}")
            continue
    await msg.edit("Done !")
