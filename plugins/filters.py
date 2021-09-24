#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import re

from pyrogram import (
    filters,
    Client
)

from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Message,
    CallbackQuery
)

from bot import Bot
from script import script
from config import MAINCHANNEL_ID


 
@Client.on_message(filters.group & filters.text)
async def filter(client: Bot, message: Message):
    if re.findall("((^\/|^,|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return

    if len(message.text) > 2:    
        buttons = []
        async for msg in client.USER.search_messages(MAINCHANNEL_ID,query=message.text,filter='document',limit=10):
            file_name = msg.document.file_name
            msg_id = msg.message_id                     
            link = msg.link
            buttons.append(
                [InlineKeyboardButton(text=f"{file_name}",url=f"{link}")]
            )
        if not buttons:
            return
        
        buttons.append(
            [InlineKeyboardButton(text=f"NEXT ⏩",callback_data="next1")]
        )

        await message.reply_text(
            f"<b> Here is the result for {message.text}</b>",
            reply_markup=InlineKeyboardMarkup(buttons)
        )



@Client.on_callback_query()
async def cb_handler(client: Bot, query:CallbackQuery):
    if query.message.reply_to_message.from_user.id == query.from_user.id:
        if query.data == "back1":
            try:
                buttons = []
                async for msg in client.USER.search_messages(MAINCHANNEL_ID,query=query.message.reply_to_message.text,filter='document',limit=10,offset=0):
                    name = msg.document.file_name
                    link = msg.link
                    buttons.append([InlineKeyboardButton(text=f"{name}",url=link)])
       
                if buttons:
                    buttons.append(
                        [InlineKeyboardButton(text=f"NEXT ⏩",callback_data="next1")]
                    )
                    
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
            except:
                await query.answer("No more results found",show_alert=True)

        elif (query.data == "next1") or (query.data == "back2"):
            try:
                buttons = []
                async for msg in client.USER.search_messages(MAINCHANNEL_ID,query=query.message.reply_to_message.text,filter='document',limit=10,offset=10):
                    name = msg.document.file_name
                    link = msg.link
                    buttons.append([InlineKeyboardButton(text=f"{name}",url=link)])
       
                if buttons:
                    buttons.append(
                        [InlineKeyboardButton(text=f"⏪ BACK",callback_data="back1"),
                            InlineKeyboardButton(text=f"NEXT ⏩",callback_data="next2")]
                    )
                    
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
            except:
                await query.answer("No more results found",show_alert=True)


        elif (query.data == "next2") or (query.data == "back3"):
            try:
                buttons = []
                async for msg in client.USER.search_messages(MAINCHANNEL_ID,query=query.message.reply_to_message.text,filter='document',limit=10,offset=20):
                    name = msg.document.file_name
                    link = msg.link
                    buttons.append([InlineKeyboardButton(text=f"{name}",url=link)])
     
                if buttons:
                    buttons.append(
                        [InlineKeyboardButton(text=f"⏪ BACK",callback_data="back2"),
                            InlineKeyboardButton(text=f"NEXT ⏩",callback_data="next3")]
                    )
                    
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
            except:
                await query.answer("No more results found",show_alert=True)


        elif (query.data == "next3") or (query.data == "back4"):
            try:
                buttons = []
                async for msg in client.USER.search_messages(MAINCHANNEL_ID,query=query.message.reply_to_message.text,filter='document',limit=10,offset=30):
                    name = msg.document.file_name
                    link = msg.link
                    buttons.append([InlineKeyboardButton(text=f"{name}",url=link)])
     
                if buttons:
                    buttons.append(
                        [InlineKeyboardButton(text=f"⏪ BACK",callback_data="back3"),
                            InlineKeyboardButton(text=f"NEXT ⏩",callback_data="next4")]
                    )
                    
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
            except:
                await query.answer("No more results found",show_alert=True)
                

        elif query.data == "next4":
            try:
                buttons = []
                async for msg in client.USER.search_messages(MAINCHANNEL_ID,query=query.message.reply_to_message.text,filter='document',limit=10,offset=40):
                    name = msg.document.file_name
                    link = msg.link
                    buttons.append([InlineKeyboardButton(text=f"{name}",url=link)])
     
                if buttons:
                    buttons.append(
                        [InlineKeyboardButton(text=f"⏪ BACK",callback_data="back4")]
                    )
                    
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
            except:
                await query.answer("No more results found",show_alert=True)

        elif query.data == "start_data":

            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("HELP", callback_data="help_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data")],
                [InlineKeyboardButton("⭕️ JOIN OUR CHANNEL ⭕️", url="https://t.me/TroJanzHEX")]
            ])

            await query.message.edit_text(
                script.START_MSG.format(query.from_user.mention),
                reply_markup=keyboard,
                disable_web_page_preview=True
            )

        elif query.data == "help_data":

            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("BACK", callback_data="start_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data")],
                [InlineKeyboardButton("⭕️ SUPPORT ⭕️", url="https://t.me/TroJanzSupport")]
            ])

            await query.message.edit_text(
                script.HELP_MSG,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )

        elif query.data == "about_data":

            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("BACK", callback_data="help_data"),
                    InlineKeyboardButton("START", callback_data="start_data")],
                [InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Auto-Filter-Bot")]
            ])

            await query.message.edit_text(
                script.ABOUT_MSG,
                reply_markup=keyboard,
                disable_web_page_preview=True
            )

    else:
        await query.answer("Thats not for you!!",show_alert=True)