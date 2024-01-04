from twitchAPI.chat import ChatCommand

from libs.data import get_relevant_information


# this will be called whenever the one of the commands is issued
# projekt, project
async def project_command(cmd: ChatCommand):
    json_data = get_relevant_information("project")
    text = json_data["text"]
    link = json_data["link"]
    link_text = json_data["link-text"]

    await cmd.reply(f"{text} {link_text} {link}" if link != "" else text)
