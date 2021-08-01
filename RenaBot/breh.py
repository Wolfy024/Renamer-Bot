import sys
import pathlib
import time
import datetime as dt
import os
sys.path.insert(0, f"{pathlib.Path(__file__).parent.resolve()}")

from FastTelethon import upload_file, download_file

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0 or unit == 'PB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

async def download_with_progressbar(client, msg,down_location,edited):
    timer = Timer()

    async def progress_bar(downloaded_bytes, total_bytes):
        if timer.can_send():
            data = progress_bar_str(downloaded_bytes, total_bytes)
            edited.edit(f"Downloading...\n{data}")

    file = msg.document
    filename = msg.file.name
    dir = f"{down_location}"
    try:
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)
    except SyntaxError:
        print("Write the path correctly.") 
        raise SyntaxError
    if not filename:
        filename = (
            "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                    )
    download_location = dir + filename
    with open(download_location, "wb") as f:
        await download_file(
            client=client, 
            location=file, 
            out=f,
            progress_callback=progress_bar
        )
    return download_location

async def upload_with_progress_bar(client,edited, file_location, name=None, thumbnail=None):
    timer = Timer()
    if name == None:
        name = file_location.split("/")[-1]
    async def progress_bar(downloaded_bytes, total_bytes):
        if timer.can_send():
            data = progress_bar_str(downloaded_bytes, total_bytes)
            edited.edit(f"Uploading...\n{data}")

    with open(file_location, "rb") as f:
        the_file = await upload_file(
            client=client,
            file=f,
            name=name,
            progress_callback=progress_bar
        )
    the_message = await client.send_message(
        edited.chat_id, file=the_file,
        force_document=True,
        thumb=thumbnail
    )
    return the_message

async def download_without_progressbar(client, msg,down_location):
    file = msg.document
    filename = msg.file.name
    dir = f"{down_location}"
    try:
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)
    except SyntaxError:
        print("Write the path correctly.") 
        raise SyntaxError   
    if not filename:
        filename = (
            "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                    )
    download_location = dir + filename
    with open(download_location, "wb") as f:
        await download_file(
            client=client, 
            location=file, 
            out=f,
        )
    return download_location

async def upload_without_progress_bar(client, entity, file_location, name=None, thumbnail=None):
    if name == None:
        name = file_location.split("/")[-1]

    with open(file_location, "rb") as f:
        the_file = await upload_file(
            client=client,
            file=f,
            name=name,
        )
    the_message = await client.send_message(
        entity, file=the_file,
        force_document=True,
        thumb=thumbnail
    )
    return the_message

def progress_bar_str(done, total):
    percent = round(done/total*100, 2)
    strin = "░░░░░░░░░░"
    strin = list(strin)
    for i in range(round(percent)//10):
        strin[i] = "█"
    strin = "".join(strin)
    final = f"Percent: {percent}%\n{human_readable_size(done)}/{human_readable_size(total)}\n{strin}"
    return final
    
