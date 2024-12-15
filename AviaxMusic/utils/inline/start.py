from pyrogram.types import InlineKeyboardButton

import config
from AviaxMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍ 𝐀ᴅᴅ 𝐌ᴇ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ❍",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐘ᴏᴜʀ 𝐇ᴇʟᴘᴇʀ ❍", callback_data="settings_back_helper"),
        ],
        [
             InlineKeyboardButton(
                text="❍ 𝐎ᴡɴᴇʀ ❍",
                url=f"https://t.me/ll_SARKAR_OWNER_ll",
            ),
            InlineKeyboardButton(
                text="❍ 𝐀ʟʟ 𝐁ᴏᴛs ❍",
                url=f"https://t.me/PROMOTION_UPDATE/6",
            )
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐏𝐑𝐎𝐌𝐎𝐓𝐈𝐎𝐍 𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 ❍",
                url=f"https://t.me/TG_NAME_STYLE/4602",
            ),
        ],
    ]
    return buttons
