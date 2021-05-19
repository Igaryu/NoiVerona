#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import getpass
import time

from ProcComuni import *
from Totali import *
from Manutenzione import *
from LeggiScheda import * 

try:
    import  pymysql
except ImportError:
    print("\n\n*** Attenzione !!!")
    print("\tPer poter utilizzare questo script devi avere installato il modulo:")
    print("\tPyMySQL. Da un analisi del tuo sistema non riuslta installato.")
    print("\tPer installarlo via pip esegui il seguente comando:")
    print("\tpip install pymysql. Dopo l'emerge rilancia GesRemTrad\n")
    sys.exit(-1)



vista_anagra, vista_es, vista_s, annullato, nr_scheda = '', '', '', '', ''
ns = 0
bianca = 0
nulla = 0
valida = 0
scheda_chiusa = 0
schede_lette = 0

intesta()

user, password = getlogin()


if len(user) == 0 or len(password) == 0:
    print("\nI campi user e password devono contenere un valore !!\n\n")
    input("Premi un tasto per continuare...")
    sys.exit(-2)

print("\n\nConnesione al server in corso: attendere prego ....")

try:
    db = pymysql.connect("127.0.0.1", user, password, "NoiVerona")
    db.autocommit(False)


except:
    print("\n\n*** Attenzione !!!")
    print("\nConnessione al database Votazioni NoiVerona fallito !!!")
    print("Verifica username e password e riprova.\n")
    input("Premi un tasto per continuare...")
    sys.exit(-2)
        
c = db.cursor()
risp = 0
while risp !=4 :
    risp = menu()
    if risp == 1:
        leggi_scheda(user, db)
    if risp == 2:
        visuallizza_totali(db)
    if risp == 3:
        if user != "root" and user != "Admin":
            allarme(3)
            input("\n\nNon sei un utente abilitato per la manutenzione!!\nPremi un tasto per continuare... ")
            pass
        else:
            risp1 = 0
            risp1 = menu_manutenzione()
            while risp1 != 4:
                if risp1 == 1:
                    upd_scrutinio(db)
                    risp1 = 4
                elif risp1 == 2:
                    esegui_dump(user, password, db)
                    risp1 = 4
                elif  risp1 == 3:
                    db_init(db)
                    risp1 = 4
                elif risp1 == 4:
                    pass

    if risp == 4:
        input("\n\nFine sessione.\nPremere un tasto per conitnuare... ")
        c.execute("commit;")
        d = c.fetchall()
        db.close()
        cls()
        sys.exit(0)
