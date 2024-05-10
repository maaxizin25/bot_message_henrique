from pyrogram import Client
from pyrogram.raw.types import UpdatePendingJoinRequests
from pyrogram.raw.types import ChannelParticipantsRecent

api_id = 25981977
api_hash = "82cf4c60a901e63931b0f612c083e613"


app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_raw_update()
def handler(client, update, users, chats):
    if isinstance(update, UpdatePendingJoinRequests):
        users_request = update.recent_requesters
        for requester in users_request:
            client.approve_chat_join_request(chat_id=-1002109502961, user_id=requester)
            print()

app.run()