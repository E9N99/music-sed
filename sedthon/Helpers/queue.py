
from music-sed import blald


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = blald.get(chat_id)
    if get:
        blald[chat_id].append(put_f)
    else:
        blald[chat_id] = []
        blald[chat_id].append(put_f)
