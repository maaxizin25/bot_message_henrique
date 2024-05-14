from pyrogram import Client
from pyrogram.raw.types import UpdatePendingJoinRequests
from pyrogram.raw.types import ChannelParticipantsRecent

api_id = 25424480
api_hash = "5f726d34d6c9708ff35b43069503dbad"


app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_raw_update()
def handler(client, update, users, chats):
    if isinstance(update, UpdatePendingJoinRequests):
        client.approve_all_chat_join_requests(chat_id = -1002048842040)

app.run()