import telepot, time

def principal(msj):
    tipoDeMensaje, tipoDeChat, chatID = telepot.glance(msj)
    informacionEmisor = msj['from']
    emisor = informacionEmisor['first_name']

    if (tipoDeMensaje == 'text'):
        comando = msj ['text']
        print('Comando recibido: %s' %comando)

        if 'hola' in comando:
            bot.sendMessage(chatID, "Hola !")

        if 'Todo bien?' in comando:
            bot.sendMessage(chatID, "Pura vida!")


        if 'Tengo hambre!' in comando:
            bot.sendMessage(chatID, "Que quieres comer?")

        if 'Pizza' in comando:
            bot.sendMessage(chatID, "Lets go!")

        if 'Quiero un helado' in comando:
            bot.sendMessage(chatID, "Que rico!")

        if 'Que eres?' in comando:
            bot.sendMessage(chatID, "Soy un bot!")

    if (tipoDeMensaje == 'voice'):
        bot.sendMessage(chatID,"No puedo responder a eso " + emisor + " No hemos implementado notas de voz")

bot =  telepot.Bot('324478631:AAFLI_h9sbhJSLrPXyU_ykMs6Q8uAHefO2U')
bot.message_loop(principal)

while 1:
    time.sleep(10)