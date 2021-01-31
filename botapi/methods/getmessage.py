from typing import Union
from botapi import app, sessions
import json 


@app.get('/getmessage')
@app.post('/getmessage')
async def get_messages(token: str, chat_id: Union[int, str], message_ids: int):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.get_messages(chat_id, message_ids)
    except Exception as err:
        return {
            "error": str(err)
        }
    return json.loads(str(c))
