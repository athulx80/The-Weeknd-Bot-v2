class script(object):
    START_TXT = """<b>𝖧𝖾𝗒 {},
𝖬𝗒 𝖭𝖺𝗆𝖾 𝗂𝗌 <a href=https://t.me/{}>{}</a>, 𝖨 𝖼𝖺𝗇 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌, 𝗃𝗎𝗌𝗍 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖺𝗇𝖽 𝖬𝖺𝗄𝖾 𝗆𝖾 𝖠𝖽𝗆𝗂𝗇...</b>"""
    
    HELP_TXT = """<b>𝖧𝖾𝗒 {},
𝗁𝖾𝗋𝖾 𝗂𝗌 𝗆𝗒 𝗁𝖾𝗅𝗉 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌.</b>"""


# ⚠️ Please don't change our source code 👇🏻

    ABOUT_TXT = """➲ 𝖬𝗒 𝖭𝖺𝗆𝖾 : {}
➲ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href=https://t.me/athulx80>𝖠𝗍𝗁𝗎𝗅</a>
➲ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : <a href=https://docs.pyrogram.org/>𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆</a>
➲ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <a href='https://www.python.org/download/releases/3.0/'>𝖯𝗒𝗍𝗁𝗈𝗇</a>
➲ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href=https://www.mongodb.com/>𝖬𝗈𝗇𝗀𝗈𝖣𝖡</a>
➲ 𝖡𝗈𝗍 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖠𝗇𝗒𝗐𝖾𝗋𝖾
➲ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : 𝗏𝟤.𝟢.𝟥 [ Sᴛᴀʙʟᴇ ]"""

    SOURCE_TXT = """<b>⭕ NOTE:</b>

<b><i>-Sorry this is an open source project!</i></b>"""

    MANUELFILTER_TXT = """Help: <b>FILTERS</b>
- 𝖥𝗂𝗅𝗍𝖾𝗋 𝗂𝗌 𝗍𝗁𝖾 𝖿𝖾𝖺𝗍𝗎𝗋𝖾𝗌 𝗐𝖾𝗋𝖾 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝗌𝖾𝗍 𝖠𝗎𝗍𝗈𝗆𝖺𝗍𝖾𝖽 𝖱𝖾𝗉𝗅𝗂𝖾𝗌 𝖿𝗈𝗋 𝖺 𝖯𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝖪𝖾𝗒𝖻𝗈𝖺𝗋𝖽 𝖺𝗇𝖽 𝖡𝖮𝖳 𝗐𝗂𝗅𝗅 𝖱𝖾𝗌𝗉𝗈𝗇𝖽 𝗐𝗁𝖾𝗇𝖾𝗏𝖾𝗋 𝖺 𝖪𝖾𝗒𝖻𝗈𝖺𝗋𝖽 𝗂𝗌 𝖿𝗈𝗎𝗇𝖽 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾.

<b>⭕ NOTE:</b>
<b>1.⚙️ BOT should have Admin privilege.
2.⚙️ Only Admins can Add filters in a chat.
3.⚙️ Alert Buttons have a limited of 64 Characters.</b>

<b>Commands & Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>BUTTONS</b>

𝖨 𝖼𝖺𝗇 𝖲𝗎𝗉𝗉𝗈𝗋𝗍𝗌 𝖻𝗈𝗍𝗁 𝖴𝖱𝖫 𝖺𝗇𝖽 𝖠𝗅𝖾𝗋𝗍 𝖨𝗇𝗅𝗂𝗇𝖾 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 ♥️

<b>⭕ NOTE:</b>
<b>1. Telegram will not allows you to send Buttons without any Content, So content is Mandatory.
2. Bot supports Buttons with any Telegram Media type.
3. Buttons should be properly parsed as Markdown Format</b>
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https:xxxxxxxxxxxx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>AUTO FILTER</b>

<b>⭕ NOTE:</b>
<b>1. Make me Admin of your Channel if it's Private.
2. Make sure that your Channel does not Contain CamRips, Porn and Fake Files.
3. Forward the Last Massage to me with Quotes. I'll Add the Files in that Channel to my DB.</b>

<b>Commands and Usage:</b>
<b>/set_template - Custom IMDb Template For Auto Filter.</b>
<b>/get_template - Get current IMDB Template of Auto Filter.</b>
<b>/autofilter on - Enable Auto Filter in the Groups.</b>
<b>/autofilter off - Disabled Auto Filter in the Groups.</b>"""

    CONNECTION_TXT = """Help: <b>CONNECTIONS</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>⭕ NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands & Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>EXTRA MODULES</b>

<b>⭕ NOTE:</b>
these are the extra features of The Weeknd Bot

<b>Commands & Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    SONG_TXT = """<b>SONG DOWNLOAD MODULE</b>

<i>Song Download Module, For those who Love Music. You can use this Feature for Download any Song with Super fast Speed. Works only on Groups..!/</i>
<b>COMMANDS</b>

⏭️ /song Song Name

<b>Works both Group and PM!</b>
© @MEmpire_Official"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.
• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/example...)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/example...</code>
<code>/video https://youtu.be/example...</code>"""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>
Translate text to speech
<b>Commands and Usage:</b>
• /tts <text> : convert text to speech"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
✒️ /telegraph - Send me Picture or Vide Under (5MB)

<b>⭕ NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽
This Command helps you to know daily Information about COVID-19

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /covid - Use this Command with your Cuntry Name to get COVID Information.
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid India</code>

⚠️ This service has been stopped!"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
You can Convert a PDF file to a Audio file with this Command ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /audiobook: Reply this Command to any PDF to Generate the Audio"""

    DEPLOY_TXT= """𝙸𝙵 𝚈𝙾𝚄 𝙵𝙰𝙲𝙸𝙽𝙶 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴 𝙸𝙽 𝚃𝙷𝙴 𝚁𝙴𝙿𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴..."""
   
    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 🚶🏼‍♂️
<b>Commands:</b>
• /alive - To check you are alive.
• /help - To get help.

• /ping - <b>To get your ping.</b>

<b>🛠️Usage🛠️ :</b>
• This commands can be used in pm and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
 
    STICKER_TXT = """<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.</b>
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""

    FONT_TXT= """⚙️ 𝐔𝐒𝐀𝐆𝐄

𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 

<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>

 <i>This feature added by @𝙲𝚉𝙳 𝙱𝙾𝚃𝚉"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- <b>Give a user details</b>

•/whois :-give a user full details 📑"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""

    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶'𝚂 ⚡</b>
 
1. /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
2. /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
3. /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
4. /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
5. /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>⭕ NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all groups</code>
• /gfilter - <code>group filter</code>
• /setskip - <code>skip no of files before indexing</code>"""
    
    STATUS_TXT = """<b>★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b>"""

    CARB_TXT = """<b>Help</b> : 𝗖𝗔𝗥𝗕𝗢𝗡
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""


    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""


    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""


    FILE_MSG = """
<b>Hey 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <code>{}</code>              
                       
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Hey 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>കോപ്പിറൈറ്റ് ഉള്ളതുകൊണ്ട് ഫയൽ 10 മിനിറ്റിനുള്ളിൽ ഇവിടെനിന്നും ഡിലീറ്റ് ആകുന്നതാണ് അതുകൊണ്ട് ഇവിടെ നിന്നും മറ്റെവിടെക്കെങ്കിലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക!</b>

<b>© Powered by {}</b>
"""
    SUR_TXT = """
<b>
𝙷𝙴𝙻𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 
</b>
"""

    IMDB_TEMPLATE_TXT = """
<b>📺 ᴛɪᴛʟᴇ :<a href={url}>{title}</a>

🎭 ɢᴇɴʀᴇꜱ : {genres}
⭐ ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)

🗓️ ʏᴇᴀʀ : {release_date}
🎙️ ʟᴀɴɢᴜᴀɢᴇ : {languages}
🌐 ᴄᴏᴜɴᴛʀʏ : {countries}
📑 ꜱᴛᴏʀʏ : {plot} 

©{message.chat.title}</b>
"""

    CUSTOM_FILE_CAPTION = """<b>📂ꜰɪʟᴇ ɴᴀᴍᴇ : {file_name}

╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
▫️<a href=https://t.me/+L8SWfrF_7m04ODZl> ᴄʜᴀɴɴᴇʟ </a>
▫️<a href=https://t.me/+hC5tRAvQHHplMWQ1> ɢʀᴏᴜᴘ </a>
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</b>""" 

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>"""



    MELCOW_ENG = """<b>Hey {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    ALRT_TXT = """𝚃𝙷𝙰𝚃 𝙸𝚂 𝙽𝙾𝚃 𝙵𝙾𝚁 𝚈𝙾𝚄 𝚂𝙸𝚁 @ᴄᴢᴅ ʙᴏᴛᴢ​"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧 @ᴄᴢᴅ ʙᴏᴛᴢ​"""

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>𝚃𝙷𝙸𝚂 𝙼𝙾𝚅𝙸𝙴 I𝚂 𝙽𝙾𝚃 𝚈𝙴𝚃 𝚁𝙴𝙻𝙴𝙰𝚂𝙴𝙳 𝙾𝚁 𝙰𝙳𝙳𝙴𝙳 𝚃𝙾 𝙳𝙰𝚃𝚂𝙱𝙰𝚂𝙴</b> """

    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>
©𝐌𝐎𝐕𝐈𝐄𝐒 𝐄𝐌𝐏𝐈𝐑𝐄"""

    I_CUDNT = """𝑯𝑬𝑳𝑳𝑶 {} 𝑰 𝑪𝑶𝑼𝑳𝑫𝑵'𝑻 𝑭𝑰𝑵𝑫 𝑨𝑵𝒀 𝑴𝑶𝑽𝑰𝑬 𝑰𝑵 𝑻𝑯𝑨𝑻 𝑵𝑨𝑴𝑬 ."""

    I_CUD_NT = """𝑯𝑬𝑳𝑳𝑶 {} 𝑰 𝑪𝑶𝑼𝑳𝑫𝑵'𝑻 𝑭𝑰𝑵𝑫 𝑨𝑵𝒀𝑻𝑯𝑰𝑵𝑮 𝑹𝑬𝑳𝑨𝑻𝑬𝑫 𝑻𝑶 𝑻𝑯𝑨𝑻 . 𝑪𝑯𝑬𝑪𝑲 𝒀𝑶𝑼𝑹 𝑺𝑷𝑬𝑳𝑳𝑰𝑵𝑮."""
    
    CUDNT_FND = """𝑯𝑬𝑳𝑳𝑶 {} 𝑰 𝑪𝑶𝑼𝑳𝑫𝑵'𝑻 𝑭𝑰𝑵𝑫 𝑨𝑵𝒀𝑻𝑯𝑰𝑵𝑮 𝑹𝑬𝑳𝑨𝑻𝑬𝑫 𝑻𝑶 𝑻𝑯𝑨𝑻 𝑫𝑰𝑫 𝒀𝑶𝑼 𝑴𝑬𝑨𝑵 𝑨𝑵𝒀 𝑶𝑵𝑬 𝑶𝑭 𝑻𝑯𝑬𝑺𝑬?"""
    
    REPRT_MSG = """ Reported To Admin"""
