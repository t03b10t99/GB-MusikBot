from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

GROUP_MUSIC_PROBOT_IMG= "https://telegra.ph/file/c03f733d6db058a48098f.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GROUP_MUSIC_PROBOT_IMG)
    await message.reply_text(
        f"""**ðð» Hai, Saya {bn} ðµ

Bot musik adalah bot sumber terbuka yang memungkinkan Anda memutar musik di grup telegram Anda.
Tidak mengetahui cara memakainya? Baca á´á´É´á´á´á´É´ á´á´É´É¢É¢á´É´á´á´á´É´ Êá´á´ agar langsung memahami tanpa bertanya!
âââââââââââââââââââââ
Kutipan: "Ada waktunya kita akan terpuruk dan menangis.
Tapi Percayalah di setiap tangis pasti akan ada kebahagiaan yang akan datang"
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð  á´á´á´á´ Êá´á´á´ ð ", url="https://github.com/comingsoon")
                  ],[
                    InlineKeyboardButton(
                        "ð§¾ á´á´É´á´á´á´É´", url="https://t.me/Hindi_K_drama_1"
                    ),
                    InlineKeyboardButton(
                        " á´á´É´á´sÉª ð", url="https://saweria.co/DonasiUntukAdmin"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ð á´á´¡É´á´Ê É¢Ê | á´á´sÉªá´ Êá´á´ ð", url="http://t.me/GB_03101999"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "â á´á´á´Êá´Êá´á´É´ á´á´ É¢Êá´á´ â", url="https://t.me/GB_MusikBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**â {bn} sudah aktif\nSaya siap memutar musik yang anda inginkan**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð á´á´¡É´á´Ê É¢Ê | á´á´sÉªá´ Êá´á´ ð", url="http://t.me/GB_03101999")
                ]
            ]
        )
   )
