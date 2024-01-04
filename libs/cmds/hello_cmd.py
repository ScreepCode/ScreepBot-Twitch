from twitchAPI.chat import ChatCommand


# this will be called whenever the one of the commands is issued
# hi, hello, hallo
async def hello_command(cmd: ChatCommand):
    await cmd.reply(f'Hello World! from {cmd.user.display_name}')
