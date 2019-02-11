from watson_developer_cloud import SpeechToTextV1
import json
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
import soundfile as sf
import sounddevice as sd

class SpeechToText:
    def __init__(self):
        self.SpeechtoTxt = SpeechToTextV1(
            iam_apikey='Ymt_PewjqkvzOc7Ky7QGEZnawcY60SbdXKLGrfb8zb4n',
            url='https://stream.watsonplatform.net/speech-to-text/api'
        )
        self.SpeechtoTxt.set_detailed_response(False)
    pass

    def record(self):
        fs=44100
        duration = 8  # seconds
        self.myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
        print ("Gravando Audio")
        sd.wait()
        print("Escrevendo arquivo")
        sf.write('./sounds/SpeechToText.wav',self.myrecording,fs)
        return self.reconhecer()
    

    def reconhecer(self):
        data= open('./sounds/SpeechToText.wav', 'rb')
        data=self.SpeechtoTxt.recognize(data,model='pt-BR_NarrowbandModel')
        print(data.get('results')[0].get('alternatives')[0].get('transcript'))
        return data.get('results')[0].get('alternatives')[0].get('transcript') 

    pass
