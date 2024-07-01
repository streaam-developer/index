from pyrogram import Client, filters, enums
from utils import mydb
from info import FLOG_CHANNEL

usrcol = mydb['Users']

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    if not usrcol.find({'user_id': message.from_user.id}):
        usrcol.insert_one({'user_id': message.from_user.id, 'username': message.from_user.username, 'name': message.from_user.first_name})
    if len(message.command) != 2:
        await message.reply_text("Hello")
        return
    vp = await client.get_messages(FLOG_CHANNEL, message.command[1])
    media = vp.document or vp.video
    await message.reply_cached_media(file_id=media.file_id, caption=media.file_name)