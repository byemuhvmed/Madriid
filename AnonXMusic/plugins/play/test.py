from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant

# Initialize the bot and define the channel that users must be subscribed to
channel = "M_C_II"

# Define a function to check if a user is subscribed to the channel
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try:
        await app.get_chat_member(channel, user_id)
    except UserNotParticipant:
        return False
    return True

# Create a filter to check if a user is subscribed
subscribed = filters.create(subscription)

# Define a function to handle messages from users who are not subscribed
@app.on_message(~subscribed)
async def checker(_: Client, message: Message):
    # If the message is in a group or supergroup chat, delete it
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        await message.delete()

    # Get the user's ID and name
    user_id = message.from_user.id
    user = message.from_user.first_name

    # Define the markup for the inline keyboard with a button to join the channel
    markup = Markup([
        [Button("𓏺 ََِ𝗠𝗔𝗗𝗥𝗜𝗗 ↺", url=f"https://t.me/{channel}")]
    ])

    # Send a message to the user telling them to subscribe to the channel
    await message.reply(
        f"عذرًا عزيزي {user}عليك الإشتراك بقناة السور أولا.",
        reply_markup = markup
    )
