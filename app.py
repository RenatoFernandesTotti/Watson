import tkinter
from Wats import Wats
from TextToSpeech import TextToSpeech
from SpeechToText import SpeechToText
import os
def receive(msg):
    while True:
        try:
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break
#Botoes funcoes
def send(event=None):
    msg = my_msg.get()
    msg='Voce: '+   msg
    my_msg.set("")
    msg_list.insert(tkinter.END,msg)
    bot.bot_resposta(msg_list,msg)

def voiceSend():
    texto=SpeechToText()
    voz.speak("estou escutando")
    texto=texto.record()
    msg_list.insert(tkinter.END,texto)
    bot.bot_resposta(msg_list,texto)
    pass

#
os.system('pip install -r ./req.txt')
os.system('cls')
#Parte grafica
top = tkinter.Tk()
top.title("Sherbot Holmes")
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("Digite aqui")
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=15, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Enviar", command=send)
send_button.pack()
voiceSend_Button=tkinter.Button(top, text="Falar", command=voiceSend)
voiceSend_Button.pack()
voz=TextToSpeech()
msg_list.insert(tkinter.END,"Bom dia! Meu nome é SherBot Holmes estou aqui pra te dar informacoes sobre a facens!")
msg_list.insert(tkinter.END,"Em que posso ajudar?")
bot=Wats(top,msg_list)
voz.speak("Bom dia! Meu nome é XerBot Rolmes estou aqui pra te dar informações sobre a facêns!  Em que posso ajudar?")
tkinter.mainloop()

