import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import gestorComandes as gcom
import actualitzaDades as actu

def start(bot, update, user_data):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! Actualitzo les dades i comencem")
    actu.comprovaActualitzat()
    bot.send_message(chat_id=update.message.chat_id, text="Som-hi!")
    user_data['graph'] = gcom.graph(["300", "100000"])

def help(bot, update):
    infoAuthor = "/author: Per obtenir les dades de l'autor d'aquest bot tan simpàtic\n\t"
    infoGraph = "/graph (distance) (population): Creo un graf geomètric amb les ciutats del món que tenen més habitants que el total d'habitants donat\n\t"
    infoNodes = "/nodes: Retorno el total de nodes de l'últim graf generat\n\t"
    infoEdges = "/edges: Retorno el total de d'aristes de l'últim graf generat\n\t"
    infoComponents = "/components: Retorno el total de components connexos de l'últim graf generat\n\t"
    infoPlotPop = "/plotpop (dist) [(lat), (lon)]: Donada una distància i una posició, mostro el mapa amb les ciutats que es troben a distància menor o igual a dist, si no m'indiques una posició utilitzo l'última posició que m'hagis enviat\n\t"
    infoPlotGraph = "/plotgraph (dist) [(lat), (lon)]: Donada una distància i una posició, mostro el mapa amb el graph de la zona a un radi de dist dist, si no m'indiques una posició utilitzo l'última posició que m'hagis enviat\n\t"
    infoRoute = "/route (src) (dst): Calculo i mostro un mapa amb la ruta més curta entre src i dst, la sintàxi per donar src i dst és 'Nom, codi_país'"
    ajuda = "Aquestes són les comendes que entenc, amb una petita descripció:\n\t"+infoAuthor+infoGraph+infoNodes+infoEdges+infoComponents+infoPlotPop+infoPlotGraph+infoRoute
    bot.send_message(chat_id=update.message.chat_id, text=ajuda)

def author(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Adrian Lozano Navarro\nadrian.lozano.navarro@est.fib.upc.edu")

def graph(bot, update, args, user_data):
    if len(args) != 2:
        resposta = "Aquesta comanda s'utilitza així: /graph distance population"
        bot.send_message(chat_id=update.message.chat_id, text=resposta)
    else:
        try:
            if int(args[0]) > 1000:
                args[0] = 1000
            if int(args[1]) < 50000:
                args[1] = 50000
            user_data['graph'] = gcom.graph(args)
            bot.send_message(chat_id=update.message.chat_id, text="Ok")
        except Exception as e:
            print(e)
            bot.send_message(chat_id=update.message.chat_id, text='💣')

def nodes(bot, update, user_data):
    resposta = str(user_data['graph'].number_of_nodes())
    bot.send_message(chat_id=update.message.chat_id, text=resposta)

def edges(bot, update, user_data):
    resposta = str(user_data['graph'].number_of_edges())
    bot.send_message(chat_id=update.message.chat_id, text=resposta)

def components(bot, update, user_data):
    resposta = str(gcom.components(user_data['graph']))
    bot.send_message(chat_id=update.message.chat_id, text=resposta)

def localitzacio(bot, update, user_data):
    user_data['lat'], user_data['lon'] = update.message.location.latitude, update.message.location.longitude
    bot.send_message(chat_id=update.message.chat_id, text="Rebut, guardo la teva posició")

def plotpop(bot, update, args, user_data):
    try:
        if len(args) == 1:
            if 'lat' not in user_data:
                resposta = "No tinc la teva localització, me la pots enviar o dir-me unes coordenades a la comanda: /plotpop dist [lat] [lon]"
                bot.send_message(chat_id=update.message.chat_id, text=resposta)

            else:
                gcom.plotpot(args[0], user_data['lat'], user_data['lon'], user_data['graph'])
                bot.send_photo(chat_id=update.message.chat_id, photo = open('plotpop.png', 'rb'))

        elif len(args) == 3:
            print('me da los datos')
            gcom.plotpot(args[0], args[1], args[2], user_data['graph'])
            bot.send_photo(chat_id=update.message.chat_id, photo = open('plotpop.png', 'rb'))

        else:
            resposta = "Aquesta comanda s'utilitza així: /plotpop dist [lat] [lon]"
            bot.send_message(chat_id=update.message.chat_id, text=resposta)

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

def plotgraph(bot, update, args, user_data):
    try:
        if len(args) == 1:
            if 'lat' not in user_data:
                resposta = "No tinc la teva localització, me la pots enviar o dir-me unes coordenades a la comanda: /plotgraph dist [lat] [lon]"
                bot.send_message(chat_id=update.message.chat_id, text=resposta)

            else:
                gcom.plotgraph(args[0], user_data['lat'], user_data['lon'], user_data['graph'])
                bot.send_photo(chat_id=update.message.chat_id, photo = open('plotgraph.png', 'rb'))

        elif len(args) == 3:
            gcom.plotgraph(args[0], args[1], args[2], user_data['graph'])
            bot.send_photo(chat_id=update.message.chat_id, photo = open('plotgraph.png', 'rb'))

        else:
            resposta = "Aquesta comanda s'utilitza així: /plotgraph dist [lat] [lon]"
            bot.send_message(chat_id=update.message.chat_id, text=resposta)

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

def route(bot, update, args, user_data):
    if len(args) != 4:
        resposta = "Aquesta comanda s'utilitza així: /route |Source city| |Source country code| |Destination city| |Destination country code|"
        bot.send_message(chat_id=update.message.chat_id, text=resposta)
    else:
        try:
            gcom.route(args, user_data['graph'])
            bot.send_photo(chat_id=update.message.chat_id, photo = open('plotroute.png', 'rb'))
        except Exception as e:
            print(e)
            bot.send_message(chat_id=update.message.chat_id, text='💣')

TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start, pass_user_data=True))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('graph', graph, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('nodes', nodes, pass_user_data=True))
dispatcher.add_handler(CommandHandler('edges', edges, pass_user_data=True))
dispatcher.add_handler(CommandHandler('components', components, pass_user_data=True))
dispatcher.add_handler(MessageHandler(Filters.location, localitzacio, pass_user_data=True))
dispatcher.add_handler(CommandHandler('plotpop', plotpop, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('plotgraph', plotgraph, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('route', route, pass_args=True, pass_user_data=True))

updater.start_polling()