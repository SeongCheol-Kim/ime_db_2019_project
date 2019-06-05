import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from sql_model import *

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = secrets['admin_id']
        self.name = name

    def sendMessage(self, text, parse_mode=None):
        self.core.sendMessage(chat_id = self.id, text=text, parse_mode=parse_mode, disable_web_page_preview=False)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class HangangBot(TelegramBot):
    def __init__(self):
        self.token = secrets['telegram_access_token']
        TelegramBot.__init__(self, '텔레그램', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('''안녕하세요.\n
        해당 챗봇은 서울시 한강공원 내 체육시설에 대한 안내를 합니다.\n
        사용 방법에 대한 설명입니다.\n
        \n
        지역코드\n
        1:잠실지구, 2:광나루지구, 3:뚝섬지구,\n
        4:잠원지구, 5:반포지구, 6:이촌지구,\n
        7:여의도지구, 8:양화지구, 9:난지지구,\n
        10:망원지구, 11:강서지구\n
        \n
        종목코드\n
        1:Tennis, 2:Soccer, 3:Baseball,\n
        4:Gateball, 5:Basketball, 6:Volleyball,\n
        7:Badminton, 8:WaterLeisure, 9:Pool,\n
        10:InlineSkate, 11:Jokgu\n
        \n
        입력방법\n
        원하는 지역코드_원하는 종목코드: 원하는 지역에 있는 종목의 시설들의 지도를 보여줍니다.\n
        ex) /1_1\n
        시설의 id: 원하는 시설의 전화번호 및 요금을 안내합니다.\n
        ex) /19\n
        /help: 다시 한번 사용법에 대한 안내를 받습니다.\n
        /stop: 사용을 종료합니다.''')
        self.updater.start_polling()
        self.updater.idle()