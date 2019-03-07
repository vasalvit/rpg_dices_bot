import os

from telegram.ext import Updater, CommandHandler, RegexHandler

from dices import parse, calculate, InvalidFormat, InvalidDicesCount, InvalidFacesCount, minimal_dices_count, \
    maximal_dices_count, minimal_faces_count, maximal_faces_count


def command_help(_, update):
    update.message.reply_text('Example: Send "1d4" or "2d6+1" to roll dices and calculate the result')


def command_license(_, update):
    update.message.reply_text('MIT')


def command_author(_, update):
    update.message.reply_text('Alexander Vasilevsky')


def command_copyright(_, update):
    update.message.reply_text('Copyright (c) 2019 Alexander Vasilevsky')


def command_github(_, update):
    update.message.reply_text('https://github.com/vasalvit/rpg_dices_bot')


def roll_dices(_, update):
    try:
        dices = parse(update.message.text)

        value, minimal, maximal = calculate(dices)
        update.message.reply_text('%d (%d..%d)' % (value, minimal, maximal))

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
updater.dispatcher.add_handler(CommandHandler(['license'], command_license))
updater.dispatcher.add_handler(CommandHandler(['author'], command_author))
updater.dispatcher.add_handler(CommandHandler(['copyright'], command_copyright))
updater.dispatcher.add_handler(CommandHandler(['github', 'git'], command_github))

updater.dispatcher.add_handler(RegexHandler(r'.*', roll_dices))

updater.start_polling()
updater.idle()
