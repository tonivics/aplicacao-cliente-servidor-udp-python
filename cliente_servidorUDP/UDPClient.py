from socket import *
nomeDoServidor  = 'ServidorKubuntu'
portaDoServidor = 12000
socketDoCliente = socket(AF_INET, SOCK_DGRAM)
mensagem = input('MSG: ')
socketDoCliente.sendto(mensagem, (nomeDoServidor, portaDoServidor))
mensagemModificada, enderecoDoServidor = socketDoCliente.recvfrom(2048)
print (mensagemModificada)
socketDoCliente.close()
