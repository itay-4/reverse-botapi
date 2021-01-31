from typing import Union
from botapi import app, sessions
import json 


@app.get('/pinmsg')
@app.post('/pinmsg')
async def pin_chat_message(token: str, chat_id: Union[int, str], message_id: int):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.pin_chat_message(chat_id, message_id, both_sides=True)
    except Exception as err:
        return {
            "error": str(err)
        }
    else:
     return {
            "True": str(c)
        }

      
