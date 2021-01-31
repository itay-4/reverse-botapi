from typing import Union
from botapi import app, sessions
import json 


@app.get('/unpinmsg')
@app.post('/unpinmsg')
async def unpin_chat_message(token: str, chat_id: Union[int, str], message_id: int):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.unpin_chat_message(chat_id, message_id)
    except Exception as err:
        return {
            "error": str(err)
        }
    else:
     return {
            "True": str(c)
        }



