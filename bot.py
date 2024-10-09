from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from gtts import gTTS
import os

# استبدل 'YOUR_TOKEN' بالتوكن الخاص بك
BOT_TOKEN = '7613699439:AAHLO_PFkOX84PihE7tEobJjABVQMcNJZ_Q'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('أهلاً! أرسل لي نصًا لتحويله إلى صوت.')

def text_to_speech(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    tts = gTTS(text=text, lang='ar')  # يمكنك تغيير اللغة هنا
    tts.save('output.mp3')
    with open('output.mp3', 'rb') as audio:
        update.message.reply_audio(audio)
    os.remove('output.mp3')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_to_speech))

    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()