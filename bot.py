import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import gestorComandes as gcom

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola!")

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sento no ser de gran ajuda")

def author(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Adrian Lozano Navarro\nadrian.lozano.navarro@est.fib.upc.edu")

def graph(bot, update, args, user_data):
    print('hago la llamada')
    user_data['graph'] = gcom.graph(args)
    print('vuelvo de la llamada')
    bot.send_message(chat_id=update.message.chat_id, text="Ok")

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
        resposta = str(nx.number_connected_components(user_data['graph']))
    bot.send_message(chat_id=update.message.chat_id, text=resposta)


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
dispatcher.add_handler(CommandHandler('plotpop', start, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('plotgraph', start, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('route', start, pass_args=True, pass_user_data=True))
updater.start_polling()