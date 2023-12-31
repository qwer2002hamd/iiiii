from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils.database import set_loop
from AnonX.utils.decorators import AdminRightsCheck
from AnonX.utils.decorators.adminss import AdminRightsCheckk
from AnonX.utils.inline.play import close_keyboard
from strings.filters import command
# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    command(PAUSE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await Anon.pause_stream(chat_id)
    await music_off(chat_id, 0)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard,
    )

@app.on_message(
    command(PAUSE_COMMAND)
    & filters.channel
    & ~BANNED_USERS
)
@AdminRightsCheckk
async def pause_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await Anon.pause_stream(chat_id)
    await music_off(chat_id, 0)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard,
    )
