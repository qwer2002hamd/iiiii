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
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                


@app.on_message(
    command(["مبرمج","المبرمج","المبرمـج"])
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ah_2_v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )    




@app.on_message(
    command(["السورس","الـسورس","سورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ah07v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ مـبرمج الـسورس ›", url=f"https://t.me/ah_2_v"), 
                
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
                ],

            ]

        ),

    )
