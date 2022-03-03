import socket
from datetime import datetime
import random
import math

serverName='localhost'
serverPort=14000
serverS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverS.bind((serverName, serverPort))

#Metodat
def IP():
   return 'IP adress is: '+address[0]

def NRPORTIT():
    return 'Numri i portit te klientit eshte: '+ str(address[1])

def NUMERO(text):
    zanore=0
    bashtingellore=0
    for word in text:
        for i in word:
             if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                zanore=zanore+1
             elif i.isalpha():
                bashtingellore=bashtingellore+1
    
    return 'Numri i zanoreve ' +str(zanore)  + ',bashtingelloreve '+str(bashtingellore)

def ANASJELLTAS(text):
   
    return str(text[::-1])

def PALINDROM(text):
    
    if(text==text[::-1]):
        return "Ky tekst eshte palindrome"
    else:
        return  "Ky tekst nuk eshte palindrome"

def KOHA():
    now = datetime.now()

    current_time = now.strftime("%m:/%d:/%y:%H:%M:%S")
    return 'Koha aktuale: '+current_time


def GCF(nr1,nr2):
    return 'Faktori me i madh i perbashket '+str(math.gcd(int(nr1),int(nr2)))

def LOJA():
    randomNumbers=random.sample(range(1,36),5)
    return 'Rangu i rastesishem' +(str(sorted(randomNumbers)))



def KONVERTO(opsioni,numri):
    if opsioni == "cmNeInch":
        return 'Vlera e konvertuar' +str(numri/2.54)
    elif opsioni== "inchNeCm":
      return 'Vlera e konvertuar' +str(numri*2.54)
    elif opsioni == "kmNeMiles":
        return 'Vlera e konvertuar' +str(numri/1.609)
    elif opsioni == "mileNeKm":
        return 'Vlera e konvertuar' +str(numri*1.609)      
    else:
        return "Nuk kemi pergjigjje per opsionin qe keni dhene"


#Metodat shtese
def VITI_BRISHTE(viti):
     if (viti % 4 == 0 and viti % 100 != 0):
        return  'eshte viti i Brishte'
     elif viti % 400 == 0:
       return  'eshte viti i Brishte'
     else:
       return 'nuk eshte viti i Brishte'

def TIPI_VARIABLES(n):
    if n.isnumeric():
        return 'Variabla eshte nje numer'
    else:
       return 'Variabla nuk eshte nje numer'
while True:
    kerkesa, address = serverS.recvfrom(1024)
   

    pergjigjja = ''

   
    
    #e procesojme kerkesen e klientit
    if kerkesa[0] == 'IP':
            pergjigjja = IP()
    elif kerkesa[0] == 'NRPORTIT':
            pergjigjja = NRPORTIT()
    elif kerkesa[0] == 'NUMERO':
             if len(kerkesa)<2:
                 pergjigjja="Ju duhet te shtypni nje TEKST qe te implementohet funksioni"
             else:
                 pergjigjja = NUMERO(kerkesa[1:])
    elif kerkesa[0] == 'ANASJELLTAS':
             if len(kerkesa)<2:
                 pergjigjja="Ju duhet te shtypni nje TEKST qe te implementohet funksioni"
             else:
                 pergjigjja = ANASJELLTAS(kerkesa[1])
    elif kerkesa[0] == 'PALINDROM':
              if len(kerkesa)<2:
                 pergjigjja="Ju duhet te shtypni nje TEKST qe te implementohet funksioni"
              else:
                 pergjigjja = PALINDROM(kerkesa[1])
    elif kerkesa[0] == 'KOHA':
            pergjigjja = KOHA()
    elif kerkesa[0] == 'LOJA':
        pergjigjja = LOJA()
    elif kerkesa[0] == 'GCF':
            if len(kerkesa)<3:
                pergjigjja="Ju duhet te shtypni 2 numra qe te implementohet funksioni"
            else:
                pergjigjja = GCF(int(kerkesa[1]), int(kerkesa[2]))
    elif kerkesa[0] == 'KONVERTO':
            if len(kerkesa)<3:
                pergjigjja="Ju duhet te shtypni llojin e konvertimit dhe numrin  qe te implementohet funksioni"
            else:
                pergjigjja = KONVERTO(kerkesa[1],float(kerkesa[2]))
    elif kerkesa[0] == 'VITI_BRISHTE':
            if len(kerkesa)<2:
                pergjigjja="Ju duhet te shtypni vitin qe te implementohet funksioni"
            else:
                pergjigjja = VITI_BRISHTE(int(kerkesa[1]))
    elif kerkesa[0] == 'TIPI_VARIABLES':
            if len(kerkesa)<2:
                pergjigjja="Ju duhet te shtypni nje variabel qe te implementohet funksioni"
            else:
                pergjigjja = TIPI_VARIABLES(kerkesa[1])
    else: 
        pergjigjja = "Keni shenuar njeren nga kerkesen me shkronja te vogla ose gabim"
        

          
    print('Pergjigjja nga server: ' +pergjigjja)
    kerkesa=pergjigjja.encode()
    serverS.sendto(kerkesa,address)
    

