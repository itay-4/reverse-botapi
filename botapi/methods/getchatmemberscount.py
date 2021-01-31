from typing import Union
from botapi import app, sessions
import json 


@app.get('/getchatmemberscount')
@app.post('/getchatmemberscount')
async def get_chat_members_count(token: str, chat_id: Union[int, str]):
    try:
        client = await sessions(token)
    except Exception as err:
        return {
            "error": str(err)
        }
    try:
        c = await client.get_chat_members_count(chat_id)
    except Exception as err:
        return {
            "error": str(err)
        }

    else:
     return {
            str(c) + " " + "members"
        }



