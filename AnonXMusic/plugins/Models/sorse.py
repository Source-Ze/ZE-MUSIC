
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "Ze"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/73f9dd795b22c7cb670d6.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ѕᴏụʀᴄᴇ Ze⌝](https://t.me/UI_XB)⧽⌯⊶★═╮\n★‹ [⌞ѕᴏụʀᴄᴇ Ze⌝](https://t.me/UI_XB)\n★‹ [𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮ِ](https://t.me/UP_UO)\n╰═★⊷⌯⧼[⌞ ѕᴏụʀᴄᴇ Ze⌝](https://t.me/UI_XB)⧽⌯⊶★═╯\n ⍟ Welcome to ѕᴏụʀᴄᴇ Ze""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𐇮 𝑴𝑶𝑫𝒀 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮", url=f"https://t.me/UP_UO"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ѕᴏụʀᴄᴇ Ze⌝⚡️", url=f"https://t.me/UI_XB"),
                ],[
                    InlineKeyboardButton(
                        "للتنصيب راسلني", url=f"https://t.me/UP_UO"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



