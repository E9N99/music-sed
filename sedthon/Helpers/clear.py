
from music-sed import blald
from music-sed.Helpers import remove_active_chat


async def _clear_(chat_id):
    try:
        blald[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
