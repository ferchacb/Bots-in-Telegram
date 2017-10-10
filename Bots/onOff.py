import telepot, time, serial

from telepot.namedtuple import ReplyKeyboardMarkup
ser = serial.Serial ('COM3',9600)

def comandosTexto(msj):
    tipoDeMensaje, tipoDeChat, chatID = telepot.glance(msj)

    markup = ReplyKeyboardMarkup(keyboard=[
        ['Encendido'],
        ['Apagado']
    ])
    bot.sendMessage(chatID,'.', reply_markup=markup)

    if msj['text'] == "Encendido":
        bot.sendMessage(chatID, "Encendido")
        ser.write(b'Y')

    if msj['text'] == "Apagado":
        bot.sendMessage(chatID, "Apagado")
        ser.write(b'N')

def principal(msj):
    tipoDeMensaje, tipoDeChat, chatID = telepot.glance(msj)

    informacionEmisor = msj['from']
    emisor = informacionEmisor['first_name']

    if (tipoDeMensaje == 'text'):
        comandosTexto(msj)

    if(tipoDeMensaje == 'voice'):
        bot.sendMessage(chatID,"Lo sentimos" + emisor +
                        "aun no implemento mensajes de voz")


bot =  telepot.Bot('388226532:AAEm_p71HOktVJLWz73xrW3_ooJy2WT37xw')

bot.message_loop(principal)

while 1:
    time.sleep(10)