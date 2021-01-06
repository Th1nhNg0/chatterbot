from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Bot Thong Minh',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='duong dan',
    read_only=True
)


trainer = ChatterBotCorpusTrainer(chatbot)

# comment dòng này lại để không phải train mỗi khi chạy chương trình
trainer.train('./vietnamese')
# chỉ train file mình muốn:
# trainer.train('./vietnamese/chaohoi.yml')

# chương trình đơn giản để chat trên terminal
while True:
    try:
        bot_input = chatbot.get_response(input('user: '))
        print('bot:', bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
