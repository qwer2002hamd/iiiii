#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki


from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils.database import music_on, music_off
from AnonX.utils.decorators import AdminRightsCheck

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(
    filters.command(MUTE_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"], disable_web_page_preview=True)
    await mute_on(chat_id)
    await Anon.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention), disable_web_page_preview=True
    )
