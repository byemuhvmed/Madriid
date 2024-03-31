from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني لجروبك", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𓏺 ََِ𝗠𝗔𝗗𝗥𝗜𝗗 ↺", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضفني لمجموعتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الاوامر", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="مطور السورس", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𓏺 ََِ𝗠𝗔𝗗𝗥𝗜𝗗 ↺", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="قناه المطور", url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons
