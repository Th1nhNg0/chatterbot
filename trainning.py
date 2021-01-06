from chatterbot import ChatBot
from chatterbot.conversation import Statement

bot = ChatBot(
    'Bot Thong Minh',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://admin:DBhMSEL1BU4HAzYs@chatbot-shard-00-00.2jziq.mongodb.net:27017,chatbot-shard-00-01.2jziq.mongodb.net:27017,chatbot-shard-00-02.2jziq.mongodb.net:27017/chatbot2?ssl=true&replicaSet=atlas-jdhzqq-shard-0&authSource=admin&retryWrites=true&w=majority',  preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
    ]
)


def get_feedback():
    text = input()
    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


while True:
    try:
        print('Type something to begin...')
        input_statement = Statement(text=input())
        response = bot.generate_response(
            input_statement
        )
        print('\n Is "{}" a coherent response to "{}"? \n'.format(
            response.text,
            input_statement.text
        ))
        if get_feedback() is False:
            print('please input the correct one')
            correct_response = Statement(text=input())
            bot.learn_response(correct_response, input_statement)
            print('Responses added to bot!')
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
