import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VIPMUSIC import LOGGER, app, userbot
from VIPMUSIC.core.call import VIP
from VIPMUSIC.misc import sudo
from VIPMUSIC.plugins import ALL_MODULES
from VIPMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐀𝐁𝐄 𝐑𝐀𝐍𝐃𝐈 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄 𝐄𝐃𝐈𝐓 𝐊𝐀𝐑 𝐋𝐀𝐈 𝐍𝐀 𝐑𝐄𝐏𝐎 🤬")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VIPMUSIC.plugins" + all_module)
    LOGGER("VIPMUSIC.plugins").info("𝐁𝐀𝐂𝐊 𝐁𝐇𝐄𝐍𝐂𝐇𝐎𝐃 𝐀𝐁 𝐍𝐇𝐈.𝐂𝐇𝐀𝐋𝐄 𝐆𝐀 🖕🏻 ...")
    await userbot.start()
    await VIP.start()
    await VIP.decorators()
    LOGGER("VIPMUSIC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝐌𝐀𝐃𝐄 𝐁𝐘 𝐓𝐄𝐀𝐌 𝐇𝐔𝐍𝐓𝐄𝐑♨️\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("VIPMUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝐌𝐀𝐃𝐄 𝐁𝐘 𝐓𝐄𝐀𝐌 𝐇𝐔𝐍𝐓𝐄𝐑♨️\n╚═════ஜ۩۞۩ஜ════╝")
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
