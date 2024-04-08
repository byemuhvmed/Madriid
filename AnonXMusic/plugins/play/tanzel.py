import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from yt_dlp import YoutubeDL 
from youtube_search import YoutubeSearch
from AnonXMusic import app
import os

@app.on_message(filters.command([ نزل , تنزيل , حمل , تحميل ],""))
async def download_song(c,msg):
  if msg.text ==  حمل  or msg.text == "نزل":
    return await msg.edit(f <b> يرجي كتابة {msg.text} + اسم الاغنية</b> )
  else:
    name = msg.text.split(   ,1)[1]
    x = await msg.reply(f <b>جاري البحث انتظر قليلاً .🚦</b> )
    ydl_opts = {"format": "bestaudio[ext=m4a]"} if msg.text.split()[0] ==  نزل  else {"format": "best","keepvideo": True,"prefer_ffmpeg": False,"geo_bypass": True,"outtmpl": "%(title)s.%(ext)s","quite": True}
    try:
      results = YoutubeSearch(name,max_results=1).to_dict()
      link = f"https://youtube.com{results[0][ url_suffix ]}"
      title = results[0]["title"][:40]
      thumbnail = results[0]["id"]
      thumb_name = f"thumb{results[0][ id ]}.jpg"
      thumb = requests.get(f"https://img.youtube.com/vi/{thumbnail}/hqdefault.jpg", allow_redirects=True)
      open(thumb_name, "wb").write(thumb.content)
      duration = results[0]["duration"]
    except Exception as e:
      return await msg.edit(f <b> حدث خطا :</b> \n {e} )
    await x.edit( <b>جاري الارسال</b> )  
    with YoutubeDL(ydl_opts) as ytdl:
      ytdl_data = ytdl.extract_info(link,download=True)
      file_name = ytdl.prepare_filename(ytdl_data)
    
    rep = f"<b> {title}</b>\n<b> • uploader : @MH_BP</b>"
    secmul, dur, dur_arr = 1, 0, duration.split(":")
    for i in range(len(dur_arr) - 1, -1, -1):
        dur += int(dur_arr[i]) * secmul
        secmul *= 60
    await x.edit("<b>يتم الارسال</b>")
    try:
      if msg.text.split()[0] ==  نزل :
        await app.send_audio(
          chat_id=msg.chat.id,
          audio=file_name,
          caption=rep,
          thumb=thumb_name,
          title=title,
          duration=dur)
      else:
        await app.send_video(
          chat_id=msg.chat.id,
          video=file_name,
          caption=rep,
          thumb=thumb_name,
          duration=dur)
      await x.delete()
    except Exception as e:
      return await msg.edit(f <b>حدث خطا :</b> \n {e} )
    try:
      os.remove(file_name)
      os.remove(thumb_name)
    except: pass
    