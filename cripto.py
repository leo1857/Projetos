#criptografia com chave composta 

def cript(x:str,y:str):
    texto = ''
    x.replace(y,'abc')
    for i in range(0,len(x)):
        texto = texto + chr(ord(x[i])+6)
    return texto


def descript(x:str,y:str):
    texto = ''
    for i in range(0,len(x)):
        texto = texto + chr(ord(x[i])-6)
    texto.replace('abc',y)
    return texto

#comeco do programa mesmo
print('Bem vindo ao centro de criptografias.')
teste = input('Deseja criptografar ou descriptografar uma mensagem?(Criptografar/Descriptografar) ').lower()
while (teste != 'descriptografar') and (teste != 'criptografar'):
    print('nao consegui entender, poderia repetir?')
    teste = input('Deseja criptografar ou descriptografar uma mensagem?(Criptografar/Descriptografar) ').lower()


if teste == 'criptografar':
    mensagem = input('Por favor digite a mensagem que deseja ser criptografada: \n').lower()
    chave = input('Agora digite a chave para ser usada na sua criptografia (a chave deve ter 3 letras, contando espacos, que estejam dentro da mensagem digitada anteriormente): \n').lower()

    #teste da chave se esta de acordo com o pedido
    while (len(chave)!= 3) or (chave not in mensagem):
        print('A chave digitada nao foi valida. A chave deve ter 3 letras que estejam dentro da mensagem que deseja criptografar.')
        chave = input('Digite novamente a chave: \n').lower()

    print('lembre-se de so dar a sua chave para quem voce quer que saiba da mensagem')
    mensagem = cript(mensagem,chave)
    print('sua mensagem foi criptografada com sucesso!!\nAqui esta a sua mensagem criptografada:')
    print(mensagem)

    cont = input('deseja descriptografar a sua mensagem? (S/N): ').lower()
    if cont == 's':
        mensagem = descript(mensagem,chave)
        print('sua mensagem foi recuperada com sucesso!!\nA qui esta a mensagem original:')
        print(mensagem)
    else:
        print('para retornar a sua mensagem ao que era antes inicie novamente esse programa quando quiser e escolha decodificar ao iniciar')
    print('Obrigado pelo uso, ate a proxmia')

else:
    mensagem = input('Digite a mensagem criptografada, exatamente igual lhe foi entregue:\n')
    chave = input('e agora a chave que voce usou para criptografar a sua mensagem: \n')
    
    mensagem = descript(mensagem,chave)
    print('sua mensagem foi recuperada com sucesso!!\nA qui esta a mensagem original:')
    print(mensagem)


