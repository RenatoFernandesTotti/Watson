import json
import pyodbc
import re
from tkinter import *
import os
from PIL import Image, ImageTk
class ResponseTreatment:
    def __init__(self,top,msgList):
        conn = pyodbc.connect(r'Driver={ODBC Driver 13 for SQL Server};SERVER=localhost;DATABASE=Professor;Trusted_Connection=yes;')
        self.cursor = conn.cursor()
        self.regex=re.compile("[a-z][ ]*[1-3][0-9]",re.IGNORECASE)
        self.predios=('A','E','L','G','H','E','B','J','C','D','K','I')#Todos os predios da facens
        self.root=top
        self.msg_list=msgList
    def professor(self,response,msg_list):
        i=0
        profs=response.get('entities')
        self.p=0
        if(len(profs)==0):
            self.insertMessage("nao encontrei professores com esse nome!")
            return 
        elif(len(profs)!=1):
            repete=True
            while (repete):
                self.insertMessage("Encontrei mais de um professor com esse nome! qual deles e o correto?")
                for prof in profs:
                    self.insertMessage(str(i+1)+':'+prof.get('value'))
                    i+=1
                self.popup()
                if(self.p<0 or self.p>len(profs)):
                    self.insertMessage("\n o numero deve ser igual a um da lista!!\n")
                    i=0
                    continue#Caso o numero seja invalido ocorre um loop forcado a partir do teste
                break#caso esteja tudo correto o programa continua
            self.p-=1
        query = 'select * from tbProf where nome='+r"'" + profs[self.p].get('value')+r"'"
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        retorno = str(response.get('output').get('text')[0])
        retorno = retorno.replace("^professor", row[0][1])
        retorno = retorno.replace("^mail", row[0][2])
        self.insertMessage(retorno)
        msg_list.yview(END)
        pass
    def sala(self, reponse,msg_list):
        #reponsetxt=str.split(reponsetxt)
        a=reponse
        retorno = str(a.get('output').get('text')[0])
        user= str(a.get('input').get('text'))
        result=self.regex.search(user)
        try:
            result=result.group(0)
        except:
            self.insertMessage("Eu nao encontrei essa sala, voce pode ter digitado uma sala invalida ou no formato errado, porfavor digite por exemplo A12")
            return
        result=str.upper(result)
        result=result.replace(" ","")
        result=list(result)
        if result[0] not in self.predios:
            self.insertMessage('Esse predio nao existe!')
        if(result[0]=='C' and int(result[1])>=5):
            self.insertMessage("O predio C somente tem 3 andares!")
            return
        elif(result[0]=='L' and int(result[1])>=4):
            self.insertMessage("O predio C somente tem 3 andares!")
            return
        elif(int(result[1])>=3):
            erro='O predio '+str(result[0])+' nao tem mais que dois andares!'
            self.insertMessage(erro)    
        retorno=retorno.replace("^predio","no predio "+result[0])
        retorno=retorno.replace("^andar",result[1]+"ºandar")
        self.insertMessage(retorno)
    def setores(self,response,msg_list):
        setor=response.get('entities')[0].get('value')
        resposta=""
        if(setor=='Biblioteca'):
            resposta+='A biblioteca fica no predio H abaixo da sala de estudos!'
        elif(setor=='AMT'):
            resposta+='A sala da AMT fica no terreo do predio A, porem esta sendo usada pela equipe do Liquid Galaxy'
        elif(setor=='Atlética'):
            resposta+=('A Atletica fica ao lado direito do predio H e a'+
                        'esquerda da cantina! Voce so precisa pegar um caminho entre as duas!')
        elif(setor=='Cantina'):
            resposta+=('A cantina fica perto da Biblioteca em frente ao predio D')
        self.insertMessage(resposta)
        pass
    
    def getVar(self,event=None):
        self.p=int(self.e2.get())#-1
        self.new.destroy()
    
    def popup(self):
        self.new = Toplevel()
        self.e2 = Entry(self.new)
        self.e2.pack(side = LEFT)
        self.e2.bind("<Return>",self.getVar)
        b2 = Button(self.new, text = "OK", command = self.getVar)
        b2.pack(side = RIGHT)
        l2 = Label(self.new, text = "Digite o numero do professor!")
        l2.pack()
        self.e2.focus_force()
        self.root.wait_window(self.new)

    def insertMessage(self,msg):
        self.msg_list.insert(END,msg)
        self.msg_list.yview(END)

    def mapPopup(self,fodac,msg):
        load = Image.open('./scr/images/sector-'+fodac+'.png')
        render = ImageTk.PhotoImage(load)
        op={"height":load.height,"width":load.width}
        pop=Toplevel()
        pop.config(op)
        img = Label(pop, image=render)
        img.image = render
        img.place(x=0,y=0)

        