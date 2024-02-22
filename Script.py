class script(object):
        START_TXT = """<b>Hey {},</b>
    
⪼ This bot will provide Movie/Series.

⪼ Just Send the Movie/Series name with Proper Spelling... in the <a href="https://t.me/MixologyMoviesSeries">Group</a>.

<i>🎦 Tutorial Video » <a href="https://t.me/moviemixologymanager/341">Click Here</a></i>"""

    MY_ABOUT_TXT = """○ Server: <a href=https://www.heroku.com>Heroku</a>
○ Database: <a href=https://www.mongodb.com>MongoDB</a>
○ Language: <a href=https://www.python.org>Python</a>
○ Library: <a href=https://pyrogram.org>Pyrogram</a>"""

    MY_OWNER_TXT = """○ My Name: @MixologyFilterBot
○ Creator: @MovieMixology
○ Updates: @MovieMixologyManager"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
✨ Used Storage: <code>{}</code>
🗳 Free Storage: <code>{}</code>
🚀 Bot Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """<i><b>#NewUser</b></i>
┠ Name: {}
┖ ID: <code>{}</code>"""

    NO_RESULT_TXT = """<i><b>#NoResult</b></i>
┠ Group Name: {}
┠ Group ID: <code>{}</code>
┠ Name: {}
┃
┖ Message: {}"""

    REQUEST_TXT = """★ Name: {}
★ ID: <code>{}</code>

★ Message: {}"""

    NOT_FILE_TXT = """<b>Hey {},</b>

I can't find the <b>'{}'</b> in my database!

<b>1:</b> Google Search and check your spelling is correct.
<b>2:</b> Please read the Instructions to get better results.
<b>3:</b> Or not been released yet.

<b>Report to Admin ▶️ @MixologySupport</b>"""

    DMCA_TXT = """<b>©️ 𝖣𝗂𝗌𝖼𝗅𝖺𝗂𝗆𝖾𝗋:</b>
All the files in this bot are freely available on the internet or posted by somebody else.

This bot is indexing files which are already uploaded on Telegram for ease of searching,
We respect all the copyright laws and works in compliance with DMCA and EUCD.

If anything is against law please contact us so that it can be removed ASAP."""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://onepagelink.in/ref/infinity07>onepagelink.in</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink onepagelink.in f646357aa129cfbd7eb59bcba428096ab54ca950</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """{file_caption}"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """㊂ <i><b>Help Guide Menu!</b></i>

<b>NOTE: </b><i><b>Click on any CMD to see more minor detalis.</b></i>"""
    
    ADMIN_COMMAND_TXT = """⌬ <i><b>Owner or Admins Commands!</b></i>

<b>Bot Settings:</b>
┠ /settings: Change Bot Settings (Group also)
┖ /index: Index files from Bot accessible Channels

<b>Bot Stats:</b>
┠ /chats: Get all Groups
┠ /stats: Get Bot status
┠ /users: All Users Details
┠ /get_custom_settings: Get your Group Settings Details
┖ /index_channels: Check how many index Channel I'd Added

<b>Authentication:</b>
┠ /add_premium: Add User in Premium
┖ /remove_premium: Remove User from Premium

<b>Restrictions:</b>
┠ /unban_grp: Enable Group
┠ /ban_grp: Disable Group
┠ /ban_user: Ban a Users from Bot
┠ /unban_user: Unban a Users from Bot
┖ /leave: Leave your Bot from Particular Group

<b>Broadcast:</b>
┠ /broadcast: Send Message to all Bot Users
┠ /grp_broadcast: Send Message to all Groups
┠ /pin_broadcast: Send Message as Pin to all Bot Users
┖ /pin_grp_broadcast: Send Message as Pin to all Groups

<b>Delete Files:</b>
┠ /delete: Delete files Using Query
┖ /delete_all: Delete all Indexed File

<b>Maintainance:</b>
┖/restart: Restart the Bot"""
    
    USER_COMMAND_TXT = """⌬ <i><b>Users Commands!</b></i>

<b>Details:</b>
┠ /id - Check Group, Channel or User I'd
┠ /my_plan - Check your Plan Details
┖ /plans - Get Plan Details"""

    SOURCE_TXT = """<b>NOTE:</b>
⚠️ 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖨𝗌 𝖭𝗈𝗍 𝖠𝗇 𝖮𝗉𝖾𝗇 𝖲𝗈𝗎𝗋𝖼𝖾 𝖯𝗋𝗈𝗃𝖾𝖼𝗍.!

Thanks To Me For Spending Time For This.

𝖲𝗉𝖾𝖼𝗂𝖺𝗅 𝖳𝗁𝖺𝗇𝗄𝗌 𝖳𝗈 𝖬𝗒 𝖳𝖦 𝖥𝗋𝗂𝖾𝗇𝖽𝗌 𝖳𝗈𝗈.

𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝖽 𝖡𝗒: @MixologyOwnerBot"""
