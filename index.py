from sqlite3.dbapi2 import Cursor
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql
import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Fe270495',
                             db='usuarios',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

janela = Tk()
janela.title ('FD Systems - Login')
janela.geometry('600x300')
janela.configure(background='white')
janela.resizable(width = False, height = False)
janela.iconbitmap(default = "icons/Logoicon.ico")

####Carregando imagens####

logo = PhotoImage(file ='icons/logo.png')

######## Widgets########
LeftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side = LEFT) 
RightFrame = Frame(janela, width=395, height=300,bg="MIDNIGHTBLUE",relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image = logo,bg="MIDNIGHTBLUE")
LogoLabel.place(x=50,y=100)
## UserName
UserLabel = Label(RightFrame, text="Usuario:",font=("Century Gothic",18),bg="MIDNIGHTBLUE",fg='White')
UserLabel.place(x=5,y=95)

UserEntry = ttk.Entry(RightFrame, width=20)
UserEntry.place(x=120,y=100)

#Password
PassLabel = Label(RightFrame, text="Senha:",font=("Century Gothic",18),bg="MIDNIGHTBLUE",fg='White')
PassLabel.place(x=5,y=135)

PassEntry = ttk.Entry(RightFrame, width=20, show='*')
PassEntry.place(x=120,y=145)

#Botoes

LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100,y=200)

def Register():
    LoginButton.place(x=50000)
    RegisterButton.place(x=5000)
    
    NomeLabel = Label(RightFrame, text="Nome:",font=("Century Gothic",18),bg="MIDNIGHTBLUE",fg="White")
    NomeLabel.place(x=5,y=5)
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=100,y=14)
    
    EmailLabel = Label(RightFrame, text="Email:",font=("Century Gothic",18),bg="MIDNIGHTBLUE",fg="White")
    EmailLabel.place(x=5, y=50)
    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=100,y=55)
    
    def RegisterToDB():
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UserEntry.get()
        Senha = PassEntry.get()
        
        
        if Nome == "" and Email == "" and Usuario == "" and Senha =="":
            messagebox.showerror(title="Erro", message="Existem campos vazios")
        else:
            with connection.cursor() as cursor:
            sql = "INSERT INTO `USUARIOS`(`NOME`,`EMAIL`,`USUARIO`,`SENHA`) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql,(Nome,Email,Usuario,Senha))
            messagebox.showinfo(title="informação de registro", message="Cadastrado com sucesso !")
            
        connection.commit()
    
    Register = ttk.Button(RightFrame, text="Registrar",width=30, command=RegisterToDB)
    Register.place(x=100,y=200)
    
    def BackToLogin():
        NomeLabel.place(x=50000)
        NomeEntry.place(x=50000)
        EmailEntry.place(x=5000)
        EmailLabel.place(x=50000)
        Register.place(x=5000)
        Voltar.place(x=5000)
        #trazendo os botões de volta
        LoginButton.place(x=100)
        Register.place(x=100)
        
    
    Voltar = ttk.Button(RightFrame, text="Voltar",width=30,command=BackToLogin)
    Voltar.place(x=100,y=260)

RegisterButton = ttk.Button(RightFrame, text="Registrar", width=30, command=Register)
RegisterButton.place(x=100,y=250)

janela.mainloop()