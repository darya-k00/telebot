import ptbot
import os
from pytimeparse import parse
from dotenv import load_dotenv
load_dotenv()

def main():
    tg_token = os.getenv('TG_TOKEN')
    bot = ptbot.Bot(tg_token)

    def reply(chat_id, text):
        delay_seconds=parse(text)
        message_id=bot.send_message(chat_id, "Запускаю таймер")
        bot.create_countdown( delay_seconds, notify_progress, message_id=message_id, delay_seconds=delay_seconds, chat_id=chat_id)
        bot.create_timer(delay_seconds, lalal, chat_id=chat_id)

    def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
        iteration = min(total, iteration)
        percent = "{0:.1f}"
        percent = percent.format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        pbar = fill * filled_length + zfill * (length - filled_length)
        return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)
        
    def notify_progress(secs_left, delay_seconds, chat_id, message_id):
        secs_new=(delay_seconds - secs_left)
        progress = render_progressbar(delay_seconds, secs_new)
        bot.update_message(chat_id, message_id, f"Осталось {secs_left} секунд\n{progress}")

    def lalal(chat_id):
        bot.send_message(chat_id, "Время вышло!")

    bot.reply_on_message(reply)
    bot.run_bot()

if __name__=='__main__':
    main()
    
