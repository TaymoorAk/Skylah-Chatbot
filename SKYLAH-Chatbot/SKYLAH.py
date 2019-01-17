from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from _overlapped import NULL

skylah = ChatBot('SKYLAH')
skylah.set_trainer(ListTrainer)

while True:
    message = input('You : ')
    
    if message.strip()!= 'Bye' or message.strip()!= 'bye':
        reply = skylah.get_response(message)
        print('Skylah : ',reply,'\n')
        
    if message.strip()=='Bye' or message.strip()=='bye':
        break