import os

# noinspection PyPackageRequirements
from telegram.ext import Updater, CommandHandler


def command_help(_, update):
    update.message.reply_text(
        'Example: Send "2d6+1" to roll dices and calculate the result'
    )


updater = Updater(os.environ['TELEGRAM_BOT_TOKEN'])

updater.dispatcher.add_handler(CommandHandler(['help', 'h', '?'], command_help))

updater.start_polling()
updater.idle()
