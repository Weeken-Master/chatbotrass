# from bs4 import BeautifulSoup
# import csv
# import urllib.request
# import ssl
# import json
# import requests
# import os
# import html
# import random
# import pathlib

from typing import Any, Text, Dict, List
# import pymysql.cursors
# import pymysql

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import gc
import requests
Text ="aaaaaaaaaaaaaa"
try:
    connection = pymysql.connect(host="localhost", user="root", passwd="", db="flyseo_db")  
except:
    pass


def a():
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM registration_history"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()



# goi ý tính năng


class act_suggestions(Action):
    def name(self) -> Text:
        return "action_tinhnang"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
            test_carousel = {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": "😆 Đăng ký môn học",
                            # "subtitle": "Nạp điểm",
                            "image_url": "images/5138237.jpg",
                            "dims": {
                            "width": 50,
                            "height": 50,
                            },
                            "buttons": [
                                {
                                    "title": "Đăng ký môn học",
                                    "type": "postback",
                                    "payload": "Đăng ký môn học"
                                }
                            ]
                            },

                            {
                            "title": "😍Thông tin",
                            # "subtitle": "Nạp điểm",
                            "image_url": "images/5147268.jpg",
                            "dims": {
                            "width": 50,
                            "height": 50,
                            },
                            "buttons": [
                                {
                                    "title": "😄Thông tin admin",
                                    "type": "postback",
                                    "payload": "Thông tin admin"
                                },
                                {
                                    "title": "😄Thông tin gói cước",
                                    "type": "postback",
                                    "payload": "Thông tin gói cước"
                                }
                            ]
                            
                            },
                            
                        ]
                    }
                }
            dispatcher.utter_message(text="Hệ thống có thể giúp gì ah!")
            dispatcher.utter_message(attachment=test_carousel)
        except:
            pass
        return []
      
      
class ValidateSimpleForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_dang_ky_form"
   
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Filter entities to find 'mssv_sv'
        masv= next(tracker.get_latest_entity_values("mssv_sv"), None)
        mamonhoc= next(tracker.get_latest_entity_values("mamon_monhoc"), None)
        # Get the entity value from the most recent user message
       
        print(masv)
        # chỗ này query db  kiểm tra mssv đó có tồn tại ko , nêys ko bắt nhập lại
        if(mamonhoc!= None and masv == None):
            dispatcher.utter_message(text=f"Mã sinh viên chưa hợp lệ, Vui lòng nhập đúng mã sinh viên với cú pháp: Mã số sinh viên: 'mã số', Mã môn:'mã số' ")
        if(masv != None and mamonhoc == None):
            dispatcher.utter_message(text=f"Mã môn học đăng ký chưa hợp lệ, Vui lòng nhập đúng mã với cú pháp: Mã số sinh viên: 'mã số', Mã môn:'mã số' ")
        if(mamonhoc == None and masv == None):
            dispatcher.utter_message(text=f"Vui lòng nhập đúng mã với cú pháp: Mã số sinh viên: 'mã số', Mã môn:'mã số' ")
        if(mamonhoc != None and masv != None):
            dispatcher.utter_message(text=f" Hệ thống sẽ đăng ký khoá học cho bạn với thông tin!\n Mã số sinh viên là {masv}  và  mã môn học {mamonhoc}")
     


