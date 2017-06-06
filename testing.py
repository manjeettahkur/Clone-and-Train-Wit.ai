from CloneWitBot import WitBot
from CloneWitBot import TrainWitBot

witbot  = WitBot(<YOUR_MASTER_BOT_TOKEN>)
res = witbot.CloneMasterBot(<BOT_NAME>)
print res.text


trainbot = TrainWitBot(<BOT_TOKEN>)
res = trainbot.train('I want to fly to paris',<ENTITIES>)
print res.text