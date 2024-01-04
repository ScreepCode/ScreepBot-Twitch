from twitchAPI.chat import ChatCommand
from libs.data import get_relevant_information


# this will be called whenever the one of the commands is issued
# dc, discord
async def discord_command(cmd: ChatCommand):
    await cmd.reply(get_discord_text())


def get_discord_text() -> str:
    json_data = get_relevant_information("discord")
    link = json_data["invite-link"]
    return f"Link zu meinem Community Discord: {link} ^^"
