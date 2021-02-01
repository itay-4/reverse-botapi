from typing import Union, Optional
from botapi import app, sessions
import json 
from pyrogram import types

@app.get('/editmessage')
@app.post('/editmessage')
async def edit_message_text(
        token: str,
        chat_id: Union[int, str],
        message_id: int,
        text: str,
        parse_mode: Optional[str] = object,
        disable_web_page_preview: bool = None
    ) -> "types.Message":
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview
            )
    except Exception as err:
        return {
            "error": str(err)
        }
    return json.loads(str(c))

