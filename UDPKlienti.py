import socket

serverHost='localhost'
serverPort=14000

serverS=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


print('Zgjedhni njeren prej opsioneve me poshte!\n')

print('''
1.IP 
2.NRPORTIT 
3.NUMERO  
4.ANASJELLTAS 
5.PALINDROM 
6.KOHA
7.LOJA 
8.GCF 
9.KONVERTO(Mund te konvertoni:cmNeInch,inchNeCm,kmNeMiles,mileNeKm) 
10.VITI_BRISHTE
11.TIPI_VARIABLES

        ''')


kerkesa=input('Shkruani kerkesen tuaj!')
serverS.sendto(kerkesa.encode(),(serverHost,serverPort))
pergjigjja,address=serverS.recvfrom(1024)
print('Kerkesa u procesua:'+pergjigjja.decode())
