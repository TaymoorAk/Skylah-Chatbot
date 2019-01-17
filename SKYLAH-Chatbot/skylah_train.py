from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

skylah = ChatBot('SKYLAH')
skylah.set_trainer(ListTrainer)
from introduction import intro
from science import sci
from sports import sport
from greetings import greet
from humor import humor
from artificial_intelligence import A_I
   
skylah.train(intro)
skylah.train(sci)
skylah.train(sport)
skylah.train(greet)
skylah.train(humor)
skylah.train(A_I)