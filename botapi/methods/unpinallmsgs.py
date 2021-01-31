from typing import Union
from botapi import app, sessions
import json 


@app.get('/unpinallmsgs')
@app.post('/unpinallmsgs')
async def unpin_all_chat_messages(token: str, chat_id: Union[int, str]):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.unpin_all_chat_messages(chat_id)
    except Exception as err:
        return {
            "error": str(err)
        }
    else:
     return {
            "True": str(c)
        }



