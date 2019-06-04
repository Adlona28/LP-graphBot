import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import gestorComandes as gcom

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola!")

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sento no ser de gran ajuda")

def author(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Adrian Lozano Navarro\nadrian.lozano.navarro@est.fib.upc.edu")

def graph(bot, update, args, user_data):
    try:
        user_data['graph'] = gcom.graph(args)
        bot.send_message(chat_id=update.message.chat_id, text="Ok")
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

def nodes(bot, update, user_data):
    if 'graph' not in user_data:
        resposta = "Encara no s'ha generat cap graph, pots generar-ne un amb la comanda /graph"
    else:
        resposta = str(user_data['graph'].number_of_nodes())
    bot.send_message(chat_id=update.message.chat_id, text=resposta)

def edges(bot, update, user_data):
    if 'graph' not in user_data:
        resposta = "Encara no s'ha generat cap graph, pots generar-ne un amb la comanda /graph"
    else:
        resposta = str(user_data['graph'].number_of_edges())
    bot.send_message(chat_id=update.message.chat_id, text=resposta)

def components(bot, update, user_data):
    if 'graph' not in user_data:
        resposta = "Encara no s'ha generat cap graph, pots generar-ne un amb la comanda /graph"
    else:
        resposta = str(gcom.components(user_data['graph']))
    bot.send_message(chat_id=update.message.chat_id, text=resposta)

def localitzacio(bot, update, user_data):
    user_data['lat'], user_data['lon'] = update.message.location.latitude, update.message.location.longitude
    bot.send_message(chat_id=update.message.chat_id, text="Rebut, guardo la teva posició")

def plotpop(bot, update, args, user_data):
    if 'graph' not in user_data:
        resposta = "Encara no s'ha generat cap graph, pots generar-ne un amb la comanda /graph"
        bot.send_message(chat_id=update.message.chat_id, text=resposta)
    else:
        try:
            if len(args) == 1:
                if 'lat' not in user_data:
                    resposta = "No tinc la teva localització, me la pots enviar o dir-me unes coordenades a la comanda: /plotpop dist [lat] [lon]"
                    bot.send_message(chat_id=update.message.chat_id, text=resposta)

                else:
                    image = gcom.plotpot(args[0], user_data['lat'], user_data['lon'], user_data['graph'])
                    bot.send_photo(chat_id=update.message.chat_id, photo = image)

            elif len(args) == 3:
                image = gcom.plotpot(args[0], args[1], args[2], user_data['graph'])
                bot.send_photo(chat_id=update.message.chat_id, photo = image)

            else:
                resposta = "Usage: /plotpop dist [lat] [lon]"
                bot.send_message(chat_id=update.message.chat_id, text=resposta)

        except Exception as e:
            print(e)
            bot.send_message(chat_id=update.message.chat_id, text='💣')

TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('graph', graph, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('nodes', nodes, pass_user_data=True))
dispatcher.add_handler(CommandHandler('edges', edges, pass_user_data=True))
dispatcher.add_handler(CommandHandler('components', components, pass_user_data=True))
dispatcher.add_handler(MessageHandler(Filters.location, localitzacio, pass_user_data=True))
dispatcher.add_handler(CommandHandler('plotpop', plotpop, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('plotgraph', start, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('route', start, pass_args=True, pass_user_data=True))
updater.start_polling()