import json
import tkinter
from watson_developer_cloud import AssistantV1, WatsonApiException
from ResponseTreatment import ResponseTreatment
class Wats:
    def __init__(self,top,msgList):
        self.assistant = AssistantV1(
            version='2018-07-10',
            username='a3c70349-d3b4-452f-87b3-44950eff05de',
            password='wjsEskSD80HD',
            url='https://gateway.watsonplatform.net/assistant/api'
        )
        self.assistant.set_detailed_response(False)
        self.resposta = ResponseTreatment(top,msgList)
    def bot_resposta(self,msg_list,input_user):
        try:   
            texto = input_user
            response = self.assistant.message(
                workspace_id='80e56d8d-b5e8-4dc9-bb9f-811ff30d12e3',
                input={
                    'text': texto
                }
            )
            try:
                intent = response.get('intents')[0].get('intent')
            except:
                intent='error'
            if(intent == 'Professor'):
                self.resposta.professor(response,msg_list)
            elif(intent =='Salas'):
                self.resposta.sala(response,msg_list)       
            elif(intent=='Boasvindas'):
                self.resposta.insertMessage(str(response.get('output').get('text')[0]))
            elif(intent=='Setores'):
                self.resposta.setores(response,msg_list)
            elif(intent=='GoodBye'):
                self.resposta.insertMessage(str(response.get('output').get('text')[0]))
            else:
                self.resposta.insertMessage(str(response.get('output').get('text')[0]))
            self.resposta.insertMessage('Posso ajudar em algo mais?')

        except WatsonApiException as ex:
            self.resposta.insertMessage("Method failed with status code " + str(ex.code) + ": " + str(ex.message))