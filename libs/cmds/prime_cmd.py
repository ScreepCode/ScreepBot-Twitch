from twitchAPI.chat import ChatCommand

from libs.data import get_relevant_information


# this will be called whenever the one of the commands is issued
# prime, twitchprime, primegaming
async def prime_command(cmd: ChatCommand):
    json_data = get_relevant_information("prime")
    text = json_data["text"]

    await cmd.reply(text)
