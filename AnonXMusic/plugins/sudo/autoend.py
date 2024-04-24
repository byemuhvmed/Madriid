from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command(["/autoend", "الايقاف التلقائي"], "") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>مثال :</b>\n\n/autoend [enable | disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "تم تفعيل الايقاف التلقائي ↺"
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("تم تعطيل الايقاف التلقائي ↺")
    else:
        await message.reply_text(usage)