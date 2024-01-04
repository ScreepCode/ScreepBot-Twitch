from twitchAPI.chat import ChatCommand


# this will be called whenever the one of the commands is issued
# echo, reply
async def echo_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply('du solltest mir schon was sagen :)')
    else:
        await cmd.reply(f'{cmd.user.display_name}: {cmd.parameter}')
