import sys
import ChatBotModel
from connect import connect_database
import folium
from sql_model import *
import os

ROOT_DIR = os.getcwd()
FULL_DIR = os.path.join(ROOT_DIR, '.data')


def proc_help(bot, update):
    gang.sendMessage('''사용 방법에 대한 설명입니다.\n
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
    /원하는 지역코드_원하는 종목코드: 원하는 지역에 있는 종목의 시설들의 지도를 보여줍니다.\n
    ex) /1_1\n
    /시설의 id: 원하는 시설의 전화번호 및 요금을 안내합니다.\n
    ex) /19\n
    /help: 다시 한번 사용법에 대한 안내를 받습니다.\n
    /stop: 사용을 종료합니다.''')


def proc_stop(bot, update):
    gang.sendMessage('이용해주셔서 감사합니다.')


def proc_1_1(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=1).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 테니스장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_1 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_1)

        map_1_1.save('./data/map/map_1_1.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_1'>MAP Link</a>", parse_mode="HTML")


def proc_1_2(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=2).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 축구장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_2 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_2)

        map_1_2.save('./data/map/map_1_2.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_2'>MAP Link</a>", parse_mode="HTML")


def proc_1_3(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=3).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 야구장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_3 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_3)

        map_1_3.save('./data/map/map_1_3.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_3'>MAP Link</a>", parse_mode="HTML")


def proc_1_4(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=4).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 게이트볼장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_4 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_4)

        map_1_4.save('./data/map/map_1_4.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_4'>MAP Link</a>", parse_mode="HTML")


def proc_1_5(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=5).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 농구장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_5 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_5)

        map_1_5.save('./data/map/map_1_5.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_5'>MAP Link</a>", parse_mode="HTML")


def proc_1_6(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=6).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 배구장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_6 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_6)

        map_1_6.save('./data/map/map_1_6.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_6'>MAP Link</a>", parse_mode="HTML")


def proc_1_7(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=7).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 배드민턴장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_7 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_7)

        map_1_7.save('./data/map/map_1_7.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_7'>MAP Link</a>", parse_mode="HTML")


def proc_1_8(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=8).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 수상레져가 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_8 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_8)

        map_1_8.save('./data/map/map_1_8.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_8'>MAP Link</a>", parse_mode="HTML")


def proc_1_9(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=9).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 수영장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_9 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_9)

        map_1_9.save('./data/map/map_1_9.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_9'>MAP Link</a>", parse_mode="HTML")


def proc_1_10(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=10).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 인라인스케이트장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_10 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_10)

        map_1_10.save('./data/map/map_1_10.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_10'>MAP Link</a>", parse_mode="HTML")


def proc_1_11(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(region_id=1, category_id=11).all()
    if len(temp_data) == 0:
        gang.sendMessage("해당되는 잠실지구에는 족구장이 없습니다. 다른 지역을 찾아주세요.")
    else:
        map_1_11 = folium.Map(location=[temp_data[0].latitude, temp_data[0].longitude], zoom_start=17)
        for i in range(len(temp_data)):
            folium.Marker([temp_data[i].latitude, temp_data[i].longitude], popup="id:{0}, 이름:{1}".format(temp_data[i].id, temp_data[i].name)).add_to(map_1_11)

        map_1_11.save('./data/map/map_1_11.html')
        gang.sendMessage("<a href='http://13.124.61.113:5000/map_1_11'>MAP Link</a>", parse_mode="HTML")


def proc_info_42(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=42).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_63(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=63).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_64(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=64).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_65(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=65).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_66(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=66).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_119(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=119).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_120(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=120).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_168(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=168).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_172(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=72).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))


def proc_info_176(bot, update):
    session = connect_database()
    temp_data = session.query(Information).filter_by(id=176).all()
    gang.sendMessage("""시설명:{0}\n
    전화번호:{1}\n
    요금안내:{2}\n""".format(temp_data[0].name, temp_data[0].tel, temp_data[0].fare))




gang = ChatBotModel.HangangBot()

gang.add_handler('help', proc_help)
gang.add_handler('stop', proc_stop)

#지도 보여주기
gang.add_handler('1_1', proc_1_1)
gang.add_handler('1_2', proc_1_2)
gang.add_handler('1_3', proc_1_3)
gang.add_handler('1_4', proc_1_4)
gang.add_handler('1_5', proc_1_5)
gang.add_handler('1_6', proc_1_6)
gang.add_handler('1_7', proc_1_7)
gang.add_handler('1_8', proc_1_8)
gang.add_handler('1_9', proc_1_9)
gang.add_handler('1_10', proc_1_10)
gang.add_handler('1_11', proc_1_11)

#선택 시설 안내
gang.add_handler('42', proc_info_42)
gang.add_handler('63', proc_info_63)
gang.add_handler('64', proc_info_64)
gang.add_handler('65', proc_info_65)
gang.add_handler('66', proc_info_66)
gang.add_handler('119', proc_info_119)
gang.add_handler('120', proc_info_120)
gang.add_handler('168', proc_info_168)
gang.add_handler('172', proc_info_172)
gang.add_handler('176', proc_info_176)





gang.start()
