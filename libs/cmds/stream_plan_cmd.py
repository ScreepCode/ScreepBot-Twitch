from twitchAPI.chat import ChatCommand

from libs.data import get_relevant_information


# this will be called whenever the one of the commands is issued
# streamplan, schedule
async def stream_plan_command(cmd: ChatCommand):
    json_data = get_relevant_information("stream-plan")
    text = json_data["text"]

    await cmd.reply(f"{cmd.user.display_name} {text}")
