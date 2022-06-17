from fileinput import close
import sqlite3
from sre_constants import BRANCH
from time import time
from tkinter import *
import tkinter as tk
from turtle import title, width, window_height
from verifi_user_exist import req_verif_user_exist
from dblogin import *


# *******Fonction login ()
def open_login_function():
    #FENETRE LONGIN 
    fen1 = Tk()
    fen1.title('LOGIN')
    fen1.geometry('500x500')
    fen1['bg']='black'
    fen1.resizable(0,0) # ceci block la fenetre

        # Creation des LABELS
    #name = Label(fen, text= 'Votre nom : ' )
    email = Label(fen1, text= 'Votrei email : ' )
    password_label = Label(fen1, text='Votre mot de passe')

        #Desidgn des labels


    email['bg'] = 'black'
    email['fg'] = 'white'

    password_label['bg'] ='black'
    password_label['fg'] = 'white'

    # Affichage Des label  LOGIN

    email.place(x=70, y=150)
    password_label.place(x=70, y=200)
    # DESING DES LABLES LONGIN
    email['font']= 'bold,9'
    password_label['font'] ='bold,9'

    # Label qui return button action
    return_login = Label(fen1)
    #return_singup = Label(fen1)


    #Affichage des Label return
    return_login.place(x=160, y=350)
    return_login['bg']='black'
    return_login['fg']='white'
    return_login['font'] = 'bold,14'
   # return_login['width'] ='500'

    #return_singup.place(x=0, y=150)
    #return_singup['bg']='black'
    #return_singup['fg']='white'

    #LES CHAMPS DENTRER

    
    get_email = Entry(fen1)
    get_password = Entry(fen1)

    # Positionnement des champs dentre (input)
    get_email.place(x=230, y=150)
    get_password.place(x=230, y=200)
    #get_password.grid(row =2, column=0)


    # FONTION QUI EST DECLANCHER QUAND LUTULISATEUR CLIQUE SUR CONNEXION 
    def action_login():
        
        #verif_name = get_name.get()
        verif_password = get_password.get()
        verif_email = get_email.get()
        
        # jexecute la requette
        req= 'select * from user where password ="{psw}" and email ="{email}" and etat=1 '.format(psw =verif_password, email = verif_email )
        cur.execute(req)
        row = cur.rowcount
        #rep = print(cur.fetchall())
        #print(rep)


        if(row != -1):
            #print('Ok')
            return_login['bg']='red'
            return_login['text'] ='*** Connexion Reussit **'
            
        else:
            return_login['bg']='red'
            return_login['text'] ='*** Connexion Innexistante ***'
        conn.close()

    def login_back():
        fen1.destroy()

    #INPUT les buttons 
    btn_login = Button(fen1, text='Connexion', command = action_login)
    btn_back = Button(fen1, text='Fermer', command = login_back)
    
    
    
  


    #Style des button 
    btn_login.place(x=100, y=250)
    btn_login['width']= '9'
    btn_login['height']= '2'
    btn_login['font'] = 'bold, 15'
    btn_login['bg'] = 'gray'

    btn_back.place(x=300, y=250)
    btn_back['width']= '9'
    btn_back['height']= '2'
    btn_back['font'] = 'bold, 15'
    btn_back['bg'] = 'gray'

# ****** Fonction Inscription () *******
def open_singup_function():
    
    def action_singup():
        #FENETRE 2
        fen2 = Tk()
        fen2.title('SING UP')
        fen2.geometry('250x250')
        fen2['bg']='black'
        #fen2.resizable(0,0) # ceci block la fenetre

        #Creation des labels pour le sing UP

        name_label = Label(fen2, text ='Entrez votre nom')
        email_label = Label(fen2, text= 'Entrez Votre Email')
        password_label = Label(fen2, text= 'Votre mot de passe')


        #DESING DES LABLES pour le sing UP
        name_label['bg'] = 'Black'
        name_label['fg'] = 'White'

        email_label['bg']='black'
        email_label['fg']= 'white'

        password_label['bg'] = 'black'
        password_label['fg']= 'white'

        #Affichage Des labels pour le sing up
        name_label.grid(row = 1, column=0, pady = 2)
        email_label.grid(row =2, column=0, pady = 2)
        password_label.grid(row = 3, column=0, pady = 2)

        #LES CHAMPS DENTRER POUR LE SING UP

        get_name = Entry(fen2)
        get_email = Entry(fen2)
        get_password = Entry(fen2)

        # Positionnement des champs dentre (input) pour le sing Up
        get_name.grid(row = 1, column = 1)
        get_email.grid(row = 2, column = 1)
        get_password.grid(row =3, column=1)
        

        #verif_name = get_name.get()
        #verif_email = get_email.get()

        # jexecute la requette
        

        fen2.mainloop()
        

        # FIN DE DES FONCTIONS LONGIN ET SING UP

# ____FENETRE PRINCIPALE______ #

fen = Tk()
fen.title('ENREGISTREMENT')
fen.geometry('500x500')
fen['bg']='black'
fen.resizable(0,0) # ceci block la fenetre

# Espacement  des lignes
fen.columnconfigure(0, weight=1)
fen.columnconfigure(1, weight=3)

# TITRE DE LA FENETRE PRINICIPAL
h1 = Label(fen, text="Registration form",width=20,font=("bold", 20), borderwidth =2, relief =GROOVE )
h1.place(x=90,y=53)
h1['bg'] = 'gray'
h1['fg']= 'Black'

# BOUTOUNS DE LA FENETRE PRINCIPALE

btn_go_to_login = Button(fen, text='Connexion', command = open_login_function)
#btn_go_to_login.bind('<Button-1>', open_login_function)
btn_go_to_singup = Button(fen, text= 'Inscription', command = open_singup_function)

#DESING DES BOUTTONS

btn_go_to_singup['width']= '9'
btn_go_to_singup['height']= '2'
btn_go_to_singup['font'] = 'bold, 20'
btn_go_to_singup['bg'] = 'gray'

btn_go_to_login['width']= '9'
btn_go_to_login['height']= '2'
btn_go_to_login['font'] = 'bold, 20'
btn_go_to_login['bg']='gray'


# AFFICHAGE DES BOUTOUNS
btn_go_to_singup.place(x=60, y=150)
btn_go_to_login.place(x=300, y=150)


fen.mainloop()
