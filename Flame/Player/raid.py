
import asyncio
import base64
import os
import random        
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from Flame.data import RAID, REPLYRAID, FLAMESPAM, PORMS, SHAYRI
from Flame.main import BOT
from config import SUDO_USERS

OWNER_ID = SUDO_USERS
que = {}
hl = '/'


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sshayri(?: |$)(.*)" % hl))
async def spam(e):
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ= sʜᴀʏʀɪ\n\nCommand:\n\n.shayri<count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Deadly) == 2:
            user = str(Deadly[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in Deadly:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_OFFICIAL_MP0 ᴏᴡɴᴇʀ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ govind ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Deadly[0])
                for _ in range(counter):
                    reply = random.choice(SHAYRI)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in DHIMANSPAM:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_OFFICIAL_MP0 ᴏᴡɴᴇʀ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ govind ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Deadly[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(SHAYRI)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@BOT.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sporms(?: |$)(.*)" % hl))
async def spam(e):
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴘᴏʀᴍs\n\nCommand:\n\n.porms <count> <Username of User>\n\n.porms <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Deadly) == 2:
            user = str(Deadly[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DHIMANSPAM :
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_OFFICIAL_MP0 ᴏᴡɴᴇʀ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ GOVIND ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Deadly[0])
                for _ in range(counter):
                    reply = random.choice(PORMS)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in DHIMANSPAM:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_USERBOT_SPPORT ᴏᴡɴᴇʀ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ govind ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Deadly[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(PORMS)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@BOT.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYPORMS)),
            reply_to=event.message.id,
        )

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ʀᴀɪᴅ\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Deadly) == 2:
            user = str(Deadly[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DHIMANSPAM:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @DhimanBots ᴏᴡɴᴇʀ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ govind ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Deadly[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in DHIMANSPAM:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_OFFICIAL_MP0 ᴏᴡɴᴇʀ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ govind ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Deadly[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@BOT.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ʀᴇᴘʟʏ ʀᴀɪᴅ\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        SAMx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Deadly[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in Deadly:
                text = f" ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_OFFICIAL_MP0 ᴏᴡɴᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ govind ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in DHIMANSPAM:
                text = f" ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_USERBOT_SPPORT ᴏᴡɴᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ Govind ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ.."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Deadly[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
async def _(event):
   usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴅᴇʟᴀʏʀᴀɪᴅ\n\nCommand:\n\n.delayraid <delay> <count> <Username of User>\n\n.delayraid <delay> <count> <reply to a User>\n\nCount and Sleeptime must be a integer."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Deadly = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Deadly) == 3:
             user = str(Deadly[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in DHIMANSPAM:
                    text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_USERBOT_SPPORT ᴏᴡɴᴇʀ"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) == OWNER_ID:
                text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ ᴅʜɪᴍᴀɴ ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Deadly[1])
                 sleeptimet = sleeptimem = float(Deadly[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in DHIMANSPAM:
                       text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ @GOVIND_OFFICIAL_MP0 ᴏᴡɴᴇʀ"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) == OWNER_ID:
                       text = f"ʙᴇʜɴ ᴋᴇ ʟᴏᴅᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ ᴅʜɪᴍᴀɴ ᴘᴇ ʜɪ ʀᴀɪᴅ ʟɢᴀʏᴇɢᴀ ( ᴊɪs ᴛʜᴀᴀʟɪ ᴍᴇ ᴋʜᴀʏᴀ ᴜsɪ ᴍᴇ ᴄʜʜᴇᴀᴅ ) sᴇᴅ <3."
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Deadly[0])
                   counter = int(Deadly[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)
