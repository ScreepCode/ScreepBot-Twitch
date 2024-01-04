from twitchAPI.chat import ChatCommand

from libs.data import get_relevant_information


# this will be called whenever the one of the commands is issued
# prime, twitchprime, primegaming
async def prime_command(cmd: ChatCommand):
    await cmd.reply(get_prime_text())


def get_prime_text() -> str:
    json_data = get_relevant_information("prime")
    text = json_data["text"]
    return text