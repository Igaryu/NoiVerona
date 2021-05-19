# -*- coding: utf-8 -*-
import time
from ProcComuni import *



def ultima_riga_schede(db):
    req = "select max(idScheda) from schede"
    c = db.cursor()
    c.execute(req)
    d = c.fetchall()
    if d:
        return (d[0][0])
    else:
        return (0)



def scrutinio(db, vista_anagra):
    ns = numero_scrutinio(db, vista_anagra)
    if ns == 0:
        tmp = input("Non ci sono scrutini aperti: inizializzo primo scrutinio!!\n\nPremere un tasto per continiare... ")
        scrutinio = 1
    else:    
        si_no = "z"
        while si_no not in "CN":
            print("Numero attuale di scutinio e' %i: " % ns)
            si_no = input("\nVuoi continuare con questo scrutinio o avviarne uno nuovo\n[C]ontinua [N]uovo ? ").upper()
        if si_no == "N" :
            scrutinio = ns + 1
        else:
            scrutinio = ns
    return(scrutinio)      

def leggi_scheda(User, db):
    global vista_anagra
    vista_anagra = seleziona_view()
    lettura_iniziale = ''
    while lettura_iniziale != "FINE" and lettura_iniziale != "ANNULLA":
        intesta() 
        ns = numero_scrutinio(db,vista_anagra)
        if ns == 0:
            tmp = input("Non ci sono scrutini aperti: inizializzo primo scrutinio!!\n\nPremere un tasto per continiare... ")
            ns = 1
        else:    
            si_no = "z"
            while si_no not in "CN":
                print("Numero attuale di scutinio e' %i: " % ns)
                si_no = input("\nVuoi continuare con questo scrutinio o avviarne uno nuovo\n[C]ontinua [N]uovo ? ").upper()
                if si_no == "N":
                    ns = ns + 1
#                else:
#                    scrutinio=ns
        
#        ns=scrutinio(db,vista_anagra)
        annullato = ""
        scheda_chiusa = 0
        schede_lette = 0
        scheda_bianca = 0
        scheda_nulla = 0
        valida = 0
        progr = 0
        intesta()
        print("\n\nSiamo al numero ", ns , " di scrutinio.")
    
   #########             APRIRE CICLO VERIFICA SE NUMERICO O FINE         ########
    
        lettura_iniziale = input("\n\nLeggere numero di scheda\noppure FINE oppure ANNULLA \nper annullare questa scheda: ").upper()
        nr_scheda = lettura_iniziale
        if len(nr_scheda) == 0:
            continue 
        elif nr_scheda == "FINE":
            continue
        elif nr_scheda == "ANNULLA":
            continue
        if len(nr_scheda) != 0:
            try:
                tmp = int(nr_scheda)
            except:
                allarme(3)
                tmp = input("\n\n\nIl valore del Numero di Scheda deve essere:\n\n\t1) Un valore numerico\n\t2) FINE\n\t3) ANNULLA\n\nPremi un tasto per continuare...")
                continue
       
    
        req = "select scrutinio,idNumScheda from ESNA where idnumScheda="+str(int(nr_scheda))+" and scrutinio="+str(int(ns))+";"
        c = db.cursor()
        c.execute(req)
        d = c.fetchall()
        if d:
           allarme(3)
           tmp = input("Scheda gia' presente per questo scrutinio!!! Premere un tasto per continuare... ")
           continue
        
        if scheda_chiusa == 0:
            progr = 1
            aperta = 0
            code = ["","","","",""]
            while progr != 5 and scheda_chiusa == 0:
                intesta()
                ora_inizio = time.ctime()
                ora_fine = ""
                scheda_letta = progr
                lettura = input("Leggi CODICE "+str(progr)+" scrutinato\noppure FINE\t per chiudere la Scheda e registrarla\noppure BIANCA\t se la scheda va considerata bianca\noppure NULLA\t se la scheda va considerata nulla\noppure ANNULLA\t per annullare la scheda in corso di registrazione: ").upper()
                lettura = lettura[0:4]
####### AGGIUNGERE OPZIONI ANNULLA E FINE SEQUENZA LETTURA INFERIORE A TRE ######
                if lettura == "ANNU":
                    annullato = "SI"
                    allarme(3)
                    tmp = input("Caricamento scheda "+str(nr_scheda)+" annullato!! Premi un tasto per continuare... ")
                    break
                elif lettura == "FINE":
                    ora_fine = time.ctime()
                    scheda_chiusa = 1
                    schede_lette = progr
                    progr = 5
                elif lettura == "BIAN":
                    scheda_bianca = 1
                    scheda_chiusa = 1
                    scheda_nulla = 0
                elif lettura == "NULL":
                    scheda_nulla = 1
                    scheda_chiusa = 1
                    scheda_bianca = 0
                elif  len(lettura) == 4:
                    if vista_anagra == "AnagraLocale": 
                        req = "select Codice, Nome, Cognome from AnagraLocale where Codice='"+lettura+"';"
                    else:
                        req = "select Codice, Nome, Cognome from AnagraNazionale where Codice='"+lettura+"';"
                    c = db.cursor()
                    c.execute(req)
                    d = c.fetchall()
                    check =""
                    if not d:
                        check = "N"
                        tmp = input("Codice non presente nel database! Premi un tasto per continuare...")
                    elif progr > 1:
                        k = 1
                        check = ""
                        while k != progr+1: 
                            if lettura == code[k]: 
                                allarme(3)
                                tmp = input("Codice %s gia' letto per questa scheda!! Premere un tasto per rillegere... " % lettura)
                                check = "N"
                                break
                            else:
                                check = "S"
                                k = k + 1
            
##### InsERIRE COnsTROLLO SU VARIABILE ANNULLATO  ###########            
                    if check != "N":
                        code[progr] = lettura
                        print("Votato %s %s !!" % (d[0][2], d[0][1]))
                        progr = progr + 1
                        valida = 1
                        if aperta == 0:
                            aperta = 1
                            ora_inizio = time.ctime()
                   
        
            if progr == 5:
                k = ultima_riga_schede(db)
                scheda_chiusa = 1
                schede_lette = k

#    
#  Verificare se esegue correttamente la registrazione una volta raggiunte le 4 scchede consicutive:   
#  NON lo stia facendo mentre ok per normale, annulla e fine     
#        
        if schede_lette != 0 and scheda_chiusa == 1 and valida == 1:

            nr_righe = conta_righe(db, vista_anagra)
            k = 1
            intesta()
            while k < progr:
                print("\t"+str(k)+" scrutinato: "+ code[k])
                k = k + 1
            
            tmp =input("\n\nConfermi la lista caricata per la scheda nr. "+str(int(nr_scheda))+" dello scrutinio "+str(ns)+" ? [S/N] ").upper()
            if tmp != "S":
                return
            k = 1
            while k < progr:
                nr_righe = nr_righe + 1
                candidato = Codicecandidato(db, code[k])
                if candidato != -1:
                    req = "InsERT INTO elencoschede(scrutinio,idNumScheda,candidato,Bianca,Nulla,valida) VALUES ("+ str(ns)+","+str(nr_scheda)+","+str(candidato)+ ",0,0,1);" # query per l'inserimento della scheda 
                    c = db.cursor()
                    c.execute(req)
                    d = c.fetchall()

                    k = k + 1
                    aperta = 1
                else:
                    k = k + 1

            ora_fine = time.ctime()
            if vista_anagra == "AnagraLocale":
                req = "insert into SchedeNoiVerona (Evento,scrutinio,idNumScheda,Postazione,aperta,Chiusa,Status) Values('C0',"+str(int(ns))+","+ str(nr_scheda)+",'"+User+"','"+ora_inizio+"','"+ora_fine+"','OK');"
            else:
                req = "insert into SchedeNazionale (Evento,scrutinio,idNumScheda,Postazione,aperta,Chiusa,Status) Values('"+code[1][:2]+"',"+str(int(ns))+","+ str(nr_scheda)+",'"+User+"','"+ora_inizio+"','"+ora_fine+"','OK');"
            c = db.cursor()
            c.execute(req)
            d = c.fetchall()

            c.execute("commit;")
            d = c.fetchall()

        elif schede_lette == 0 and scheda_chiusa == 1 and scheda_bianca == 1:
            scheda_bianca(db, vista_anagra, code[1][:2], User, ns, scheda_bianca, scheda_nulla, valida, scheda_chiusa, schede_lette, annullato, nr_scheda, ora_inizio)
            continue
        elif schede_lette == 0 and scheda_chiusa == 1 and scheda_nulla == 1:
            scheda_nulla(db, vista_anagra, code[1][:2], User, ns, scheda_bianca, scheda_nulla, valida, scheda_chiusa, schede_lette, annullato, nr_scheda, ora_inizio)
            continue
