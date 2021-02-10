from typing import Union
from botapi import app, sessions
import json 


@app.get('/forwardmsgs')
@app.post('/forwardmsgs')
async def forward_messages(token: str, chat_id: Union[int, str], from_chat_id: Union[int, str], message_ids: int, disable_notification: bool = None):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.forward_messages(chat_id=chat_id, from_chat_id=from_chat_id, message_ids=message_ids, disable_notification=disable_notification)
    except Exception as err:
        return {
            "error": str(err)
        }
    else:
     return {
            "True": str(c)
        }

      
