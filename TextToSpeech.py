from watson_developer_cloud import TextToSpeechV1
import soundfile as sf
import sounddevice as sd
from playsound import playsound
class TextToSpeech:
    def __init__(self, *args, **kwargs):
        self.text_to_speech = TextToSpeechV1(
        iam_apikey='NQFfAAHV7hEiZGPZwHtVOX1hattVfi893ENjpCX0BTLV',
        url='https://stream.watsonplatform.net/text-to-speech/api')
        self.text_to_speech.set_detailed_response(False)
        
    pass
    def speak(self,text):
        audio=self.text_to_speech.synthesize(text,voice="pt-BR_IsabelaVoice",accept='audio/wav')
        with open('./sounds/TextToSpeech.wav', mode='bw') as f:
            f.write(audio.content)
        audio=sf.read('./sounds/TextToSpeech.wav')
        sd.play(audio[0],22200)
        sd.wait()