
import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from strings import get_command
from strings.filters import command
from config import BANNED_USERS
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

    
  
REPLY_MESSAGE = "اليك لوحه التحكم الخاصه بالاعضاء"

REPLY_MESSAGE_BUTTONS = [
         [
             ("المبرمـج"),                   
             ("اوامر التشغيل")

          ],
          [
             ("طريقه التفعيل"),
             ("الـسورس") 
          ],
          [
             ("اخـفاء الكيبورد")
          ]
]

  
@app.on_message(filters.regex("/HAMD"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

        
        
        

@app.on_message(filters.private & command("طريقه التفعيل"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""
❓ طريقة استخدام البوت

1.) اولا قم بإضافة البوت في مجموعتك.
2.) ثانيا قم برفعه مشرف اعطائه جميع الصلاحيات.
3.) قم بفتح الدردشة المرئيه قبل التشغيل.
4.) القي نظره علي الاوامر لتعلم طريقه التشغيل.

•⎆: قناه السورس @ah07v
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/USER_BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



###################new lian#############

REPLY_MESSAGEE = "اليك لـوحه اوامر التشغيل"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("اوامر القناه"), 
             ("اوامر المجموعه") 
          ],
          [  
             ("اوامر بالانگليزي")             
          ],
          [
             ("رجوع"), 
             ("اخـفاء الكيبورد") 
          ]
]

  
@app.on_message(filters.private & command("اوامر التشغيل"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.private & command("رجوع"))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.private & command("اوامر القناه"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""
♚ مرحبا بك في اومر التشغيل بالقنوات

››  تشغيل ↫ اسم الاغنيه .
››  فيديو ↫ اسم الفديو .
››  انهاء ↫ لانهاء التشغيل في القناه .
››  تخطي ↫ لتخطي تشغيل القناه .
›› وقف ↫ لايقاف التشغيل مؤقتا في القناة
›› ربط القناه ↫ ايدي  القناه لربطها بالمجموعه .
›› مـطور الـبوت ↫ @ah_2_v

•⎆: قـناة السورس @ah07v
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/USER_BOT?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("اوامر المجموعه"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""
♚ مرحبا بك في اوامر التشغيل في المجموعات

•اوامر التشغيل العربيه

›› تشغيل ↫ لتشغيل اغنية
›› فيديو ↫ لتشغيل فيديو 
›› تخطي ↫ لتخطي التشغيل الحالي
›› ايقاف ↫ لانتهاء التشغيل الحالي
›› وقف ↫ لايقاف التشغيل الحالي مؤقتا
›› استئناف ↫ لاستمرار التشغيل المتوقف
›› قائمة التشغيل ↫ لمعرفة التشغيل الحالي 
›› تحميل ↫ لتحميل اغنية من اليوتيوب
›› تحميل فيديو ↫ لتحميل فيديو من اليوتيوب
›› اعدادات ↫ لضبط اعدادات البوت
›› يـوزر الـمطور ↫ @ah_2_v

•⎆: قـناه الـسورس @ah07v
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/USER_BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.private & command("اوامر بالانگليزي"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""
♚ مرحبا بك في اوامر التشغيل في المجموعات

•اوامر التشغيل الانگليزيه

/play - لتشغيل اغنيه
/vplay - لتشغيل فيديو
/playlist - لمعرفة قائمة التشغيل 
/skip - لتخطي التشغيل الحالي
/stop - ايقاف التشغيل الحالي
/pause - لايقاف التشغيل الحالي مؤقتا
/resume - استئناف التشغيل الحالي
/reload - تحديث قائمة الادمنية
/song - تحميل اغنيه من يوتيوب
/video - تحميل فيديو من يوتيوب

›› يـوزر الـمطور @ah_2_v

•⎆: قـناه الـسورس @ah07v

 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ قـناة الـسورس ›", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك", url=f"https://t.me/USER_BOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )




   
