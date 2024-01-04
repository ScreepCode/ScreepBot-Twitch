from twitchAPI.chat import ChatCommand

from libs.data import get_relevant_information


# this will be called whenever the one of the commands is issued
# support, spende, tip
async def support_command(cmd: ChatCommand):
    json_data = get_relevant_information("support")
    text = json_data["text"]
    link = json_data["link"]

    await cmd.reply(text.replace("LINK", link))