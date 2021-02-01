from typing import Union, List, Optional
from botapi import app, sessions
import json 
from pyrogram import types

@app.get('/copymsg')
@app.post('/copymsg')
async def copy_message(
        token: str,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        caption: str = None,
        parse_mode: Optional[str] = object,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        schedule_date: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None
    ) -> List["types.Message"]:
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.copy_message(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            caption=caption,
            parse_mode=parse_mode,
            disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id,
            schedule_date=schedule_date,
            reply_markup=reply_markup
            )
    except Exception as err:
        return {
            "error": str(err)
        }
    return json.loads(str(c))

