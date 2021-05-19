# -*- coding: utf-8 -*-
import  sys, os, getpass, time

def cls():
    if os.name=='posix':
        os.system('clear')
    else:
        os.system('cls')


def getlogin():
    name=input('Username: ')
    passwd=getpass.getpass('Password: ')
    return name,passwd



def intesta():
    cls()
    print("\nR.S.V.N.N.							         ver 1.3")
    print("\nRegistrazione Schede Votazioni Noi Nazionale\n\n")


def menu():
    risp=0
    while ((risp < 1) or (risp > 4)):
        intesta()
        print("\n\n\n")
        print("\t\t\t(1) Lettura Schede\n\n")
        print("\t\t\t(2) Visualizza Totali\n\n")
        print("\t\t\t(3) Manutenzione DB\n\n")
        print("\t\t\t(4) Esci\n\n")
        risp=input('\n\nSeleziona Voce Menu [ 1 - 4 ] ')
        if (risp=="1") or (risp=="2") or (risp=="3") or (risp=="4"):
            risp=int(risp)
        else:
            risp=0
		
    return risp



def menu_manutenzione():
    intesta()
    risp=0
    while ((risp < 1) or (risp > 4)):
        intesta()
        print("\n\n\n")
        print("\t\t\t(1) Modifica Scrutinio Attuale\n\n")
        print("\t\t\t(2) Esegui Dump\n\n")
        print("\t\t\t(3) Inizializza DB      \n\n")		
        print("\t\t\t(4) Esci\n\n")
        risp=input('\n\nSeleziona Voce Menu [ 1 - 4 ] ')
        if (risp=="1") or (risp=="2") or (risp=="3") or (risp=="4"):
#               if int(risp) in range(1,5):
            risp=int(risp)
        else:
            risp=0
	
    return risp





def Allarme(n):
    print((n * chr(7)))

def ContaRighe(db,VistaAnagra):
    if VistaAnagra=="AnagraLocale":
        req="select count(idscheda) from ESNV;"
    else:
        req="select count(idscheda) from ESNA;"        
    c=db.cursor()
    c.execute(req)
    d=c.fetchall()
    return (d[0][0])


def CodiceCandidato(db,stringa):
    req="select idanagra from anagra where codice='"+stringa+"';"
    c=db.cursor()
    c.execute(req)
    d=c.fetchall()
    if d:
        return (d[0][0])
    else:
        return (-1)

def Notifica(str):
    print(("#" * (len(str)+8))) 
    print("##  "+str+"  ##")
    print(("#" * (len(str)+8))) 
    tmp=input("Premi un tasto per continuare...")
    if len(tmp) > 0:
        return(tmp)
    else:
        return


def NumeroScrutinio(db,VistaAnagra):
#    req="select max(scrutinio) from elencoschede group by scrutinio"
    if VistaAnagra=="AnagraLocale":
        req="select max(scrutinio) from ESNV group by scrutinio"
    else:
        req="select max(scrutinio) from ESNA group by scrutinio"

    c=db.cursor()
    c.execute(req)
    d=c.fetchall()
    if (d):
        return (d[len(d)-1][0])
    else:
        return (0)



def Scheda_Bianca(db,VistaAnagra,evento,user,ns,bianca,nulla,valida,schedachiusa,schedelette,annullato,nrscheda,orainizio):
#    schedachiusa=1
    if (schedachiusa==1 and bianca==1 and nulla==0):
    	progr=1
    	aperta=0
    	code=["","","","",""]
    	intesta()
    	orainizio=time.ctime()
    	orafine=""
    	schedaletta=progr
###### Aggiungere opzioni annulla e fine sequenza lettura inferiore a tre ######
    	check="s"
            
##### inserire constrollo su variabile annullato  ###########            
                   
        
#  non lo stia facendo mentre ok per normale, annulla e fine     
#        

    nrrighe=ContaRighe(db,VistaAnagra)
    k=1
    req="insert into elencoschede(scrutinio,idnumscheda,candidato,bianca,nulla,valida) values ("+ str(ns)+","+str(nrscheda)+",9998,1,0,0);" 
# query per l'inserimento della scheda 
    
    c=db.cursor()
    c.execute(req)
    d=c.fetchall()
    orafine=time.ctime()
    if VistaAnagra=="AnagraLocale": 
        req="insert into SchedeNoiVerona (evento,scrutinio,idnumscheda,postazione,aperta,chiusa,status) values('"+evento+"',"+str(int(ns))+","+ str(nrscheda)+",'"+user+"','"+orainizio+"','"+orafine+"','BIANCA');"
    else:
        req="insert into SchedeNazionale (evento,scrutinio,idnumscheda,postazione,aperta,chiusa,status) values('"+evento+"',"+str(int(ns))+","+ str(nrscheda)+",'"+user+"','"+orainizio+"','"+orafine+"','BIANCA');"
        c=db.cursor()
        c.execute(req)
        d=c.fetchall()

        c.execute("commit;")
        d=c.fetchall()
        print(); print()



def Scheda_Nulla(db,VistaAnagra,evento,user,ns,bianca,nulla,valida,schedachiusa,schedelette,annullato,nrscheda,orainizio):
#    schedachiusa=1
    if (schedachiusa==1 and bianca==0 and nulla==1):
        Progr=1
        Aperta=0
        Code=["","","","",""]
        intesta()
        OraInizio=time.ctime()
        OraFine=""
        SchedaLetta=Progr
####### UNGERE OPZIONI ANNULLA E FINE SEQUENZA LETTURA INFERIORE A TRE ######
        Check="S"
            
##### INSERIRE CONSTROLLO SU VARIABILE ANNULLATO  ###########            
                   
        
#  NON lo stia facendo mentre ok per normale, annulla e fine     
#        

        k=1
        req="INSERT INTO elencoschede(Scrutinio,idNumScheda,Candidato,Bianca,Nulla,Valida) VALUES ("+ str(ns)+","+str(nrscheda)+",9999,0,1,0);" 
# query per l'inserimento della scheda 
    
        c=db.cursor()
        c.execute(req)
        d=c.fetchall()

        orafine=time.ctime()
        if VistaAnagra=="AnagraLocale": 
            req="insert into SchedeNoiVerona (evento,scrutinio,idnumscheda,postazione,aperta,chiusa,status) values('"+evento+"',"+str(int(ns))+","+ str(nrscheda)+",'"+user+"','"+orainizio+"','"+orafine+"','NULLA');"
        else:
            req="insert into SchedeNazionale (evento,scrutinio,idnumscheda,postazione,aperta,chiusa,status) values('"+evento+"',"+str(int(ns))+","+ str(nrscheda)+",'"+user+"','"+orainizio+"','"+orafine+"','NULLA');"

        c=db.cursor()
        c.execute(req)
        d=c.fetchall()

        c.execute("commit;")
        d=c.fetchall()
        print(); print()        


def SelezionaView():
    risp=0
    while ((risp < 1) or (risp > 3)):
        intesta()
        print("\n\n\tScegli su quale set di schede vuoi lavoare: ")
        print("\n\n\n")
        print("\t\t\t(1) Noi Verona\n\n")
        print("\t\t\t(2) Noi Nazionale\n\n")
        print("\t\t\t(3) Esci\n\n")
        risp=input('\n\nSeleziona Voce Menu [ 1 - 3 ] ')
        if (risp=="1"):
            return("AnagraLocale")
            risp=int(risp)
        elif (risp=="2"):
            return("AnagraNazionale")
            risp=int(risp)
        else:
            risp=""
		
    return 

