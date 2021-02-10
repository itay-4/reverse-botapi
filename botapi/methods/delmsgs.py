from typing import Union
from botapi import app, sessions
import json 


@app.get('/delmsgs')
@app.post('/delmsgs')
async def delete_messages(token: str, chat_id: Union[int, str], message_ids: int):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.delete_messages(chat_id, message_ids)
    except Exception as err:
        return {
            "error": str(err)
        }
    else:
     return {
            "True": str(c)
        }

      
