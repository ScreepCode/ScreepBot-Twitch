import sys

from twitchAPI.chat import Chat

import libs.cmds


class CommandManager(object):
    def __init__(self, chat):
        self.chat: Chat = chat
        self.commandsModules: list = [
            [["hi", "hello", "hallo"], libs.cmds.hello_command],
            [["echo", "reply"], libs.cmds.echo_command]
        ]

    def register_commands(self):
        for commandModule in self.commandsModules:
            for command in commandModule[0]:
                self.chat.register_command(command, commandModule[1])
