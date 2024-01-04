import threading
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent, TwitchAPIException
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
from flask import Flask, redirect, request
import asyncio
import time
import os

from bellman_manager import Bellman
from command_manager import CommandManager

APP_ID = os.environ.get("Twitch_Client_ID")
APP_SECRET = os.environ.get("Twitch_Secret")
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
MY_URL = 'http://localhost:5000/login/confirm'
TARGET_CHANNEL = 'ScreepCode'

app = Flask(__name__)
twitch: Twitch
auth: UserAuthenticator


class ScreepBot:
    global twitch, auth
    chat: Chat

    def __init__(self) -> None:
        self.await_login = True

        self.CommandManager = None
        self.Bellman = None


    # this will be called when the event READY is triggered, which will be on bot start
    async def on_ready(self, ready_event: EventData):
        print('Bot is ready for work, joining channels')
        # join our target channel, if you want to join multiple, either call join for each individually
        # or even better pass a list of channels as the argument
        await ready_event.chat.join_room(TARGET_CHANNEL)
        # you can do other bot initialization things in here

    # this will be called whenever a message in a channel was send by either the bot OR another user
    async def on_message(self, msg: ChatMessage):
        print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')
        await self.Bellman.increment()

    # this will be called whenever someone subscribes to a channel
    async def on_sub(self, sub: ChatSub):
        print(f'New subscription in {sub.room.name}:\n'
              f'  Type: {sub.sub_plan}\n'
              f'  Message: {sub.sub_message}')

    # this is where we set up the bot
    async def run(self):
        global twitch, auth, app
        # set up twitch api instance and add user authentication with some scopes
        twitch = await Twitch(APP_ID, APP_SECRET)
        auth = UserAuthenticator(twitch, USER_SCOPE, url=MY_URL)

        while self.await_login:
            time.sleep(2)
            print("Still waiting")

        # create chat instance
        self.chat = await Chat(twitch)

        # register the handlers for the events you want

        # listen to when the bot is done starting up and ready to join channels
        self.chat.register_event(ChatEvent.READY, self.on_ready)
        # listen to chat messages
        self.chat.register_event(ChatEvent.MESSAGE, self.on_message)
        # listen to channel subscriptions
        self.chat.register_event(ChatEvent.SUB, self.on_sub)
        # there are more events, you can view them all in this documentation

        # register all available commands
        self.CommandManager = CommandManager(self.chat)
        self.CommandManager.register_commands()

        # register bellman
        self.Bellman = Bellman(self.chat, TARGET_CHANNEL)

        # we are done with our setup, lets start this bot up!
        self.chat.start()

        # lets run till we press enter in the console
        try:
            input('press ENTER to stop\n')
        finally:
            # now we can close the chat bot and the twitch api client
            self.chat.stop()
            await twitch.close()


chat_bot: ScreepBot


@app.route('/login')
def login():
    return redirect(auth.return_auth_url())


@app.route('/login/confirm')
async def login_confirm():
    global chat_bot
    state = request.args.get('state')
    if state != auth.state:
        return 'Bad state', 401
    code = request.args.get('code')
    if code is None:
        return 'Missing code', 400
    try:
        token, refresh = await auth.authenticate(user_token=code)

        if chat_bot.await_login:
            await twitch.set_user_authentication(token, USER_SCOPE, refresh)
            print("Authentifiziert")
            chat_bot.await_login = False
    except TwitchAPIException as e:
        return 'Failed to generate auth token', 400
    return 'Sucessfully authenticated!'


def main():
    app.run('0.0.0.0', 5000)
    # lets run our setup


if __name__ == "__main__":
    chat_bot = ScreepBot()
    thread = threading.Thread(target=main)
    thread.start()
    asyncio.run(chat_bot.run())
