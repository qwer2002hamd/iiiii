import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds

import random



selections = [
    "▁▄▂▇▄▅▄▅▃",
    "▁▃▇▂▅▇▄▅▃",
    "▃▁▇▂▅▃▄▃▅",
    "▃▄▂▄▇▅▃▅▁",
    "▁▃▄▂▇▃▄▅▃",
    "▃▁▄▂▅▃▇▃▅",
    "▁▇▄▂▅▄▅▃▄",
    "▁▃▅▇▂▅▄▃▇",
    "▃▅▂▅▇▁▄▃▁",
    "▇▅▂▅▃▄▃▁▃",
    "▃▇▂▅▁▅▄▃▁",
    "▅▄▇▂▅▂▄▇▁",
    "▃▅▂▅▃▇▄▅▃",
]

## After Edits with Timer Bar





## After Edits with Timer Bar


def stream_markup_timer(_, videoid, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ قـناة الـسورس ›", url="https://t.me/ah07v"
            )
        ],
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك", url="https://t.me/USER_BOT?startgroup=true"
            ) 
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    bar = random.choice(selections)
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup None|{chat_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ قـناة الـسورس ›", url="https://t.me/ah07v"
            )
        ],
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك", url="https://t.me/USER_BOT?startgroup=true"
            ) 
        ],
    ]
    return buttons


## Inline without Timer Bar


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ قـناة الـسورس ›", url="https://t.me/ah07v"
            )
        ],
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك", url="https://t.me/USER_BOT?startgroup=true"
            ) 
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ قـناة الـسورس ›", url="https://t.me/ah07v"
            )
        ],
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك", url="https://t.me/USER_BOT?startgroup=true"
            ) 
        ],
    ]
    return buttons

## By Anon
close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="🗑حذف", callback_data="close")]]
)


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons



## Queue Markup Anon


def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="كمل",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(text="وقف", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="تخطي", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="ايقاف", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="‹ قـناة الـسورس ›", url="https://t.me/ah07v"
            )
        ],
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك", url="https://t.me/USER_BOT?startgroup=true"
            ) 
        ],
    ]
    return buttons





def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏸ وقف", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▶️ كمل",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏯ تخطي", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⏹ ايقاف", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀️السابق",
                callback_data=f"Pages Back|0|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 رجوع",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶التالي️",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔇 كتم", callback_data=f"ADMIN Mute|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🔊 الغاءالكتم",
                callback_data=f"ADMIN Unmute|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔀 عشوائي",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔁 ترتيب", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀السابق️",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 رجوع",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶التالي️",
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏮ رجوع10ثواني",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ تقدم10ثواني",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏮ رجوع30ثانيه",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ تقدم30ثانيه",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◀السابق️",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔙 رجوع",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="▶التالي️",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons
