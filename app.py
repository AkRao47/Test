from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Hello! This is your bot.')

# Set up the updater with your bot token
updater = Updater('6371494303:AAGMaUGJltbs9rBI9p3jPX77rBfPGpahvnc', use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Register the /start command handler
dp.add_handler(CommandHandler("start", start))

# Start the Bot
updater.start_polling()

# Run the bot until you send a signal to stop it
updater.idle()
