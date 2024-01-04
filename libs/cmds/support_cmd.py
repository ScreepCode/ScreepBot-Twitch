from twitchAPI.chat import ChatCommand

from libs.data import get_relevant_information


# this will be called whenever the one of the commands is issued
# support, spende, tip
async def support_command(cmd: ChatCommand):
    await cmd.reply(get_support_text())


def get_support_text() -> str:
    json_data = get_relevant_information("support")
    text = json_data["text"]
    link = json_data["link"]
    return text.replace("LINK", link)