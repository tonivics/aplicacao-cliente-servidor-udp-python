from socket import *
portaDoServidor = 12000
socketDoServidor = socket(AF_INET, SOCK_DGRAM)
socketDoServidor.bind(('', portaDoServidor))
print ("O servidor está pronto para receber")
while 1:
	mensagem, enderecoDoCliente = socketDoServidor.recvfrom(2048)
	
	mensagemModificada = mensagem.upper()
	socketDoServidor.sendto(mensagemModificada, enderecoDoCliente)
