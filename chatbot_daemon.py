import sys
import ChatBotModel

def start(bot, update):
    gang.sendMessage('안녕하세요? 가천대학교 ibe_2019_프로젝트 한강지구 운동시설 찾기 봇입니다. ')
    gang.sendMessage('사용법을 위해 /help를 입력해주세요.')

def help(bot, update):
    gang.sendMessage('지구구분코드 : \n\
                    GIGU001 : 잠실, GIGU002 : 광나루, GIGU003 : 뚝섬 \n\
                        GIGU004 : 잠원, GIGU005 : 반포, GIGU006 : 이촌 \n\
                        GIGU007 : 여의도, GIGU009 : 양화, GIGU010 : 난지\n\
                        GIGU011 : 망원, GIGU012 : 망원')
    gang.sendMessage('지형지물코드 : \n\
                        ABB003 : Tennis1, AB003 : Tennis2, ABB100 : Baseball \n\
                        ABB109 : Gateball, AAB104 : Basketball, ABB101 : Volleyball \n\
                        ABB102 : Badminton, ABB201 : WaterLeisure, ABB012 : Pool \n\
                        AAB670 : lnlineSkate1, ADA037 : InlineSkate2, ABB112 : Jokgu')

def stop(bot, update):
    gang.sendMessage('감사합니다. 또 찾아주세요!')
    gang.stop()



gang = ChatBotModel.HangangBot()
gang.add_handler('start', start)
gang.add_handler('help', help)
gang.add_handler('stop', stop)
gang.start()
