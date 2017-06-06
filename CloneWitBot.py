import wit
import requests
import json

class WitBot:
    def __init__(self,token):
        self.token = token
        
    def CloneMasterBot(self,name='NewBot',lang='en',private='false'):
    
        headers = {}
        headers['Authorization'] = 'Bearer ' + self.token
        headers['Content-Type'] = 'application/json'
        
        data = {}
        data['name']  = name
        data['lang'] = lang
        data['private'] = private

        return requests.post('https://api.wit.ai/apps?v=20170307', headers=headers, data=json.dumps(data))
    

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
        ary = []
        ary.append(data)
        print ary
        response = requests.post('https://api.wit.ai/apps?v=20170307', headers=headers, data=json.dumps(ary))
        return response
        