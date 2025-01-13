import ptbot
import os
from pytimeparse import parse
from dotenv import load_dotenv
load_dotenv()

tg_token = os.getenv('TG_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')
bot = ptbot.Bot(tg_token)


def reply(tg_chat_id, text):
    delay_seconds=parse(text)
    message_id=bot.send_message(tg_chat_id, "Запускаю таймер")
    bot.create_countdown(delay_seconds, notify_progress, message_id=message_id)
    bot.create_timer(delay_seconds, lalal, tg_chat_id=tg_chat_id)

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)
    
def notify_progress(secs_left, message_id):
    progress = render_progressbar(secs_left, secs_left)
    bot.update_message(tg_chat_id, message_id, f"Осталось {secs_left} секунд\n{progress}")

def lalal(tg_chat_id):
    bot.send_message(tg_chat_id, "Время вышло!")


bot.reply_on_message(reply)
bot.run_bot()