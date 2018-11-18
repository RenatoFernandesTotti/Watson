import tkinter
from Wats import Wats
def receive(msg):
    while True:
        try:
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break

def send(event=None):
    msg = my_msg.get()
    msg='Voce: '+   msg
    my_msg.set("")
    msg_list.insert(tkinter.END,msg)
    bot.bot_resposta(msg_list,msg)


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
msg_list.insert(tkinter.END,"Bom dia! Meu nome é SherBot Holmes estou aqui pra te dar informacoes sobre a facens!")
msg_list.insert(tkinter.END,"Em que posso ajudar?")
bot=Wats(top,msg_list)
tkinter.mainloop()