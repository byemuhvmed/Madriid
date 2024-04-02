import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["حمودي","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6fe7de7485c993122bc4a.jpg",
        caption=f"""- 𝖴𝖾𝗌 : @MH_BP
- 𝖲𝗍𝖺 : مطـور السورس  
- i𝖽 : 6463481188
- bio : متسالنيش عن احوالي ، انا تايه """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "hamody .", url=f"https://t.me/MH_BP"), 
                 ],[
                   
                ],

            ]

        ),

    )
