import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import urllib.parse
import yt_dlp
import cloudscraper
import m3u8
import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pytube import YouTube
from aiohttp import web
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging = logging.getLogger()

# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

my_name = "Mr_X45"

cookies_file_path = os.getenv("COOKIES_FILE_PATH", "/modules/youtube_cookies.txt")

def pwdlx_video(url: str, output_filename: str):
    cmd = [
        "yt-dlp",
        "--newline",
        "--merge-output-format", "mp4",
        "--remux-video", "mp4",
        "--concurrent-fragments", "8",
        "--downloader", "aria2c",
        "--downloader-args", "aria2c:-x16 -s16 -k1M -j16 --file-allocation=none",
        "-o", output_filename,
        url,
    ]
    subprocess.run(cmd, check=True)
    return output_filename

def extract_content_id(url):
    try:
        if "contentId=" in url:
            parts = url.split("contentId=")
            if len(parts) > 1:
                content_id = parts[1]
                for char in ["?", "&"]:
                    if char in content_id:
                        content_id = content_id.split(char)[0]
                if content_id.endswith(".m3u8"):
                    content_id = content_id[:-5]
                elif ".m3u8" in content_id:
                    content_id = content_id.split(".m3u8")[0]
                return content_id
        return None
    except Exception as e:
        return None

def get_jw_signed_url(content_id, access_token):
    url = f"https://api.classplusapp.com/cams/uploader/video/jw-signed-url?contentId={urllib.parse.quote(content_id, safe='')}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en",
        "Origin": "https://web.classplusapp.com",
        "Referer": "https://web.classplusapp.com/",
        "Region": "IN",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/139.0.0.0 Safari/537.36",
        "X-Access-Token": access_token,
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        data = response.json()
        return data.get("url")
    except Exception as e:
        return None

# Define aiohttp routes
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("https://pw-downloader-bot.onrender.com/")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    await start_bot()
    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()

# 🌟 PREMIUM BOLD START COMMAND
@bot.on_message(filters.command("start"))
async def start(client: Client, msg: Message):
    user = await client.get_me()
    
    start_msg = (
        f"╭───❮ **MR_X45 BATCH EXTRACTOR** ❯───►\n"
        f"│\n"
        f"├──» **WELCOME:** {msg.from_user.mention}\n"
        f"├──» **STATUS:** **INITIALIZING UPLOADER BOT...** 🤖⚡\n"
        f"├──» **PROGRESS:** `[⬜⬜⬜⬜⬜⬜⬜⬜⬜]` **0%**\n"
        f"│\n"
        f"╰───╭⚡ **POWERED BY MR_X45** ⚡╯───►"
    )
    start_message = await client.send_message(msg.chat.id, start_msg)

    await asyncio.sleep(1)
    await start_message.edit_text(
        f"╭───❮ **MR_X45 BATCH EXTRACTOR** ❯───►\n"
        f"│\n"
        f"├──» **WELCOME:** {msg.from_user.mention}\n"
        f"├──» **STATUS:** **LOADING PREMIUM FEATURES...** ⏳\n"
        f"├──» **PROGRESS:** `[🟥🟥🟥⬜⬜⬜⬜⬜⬜]` **25%**\n"
        f"│\n"
        f"╰───╭⚡ **POWERED BY MR_X45** ⚡╯───►"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        f"╭───❮ **MR_X45 BATCH EXTRACTOR** ❯───►\n"
        f"│\n"
        f"├──» **WELCOME:** {msg.from_user.mention}\n"
        f"├──» **STATUS:** **SIT BACK AND RELAX...** 💪\n"
        f"├──» **PROGRESS:** `[🟧🟧🟧🟧🟧⬜⬜⬜⬜]` **50%**\n"
        f"│\n"
        f"╰───╭⚡ **POWERED BY MR_X45** ⚡╯───►"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        f"╭───❮ **MR_X45 BATCH EXTRACTOR** ❯───►\n"
        f"│\n"
        f"├──» **WELCOME:** {msg.from_user.mention}\n"
        f"├──» **STATUS:** **CHECKING BOT SYSTEM...** 🔍\n"
        f"├──» **PROGRESS:** `[🟨🟨🟨🟨🟨🟨🟨⬜⬜]` **75%**\n"
        f"│\n"
        f"╰───╭⚡ **POWERED BY MR_X45** ⚡╯───►"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        f"╭───❮ **MR_X45 BATCH EXTRACTOR** ❯───►\n"
        f"│\n"
        f"├──» **WELCOME:** {msg.from_user.mention}\n"
        f"├──» **STATUS:** **BOT IS ONLINE & READY!** ✅\n"
        f"├──» **PROGRESS:** `[🟩🟩🟩🟩🟩🟩🟩🟩🟩]` **100%**\n"
        f"│\n"
        f"├──» **CREATOR:** **@rahulx45_vibe**\n"
        f"│\n"
        f"╰───╭⚡ **POWERED BY MR_X45** ⚡╯───►"
    )

@bot.on_message(filters.command(["stop"]))
async def restart_handler(_, m):
    stop_text = (
        f"╭───❮ **WORK TERMINATED** ❯───►\n"
        f"│\n"
        f"├──» **STATUS:** **PROCESS STOPPED BY USER** 🛑\n"
        f"│\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    await m.reply_text(stop_text, quote=True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["Mrx45", "Official"]))
async def txt_handler(bot: Client, m: Message):
    prompt_txt = (
        f"╭───❮ **TXT BATCH LEECHER** ❯───►\n"
        f"│\n"
        f"├──» **SEND TXT FILE TO BEGIN EXTRACTING** 📥\n"
        f"│\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    editable = await m.reply_text(prompt_txt)
    input_msg: Message = await bot.listen(editable.chat.id)
    x = await input_msg.download()
    await input_msg.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = f"@rahulx45_vibe"
    token = f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzYxNTE3MzAuMTI2LCJkYXRhIjp7Il9pZCI6IjYzMDRjMmY3Yzc5NjBlMDAxODAwNDQ4NyIsInVzZXJuYW1lIjoiNzc2MTAxNzc3MCIsImZpcnN0TmFtZSI6IkplZXYgbmFyYXlhbiIsImxhc3ROYW1lIjoic2FoIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sImVtYWlsIjoiV1dXLkpFRVZOQVJBWUFOU0FIQEdNQUlMLkNPTSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTczNTU0NjkzMH0.iImf90mFu_cI-xINBv4t0jVz-rWK1zeXOIwIFvkrS0M"
    
    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            if "://" in i:
                links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Are yaar **txt** file Bhejni thi \n\n **Chal koi na tap on** /Mrx45 **then** \n\n **resend txt file to me again🫂.**")
        if os.path.exists(x):
            os.remove(x)
        return

    # STEP 1: INDEX
    await editable.edit(
        f"╭───❮ **TOTAL LINKS FOUND:** `{len(links)}` ❯───►\n"
        f"│\n"
        f"├──» **ENTER START INDEX:** *(DEFAULT IS 1)*\n"
        f"│\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    try:
        arg = int(raw_text)
    except:
        arg = 1

    # STEP 2: BATCH NAME
    await editable.edit(
        f"╭───❮ **BATCH NAME SETUP** ❯───►\n"
        f"│\n"
        f"├──» **ENTER BATCH NAME** OR SEND `/Rahul`\n"
        f"│\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == '/Rahul':
        b_name = file_name
    else:
        b_name = raw_text0

    # STEP 3: RESOLUTION
    res_menu = (
        f"╭───❮ **SELECT RESOLUTION** ❯───►\n"
        f"├──» **144**\n"
        f"├──» **240**\n"
        f"├──» **360**\n"
        f"├──» **480**\n"
        f"├──» **720**\n"
        f"├──» **1080**\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    await editable.edit(res_menu)
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text.strip()
    await input2.delete(True)
    
    if raw_text2 == "144":
        res = "256x144"
    elif raw_text2 == "240":
        res = "426x240"
    elif raw_text2 == "360":
        res = "640x360"
    elif raw_text2 == "480":
        res = "854x480"
    elif raw_text2 == "720":
        res = "1280x720"
    elif raw_text2 == "1080":
        res = "1920x1080" 
    else: 
        res = "UN"

    # STEP 4: UPLOADER NAME
    await editable.edit(
        f"╭───❮ **CREDITS SETUP** ❯───►\n"
        f"│\n"
        f"├──» **ENTER YOUR NAME** OR SEND `/Rahul`\n"
        f"│\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 in ['/Rahul', '/Cutie', '/Official', '/Love']:
        CR = credit
    else:
        CR = raw_text3

    # STEP 5: TOKEN
    await editable.edit(
        f"╭───❮ **PW TOKEN SETUP** ❯───►\n"
        f"│\n"
        f"├──» **ENTER PW TOKEN** OR SEND `/vip`\n"
        f"│\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await input4.delete(True)
    if raw_text4 in ['/vip', '/X45']:
        access_token = token
    else:
        access_token = raw_text4

    # STEP 6: THUMBNAIL
    await editable.edit(
        f"╭───❮ **THUMBNAIL SETUP** ❯───►\n"
        f"│\n"
        f"├──» **SEND THUMBNAIL URL** OR TYPE `no`\n"
        f"│\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    count = int(raw_text)    
    try:
        for i in range(arg-1, len(links)):

            Vxy = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + Vxy

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'https://contentId=' in url or 'contentHashIdl=' in url:
                content_id = extract_content_id(url)
                cpurl = get_jw_signed_url(content_id, access_token)
                url = cpurl
            
            elif '/master.mpd' in url or "/dash/" in url or ".mp4?" in url or "?Signature=" in url or "d1d34p8vz63oiq.cloudfront.net" in url or "parentId=" in url or "childId=" in url:
                if "parentId=" in url or "childId=" in url:
                    url = f"https://ankitshakyaxapi.vercel.app/download?mpd_url={url}&token={raw_text4}&quality={raw_text2}"
                else:
                    url = f"https://ankitshakyaxapi.vercel.app/download?mpd_url={url}&quality={raw_text2}"
                    
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]} {my_name}'

            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
                
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                # ULTRA BOLD & ELEGANT CAPTION DESIGN
                cc = (
                    f"╭───❮ **MR_X45 LECTURE EXTRACTED** ❯───►\n"
                    f"│\n"
                    f"├──» **ID:** `{str(count).zfill(3)}` \n"
                    f"├──» **TITLE:** **{name1}**\n"
                    f"├──» **QUALITY:** **{raw_text2}p HD**\n"
                    f"├──» **BATCH:** **{b_name}**\n"
                    f"│\n"
                    f"├──» **EXTRACTED BY:** **{CR}**\n"
                    f"│\n"
                    f"╰───╭⚡ **POWERED BY MR_X45** ⚡╯───►"
                )

                cc1 = (
                    f"╭───❮ **MR_X45 DOCUMENT EXTRACTED** ❯───►\n"
                    f"│\n"
                    f"├──» **ID:** `{str(count).zfill(3)}` \n"
                    f"├──» **TITLE:** **{name1}**\n"
                    f"├──» **BATCH:** **{b_name}**\n"
                    f"│\n"
                    f"├──» **EXTRACTED BY:** **{CR}**\n"
                    f"│\n"
                    f"╰───╭⚡ **POWERED BY MR_X45** ⚡╯───►"
                )

                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                        count += 1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        await asyncio.sleep(2)
                        url = url.replace(" ", "%20")
                        scraper = cloudscraper.create_scraper()
                        response = scraper.get(url)

                        if response.status_code == 200:
                            with open(f'{name}.pdf', 'wb') as file:
                                file.write(response.content)

                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1
                            os.remove(f'{name}.pdf')
                        else:
                            await m.reply_text(f"❌ **PDF DOWNLOAD FAILED:** `{response.status_code}`")

                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                else:
                    Show = (
                        f"╭───❮ **DOWNLOADING LECTURE** ❯───►\n"
                        f"│\n"
                        f"├──» **ID:** `{str(count).zfill(3)}` \n"
                        f"├──» **TITLE:** **{name1[:40]}**\n"
                        f"├──» **QUALITY:** **{raw_text2}p**\n"
                        f"│\n"
                        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
                    )
                    prog = await m.reply_text(Show)
                    
                    if '/master.mpd' in url or "/dash/" in url or ".mp4?" in url or "?Signature=" in url or "d1d34p8vz63oiq.cloudfront.net" in url or "parentId=" in url or "childId=" in url:
                        output_filename = f"{name}.mp4"
                        res_file = pwdlx_video(url, output_filename)
                    else:
                        res_file = await helper.download_video(url, cmd, name)

                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"╭───❮ **DOWNLOAD FAILED** ❯───►\n"
                    f"│\n"
                    f"├──» **ID:** `{str(count).zfill(3)}` \n"
                    f"├──» **TITLE:** **{name1[:30]}**\n"
                    f"│\n"
                    f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
                )
                continue

    except Exception as e:
        await m.reply_text(f"❌ **ERROR:** `{str(e)}`")

    done_text = (
        f"╭───❮ **EXTRACTION COMPLETED** ❯───►\n"
        f"│\n"
        f"├──» **ALL LECTURES EXTRACTED SUCCESSFULLY** ✅\n"
        f"│\n"
        f"╰───╭⚡ **MR_X45 STUDIO** ⚡╯───►"
    )
    await m.reply_text(done_text)

bot.run()
