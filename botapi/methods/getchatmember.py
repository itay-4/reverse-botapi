from typing import Union
from botapi import app, sessions
import json 


@app.get('/getchatmember')
@app.post('/getchatmember')
async def get_chat_member(token: str, chat_id: Union[int, str], user_id: Union[int, str]):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.get_chat_member(chat_id, user_id)
    except Exception as err:
        return {
            "error": str(err)
        }
    return json.loads(str(c))
