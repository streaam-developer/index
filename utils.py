import re
from pymongo.errors import DuplicateKeyError
from pymongo import MongoClient
from info import DATABASE_URL, DATABASE_NAME, FLOG_CHANNEL

myclient = MongoClient(DATABASE_URL)
mydb = myclient[DATABASE_NAME]
mycol = mydb['Files']

class temp(object):
    CANCEL = False

async def save_file(client, media):
    """Save file in database"""

    file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
    vp = await client.send_cached_media(chat_id=FLOG_CHANNEL, file_id=media.file_id)
    file = {
        'file_name': file_name,
        'file_size': media.file_size,
        '_id': vp.id #not a unique file id, it's message id
    }
    try:
        mycol.insert_one(file)
        return "Saved"
    except DuplicateKeyError:
        return "Duplicates"
    
def get_all_files():
    """Get all files from database"""
    return mycol.find({})

def get_readable_time(seconds):
    periods = [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]
    result = ''
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            result += f'{int(period_value)}{period_name}'
    return result
