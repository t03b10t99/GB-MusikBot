from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

GROUP_MUSIC_PROBOT_IMG= "https://telegra.ph/file/c03f733d6db058a48098f.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GROUP_MUSIC_PROBOT_IMG)
    await message.reply_text(
        f"""**👋🏻 Hai, Saya {bn} 🎵

Bot musik adalah bot sumber terbuka yang memungkinkan Anda memutar musik di grup telegram Anda.
Tidak mengetahui cara memakainya? Baca ᴘᴀɴᴅᴜᴀɴ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ agar langsung memahami tanpa bertanya!
─────────────────────
Kutipan: "Ada waktunya kita akan terpuruk dan menangis.
Tapi Percayalah di setiap tangis pasti akan ada kebahagiaan yang akan datang"
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 ᴋᴏᴅᴇ ʀᴇᴘᴏ 🛠", url="https://github.com/comingsoon")
                  ],[
                    InlineKeyboardButton(
                        "🧾 ᴘᴀɴᴅᴜᴀɴ", url="https://t.me/Hindi_K_drama_1"
                    ),
                    InlineKeyboardButton(
                        " ᴅᴏɴᴀsɪ 🎁", url="https://saweria.co/DonasiUntukAdmin"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "👑 ᴏᴡɴᴇʀ ɢʙ | ᴍᴜsɪᴋ ʙᴏᴛ 👑", url="http://t.me/GB_03101999"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "➕ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜᴘ ➕", url="https://t.me/GB_MusikBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ {bn} sudah aktif\nSaya siap memutar musik yang anda inginkan**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑 ᴏᴡɴᴇʀ ɢʙ | ᴍᴜsɪᴋ ʙᴏᴛ 👑", url="http://t.me/GB_03101999")
                ]
            ]
        )
   )
