import os

from telegram.ext import Updater, CommandHandler, RegexHandler
from string import Template

from dices import parse, calculate, InvalidFormat, InvalidDicesCount, InvalidFacesCount, minimal_dices_count, \
    maximal_dices_count, minimal_faces_count, maximal_faces_count


def command_help(_, update):
    update.message.reply_text(
        'Example: Send "1d4" or "2d6+1" to roll dices and calculate the result'
    )


def roll_dices(bot, update):
    try:
        dices = parse(update.message.text)

        result = calculate(dices)
        update.message.reply_text(str(result))

    except InvalidFormat as exc:
        update.message.reply_text('Error: Invalid format %s' % exc.format)

    except InvalidDicesCount as exc:
        update.message.reply_text(
            'Error: Invalid dices count %d (min %d, max %d)' % (exc.dices, minimal_dices_count, maximal_dices_count))

    except InvalidFacesCount as exc:
        update.message.reply_text(
            'Error: Invalid faces count %d (min %d, max %d)' % (exc.faces, minimal_faces_count, maximal_faces_count))

    except:
        update.message.reply_text('Error: Unknown')


updater = Updater(os.environ['TELEGRAM_BOT_TOKEN'])

updater.dispatcher.add_handler(CommandHandler(['help', 'h', '?'], command_help))
updater.dispatcher.add_handler(RegexHandler(r'.*', roll_dices))

updater.start_polling()
updater.idle()
