from pyconar.bot import ConversationBot
from channels.sessions import channel_session


@channel_session
def ws_bot(message):

    bot = ConversationBot()
    bot.ask(question=message)

    message.channel_session['context'] = bot.context
    message.reply_channel.send({'text': bot.response.as_json})
