from chatterbot import ChatBot
from chatterbot.conversation import Statement

bot = ChatBot(
    'Bot Thong Minh',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='duong dan',
    ]
)


def get_feedback():
    text=input()
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
        input_statement=Statement(text = input())
        response=bot.generate_response(
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
