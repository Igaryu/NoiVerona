# -*- coding: utf-8 -*-

import  sys, os, getpass, time
from ProcComuni import intesta, Allarme, Notifica, NumeroScrutinio, SelezionaView


def Db_Init(db):
    intesta()
    Allarme(5)
    print("Esiste uno scrutinio chiuso su questo sistema:\nNON posso eseguire l'inizializzazione del DataBase!!!")
    print("\nSe DAVVERO vuoi azzerare tutto chiedi l'intervento\ndel manutentore del DataBase.")
    input("\n\nPremere un tasto per continuare... ")
    return

#    print("\n\nSei davvero sicuro di voler inzializzare il database?")
#    print "Farlo significa riportare il db alle condizioni di installazione:"
#    print "Questa operazione non potra essere annullata!!!\n\n"
#    SiNo=raw_input("Conferma se vuoi inializzare il DataBase [S/N] ").upper()
#    if SiNo != "S":
#        return ("DB NON inizializzato")
#    VistaAnagra=SelezionaView()
#    if VistaAnagra=="AnagraLocale":
#        Allarme(3)
#        print "\n\nLo scrutinio del 13/11/2015 risulta chiuso !!!!"
#        print "\n NON puoi azzerare da procedura questa sezione dati"
#        print "Se ne hai necessità chiedi l'intervento dell'amministrator del database."
#        raw_input("\n\nPremere un tasto per continuare... ")
#        return
#        req="delete from ESNV"
#    else:
#        req="delete from ESNA"
#
#    c=db.cursor()
#    c.execute(req)
#    d=c.fetchall()
#
#    print "DataBase inizializzato!!"
#    print "Il DataBase contiene ora solo l'elenco dei candidati e scrutini precedendi ad oggi."
#    print "Qualunque operazione fatta antecedente a questa, è stata annullata"
#    SiNo=raw_input("\n\nPremi un tasto per tornare al menu... ").upper()
#    return ("DB Inizializzato")


def Upd_Scrutinio(db):
    intesta()
    VistaAnagra=SelezionaView()
    if VistaAnagra=="AnagraLocale":
        Allarme(3)
        input("\n\nPremere un tasto per continuare... ")
        return
    

    NS=NumeroScrutinio(db,VistaAnagra)
    if NS==0:
        Allarme(3)
        input("\n\nNon ci sono scrutini iniaizlizzati al momento: Inizializzazione non necessaria!\n\nPremi un tasto per continuare!")
        return(0)
    elif NS==1:
        Allarme(3)
        input("\n\nC'è un solo scrutinio iniaizlizzato al momento: \n\nregressione scrutinio non possibile!\n\nPer rimuovere il primo scrutinio esegui INIZIALIZZA DB dal menu\n\nPremi un tasto per continuare!")
        return(1)
    else:
        print("Siamo allo scrutinio "+str(NS)+": vuoi davvero retrocedere allo scrutinio "+str(NS-1)+" ?")
        print("Ti rammento che tutti i dati registrati per lo scrutinio "+str(NS)+" andranno persi ")
        print("senza possibilita' di recupero.")
        SiNo=input("\n\nConferma la cancellazione dello scrutinio "+str(NS)+": [S/N]: ").upper()
        if SiNo != "S":
            return ("N")
        else:
            req="delete from ESNA where Scrutinio="+str(NS)+";commit;"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            req="delete from SchedeNazionale where Scrutinio="+str(NS)+";commit;"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()


            print("Scrutinio "+str(NS)+" CANCELLATO:")
            print("Tutti i dati relativi allo scutinio "+str(NS)+" sono stati rimossi.")
            print("Da questo momento lo scrutinio attivo è il numero "+str(NS-1)+".")
            print("Potete procedere con lo scrutinio "+str(NS-1)+" o iniziallizare un nuovo scrutinio "+str(NS)+".")
            input("\n\nPremi un tasto per contnuare... ").upper()
            return("S")


def Esegui_Dump(User,Password,db):
    intesta()
    Allarme(3)
    print("Attenzione: questa funzione sovrascrivera' un eventuale backup\neseguito in precendenza!! Se volete salvare la versione precedente\nrinomiarla o spostarl in altra directory!!!")
    
    SiNo=input("\n\nVuoi continuare con il backup dei dati ?\n(dovrete digitare la password all'avvio del backup)\nDigitare S o N: ").upper()
    if SiNo != "S":
        return ("N")
    os.system("mysqldump -h 192.168.1.50 -u "+User+" -p NoiVerona>NoiVeronaNazionale.dump")
    SiNO=input("BackUp dei dati eseguito con successo!!\n\nPremi un tasto per continuare... ")
    return("S")
    
