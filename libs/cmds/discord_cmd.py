from twitchAPI.chat import ChatCommand
from libs.data import get_relevant_information


# this will be called whenever the one of the commands is issued
# dc, discord
async def discord_command(cmd: ChatCommand):
    json_data = get_relevant_information("discord")
    link = json_data["invite-link"]

    await cmd.reply(f"Link zu meinem Community Discord: {link} ^^")
