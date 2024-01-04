from twitchAPI.chat import Chat

import random
import sys
import libs.cmds


def generate_threshold(lower=5, upper=20) -> int:
    return random.randrange(lower, upper)


class Bellman(object):
    def __init__(self, chat, target_channel):
        self.chat: Chat = chat
        self.target_channel: str = target_channel

        self.threshold = generate_threshold(lower=10)
        self.counter = 0

        self.messages: list[str] = [
            "Mit einem Follow kannst du mich kostenlos unterstützen und mich ein wenig näher an mein Ziel bringen, zu dem ist es kostenlos ^^",
            libs.cmds.get_discord_text(),
            libs.cmds.get_prime_text(),
            libs.cmds.get_support_text()
        ]

    async def increment(self) -> None:
        self.counter += 1
        if self.counter == self.threshold:
            await self.send_message()
            self.threshold = generate_threshold()

    async def send_message(self) -> None:
        random_line: int = random.randrange(0, len(self.messages))
        await self.chat.send_message(self.target_channel, self.messages[random_line])
