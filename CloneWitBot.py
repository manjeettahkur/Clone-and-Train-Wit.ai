import wit
import requests

class WitBot:
    def __init__(self,token):
        self.token = token
        
    def CloneMasterBot(self,name='NewBot',lang='en',private='false'):
    
        headers = {}
        headers['Authorization'] = 'Bearer ' + self.token
        headers['Content-Type'] = 'application/json'
        
        data = {}
        datap['name']  = name
        data['lang'] = lang
        data['private'] = private

        response  = requests.post('curl', headers=headers, data=data)

        return response
    

class TrainWitBot:
    def __init__(self,token):
        self.token = token
    
    def train(self,text,entities):
        headers = {}
        headers['Authorization'] = 'Bearer ' + self.token
        headers['Content-Type'] = 'application/json'

        data = {}
        data['text'] = text
        data['entities']= entities
        data = list(data)
        response = requests.post('curl', headers=headers, data=data)
        if response['sent']:
            print 'Added to the bot'
            return True
        else:
            print 'Failed to add to the bot'
            return False
        