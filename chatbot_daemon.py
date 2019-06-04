import sys
import ChatBotModel
import folium

def proc_rolling(bot, update):
    gang.sendMessage('데구르르..')
    sound = firecracker()
    gang.sendMessage(sound)
    gang.sendMessage('르르..')

def proc_stop(bot, update):
    gang.sendMessage('종료합니다.')
    gang.stop()

def category_region(bot, update):
    gang.sendMessage('해당 내역을 검색한 결과입니다. 찾으시는 위치는')
    category=categories()
    region=regions()
    gang.sendMessage('에 있습니다.')
    
def categories(bot,update):
    gang.sendMessage(chat_id = chat_id, text='categoryname')

def regions(bot,update):
    map=folium.Map(location=['x','y'],zoom_start=13)
    gang.sendMessage(chat_id=chat_id, text=map)

def firecracker():
    return '팡팡!'

gang = ChatBotModel.HangangBot()
gang.add_handler('rolling', proc_rolling)
gang.add_handler('stop', proc_stop)
gang.start()
