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
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["حمودي"‚"المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6fe7de7485c993122bc4a.jpg",
        caption=f"""Developer Name : ˛ hamody .  
Devloper Username : @MH_BP ، 
‏ⓘ متسالنيش عن احوالي ، انا تايه """,
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
