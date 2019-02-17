import os

from telegram.ext import Updater, CommandHandler, RegexHandler

from dices import parse, calculate


def command_help(_, update):
    update.message.reply_text(
        'Example: Send "1d4" or "2d6+1" to roll dices and calculate the result'
    )


def roll_dices(bot, update):
    dices = parse(update.message.text)
    if not tuple:
        return command_help(bot, update)

    result = calculate(dices)

    update.message.reply_text(str(result))


updater = Updater(os.environ['TELEGRAM_BOT_TOKEN'])

updater.dispatcher.add_handler(CommandHandler(['help', 'h', '?'], command_help))
updater.dispatcher.add_handler(RegexHandler(r'.*', roll_dices))

updater.start_polling()
updater.idle()
