# -*- coding: utf-8 -*-
import time
from ProcComuni import *

def Visualizza_Totali(db):
    global VistaAnagra
    VistaAnagra=SelezionaView()
    
    intesta()
    NS=NumeroScrutinio(db,VistaAnagra)
    if (NS > 1):
        tmp=input("Sono presenti "+str(NS)+" scrutini registrati: \nper quale scrutinio vuoi i totali? (1-"+str(NS)+") ? ")
        if tmp.isdigit():
            tmp=int(tmp)
            if (tmp < 1) or (tmp > NS):
                Allarme(3)
                input("Valore digitato, ossia: "+str(tmp)+" fuori dal range possibile (1-"+str(NS)+") !!!")
                return("NS Fuori range")
            else:
                NS=tmp
        else:
                Allarme(3)
                input("Avete digitato '"+str(tmp)+"' ma il valore richiesto DEVE essere numerico !!!")
                return("NS AlfaNum")





######################################################################
##                                                                  ##
##                        LISTA PER C001-C014                       ##
##                                                                  ##
######################################################################
    if VistaAnagra=="AnagraLocale":
        intesta()
        for k in range(1,17):
            Codice=""
            CN=""
            req="Select Nome,Cognome,Codice from anagra where idAnagra="+str(k)+";"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            Codice=d[0][2]
            CN=d[0][1]+" "+d[0][0]
            req="select sum(Valida) from elencoschede where Scrutinio="+str(NS)+" and Candidato="+str(k)+";"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            Totale=d[0][0]
            if len(CN)<26:
                if len(CN)<18:
                    print("\tTotali voto per "+Codice, str(CN)+" \t\t\t: "+str(Totale))
                else:
                    print("\tTotali voto per "+Codice, str(CN)+" \t\t: "+str(Totale))
            else:
             print("\tTotale voti per "+Codice, str(CN)+" \t: "+str(Totale))

        req="select count(*) from schede where Status='NULLA' and Scrutinio="+str(NS)+";"
        c.execute(req)
        d=c.fetchall()
        TotaleNulle=d[0][0]

        req="select count(*) from schede where Status='BIANCA' and Scrutinio="+str(NS)+";"
        c.execute(req)
        d=c.fetchall()
        TotaleBianche=d[0][0]
        print("\n\n\tScrutinio "+str(NS)+": totale schede NULLE \t\t\t: "+str(TotaleNulle)) 
        print("\tScrutinio "+str(NS)+": totale schede BIANCHE \t\t\t: "+str(TotaleBianche)) 
        tmp=input("\n\nPremi un tasto per continuare...") 

    else:


######################################################################
##                                                                  ##
##                        LISTA PER CO01-CO14                       ##
##                                                                  ##
######################################################################

        intesta()
        for k in range(19,33):
            Codice=""
            CN=""
            req="Select Nome,Cognome,Codice from anagra where idAnagra="+str(k)+";"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            Codice=d[0][2]
            CN=d[0][1]+" "+d[0][0]
            req="select sum(Valida) from elencoschede where Scrutinio="+str(NS)+" and Candidato="+str(k)+";"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            Totale=d[0][0]
            if len(CN)<26:
                if len(CN)<18:
                    print("\tTotali voto per "+Codice, str(CN)+" \t\t\t: "+str(Totale))
                else:
                    print("\tTotali voto per "+Codice, str(CN)+" \t\t: "+str(Totale))
            else:
                print("\tTotale voti per "+Codice, str(CN)+" \t: "+str(Totale))
        tmp=input("\n\nPremi un tasto per continuare...") 

######################################################################
##                                                                  ##
##                        LISTA PER R001-R004                       ##
##                                                                  ##
######################################################################

        intesta()
        for k in range(33,37):
            Codice=""
            CN=""
            req="Select Nome,Cognome,Codice from anagra where idAnagra="+str(k)+";"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            Codice=d[0][2]
            CN=d[0][1]+" "+d[0][0]
            req="select sum(Valida) from elencoschede where Scrutinio="+str(NS)+" and Candidato="+str(k)+";"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            Totale=d[0][0]
            if len(CN)>17:
                print("\tTotale voti per "+Codice, str(CN)+" \t\t: "+str(Totale))
            else:
                print("\tTotali voto per "+Codice, str(CN)+" \t\t\t: "+str(Totale))


######################################################################
##                                                                  ##
##                        LISTA PER P001-P004                       ##
##                                                                  ##
######################################################################

#       intesta()
        print("\n\n\n")
        for k in range(37,41):
            Codice=""
            CN=""
            req="Select Nome,Cognome,Codice from anagra where idAnagra="+str(k)+";"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            Codice=d[0][2]
            CN=d[0][1]+" "+d[0][0]
            req="select sum(Valida) from elencoschede where Scrutinio="+str(NS)+" and Candidato="+str(k)+";"
            c=db.cursor()
            c.execute(req)
            d=c.fetchall()
            Totale=d[0][0]
            if len(CN)>18:
                print("\tTotale voti per "+Codice, str(CN)+" \t\t: "+str(Totale))
            else:
                print("\tTotali voto per "+Codice, str(CN)+" \t\t\t: "+str(Totale))


        if VistaAnagra=="AnagraLocale":
            req="select count(*) from SchedeNoiVerona where Status='NULLA' and Scrutinio="+str(NS)+";"
        else:
            req="select count(*) from SchedeNazionale where Status='NULLA' and Scrutinio="+str(NS)+";"
        c.execute(req)
        d=c.fetchall()
        TotaleNulle=d[0][0]


        if VistaAnagra=="AnagraLocale":
            req="select count(*) from SchedeNoiVerona where Status='BIANCA' and Scrutinio="+str(NS)+";"
        else:
            req="select count(*) from SchedeNazionale where Status='BIANCA' and Scrutinio="+str(NS)+";"

        c.execute(req)
        d=c.fetchall()
        TotaleBianche=d[0][0]
        print("\n\n\tScrutinio "+str(NS)+": totale schede NULLE \t\t\t: "+str(TotaleNulle)) 
        print("\tScrutinio "+str(NS)+": totale schede BIANCHE \t\t\t: "+str(TotaleBianche)) 
        tmp=input("\n\nPremi un tasto per continuare...") 
    return





