import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from FreakyUserbot import CMD_HELP
from FreakyUserbot.utils import Freaky_on_cmd


@Freaky.on(Freaky_on_cmd(pattern=("sang ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@SangMataInfo_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "The user have enabled privacy settings you cant get name history"
            )
        else:
            await event.edit(f"{response.message.message}")


@Freaky.on(Freaky_on_cmd(pattern=("fakemail ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    chat = "@fakemailbot"
    await event.edit("```Fakemail Creating, wait```")
    async with borg.conversation(chat) as conv:
        try:
            await event.client.send_message("@fakemailbot", "/generate")
            await asyncio.sleep(5)
            k = await event.client.get_messages(
                entity="@fakemailbot", limit=1, reverse=False
            )
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError:
            await event.reply("```Please unblock @fakemailbot and try again```")
            return
        await event.edit(mail)


@Freaky.on(Freaky_on_cmd(pattern=("mailid ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    chat = "@fakemailbot"
    await event.edit("```Fakemail list getting```")
    async with borg.conversation(chat) as conv:
        try:
            await event.client.send_message("@fakemailbot", "/id")
            await asyncio.sleep(5)
            k = await event.client.get_messages(
                entity="@fakemailbot", limit=1, reverse=False
            )
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError:
            await event.reply("```Please unblock @fakemailbot and try again```")
            return
        await event.edit(mail)


@Freaky.on(Freaky_on_cmd(pattern=("ub ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@uploadbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=97342984)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @uploadbot and try again```")
            return
        if response.text.startswith("Hi!,"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


@Freaky.on(Freaky_on_cmd(pattern=("gid ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=186675376)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```you blocked bot```")
            return
        if response.text.startswith("Hello,"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.edit(f"{response.message.message}")


CMD_HELP.update(
    {
        "botfeatures": "**Botfeatures**\
\n\n**Syntax : **`.sang <replying to user message> `\
\n**Usage :** Get Name history of an user.\
\n\n**Syntax : **`.fakemail <type and send in groups or private chats>`\
\n**Usage :** Get a fake email id and get all mails forwarded to you.\
\n\n**Syntax : **`.ub <paste direct download link here>`\
\n**Usage :** Upload any file from direct download link to telegram max file limit 500MB.\
\n\n**Syntax : **`.gid <replying to user message>`\
\n**Usage :** Get user_id of a person."
    }
)
