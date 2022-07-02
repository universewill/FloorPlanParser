#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import base64
import time

dir = 'test.jpg'
# read floor plan image as base64
with open(dir, 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    data = 'data:image/jpeg;base64,%s' % s
    # print(data)


# call house parser service to get json result
# you should change the 'xxx' to your account (contact universe.will@gmail.com to buy an account)
paras = {'image':(None, data), 'user_name':(None, 'xxx'), 'password':(None, 'xxx')}
ret = requests.post('http://192.168.31.61:9595/house_parser_json', files=paras)

print('house parser json result:')
print(ret.text)

# if your user account is valid, you will get json result like below
# house parser json result:
# {"wall": [{"start_point": {"x": 53, "y": 108}, "end_point": {"x": 74, "y": 74}}, {"start_point": {"x": 55, "y": 108}, "end_point": {"x": 55, "y": 55}}, {"start_point": {"x": 127, "y": 108}, "end_point": {"x": 151, "y": 151}}, {"start_point": {"x": 139, "y": 108}, "end_point": {"x": 139, "y": 139}}, {"start_point": {"x": 216, "y": 108}, "end_point": {"x": 234, "y": 234}}, {"start_point": {"x": 228, "y": 108}, "end_point": {"x": 228, "y": 228}}, {"start_point": {"x": 284, "y": 108}, "end_point": {"x": 308, "y": 308}}, {"start_point": {"x": 304, "y": 108}, "end_point": {"x": 304, "y": 304}}, {"start_point": {"x": 336, "y": 108}, "end_point": {"x": 362, "y": 362}}, {"start_point": {"x": 359, "y": 108}, "end_point": {"x": 359, "y": 359}}, {"start_point": {"x": 55, "y": 115}, "end_point": {"x": 65, "y": 65}}, {"start_point": {"x": 132, "y": 115}, "end_point": {"x": 139, "y": 139}}, {"start_point": {"x": 27, "y": 202}, "end_point": {"x": 27, "y": 27}}, {"start_point": {"x": 27, "y": 203}, "end_point": {"x": 110, "y": 110}}, {"start_point": {"x": 94, "y": 203}, "end_point": {"x": 94, "y": 94}}, {"start_point": {"x": 133, "y": 203}, "end_point": {"x": 151, "y": 151}}, {"start_point": {"x": 174, "y": 203}, "end_point": {"x": 309, "y": 309}}, {"start_point": {"x": 330, "y": 203}, "end_point": {"x": 363, "y": 363}}, {"start_point": {"x": 129, "y": 239}, "end_point": {"x": 129, "y": 129}}, {"start_point": {"x": 129, "y": 239}, "end_point": {"x": 178, "y": 178}}, {"start_point": {"x": 178, "y": 239}, "end_point": {"x": 178, "y": 178}}, {"start_point": {"x": 359, "y": 240}, "end_point": {"x": 359, "y": 359}}, {"start_point": {"x": 94, "y": 256}, "end_point": {"x": 94, "y": 94}}, {"start_point": {"x": 24, "y": 260}, "end_point": {"x": 100, "y": 100}}, {"start_point": {"x": 121, "y": 260}, "end_point": {"x": 130, "y": 130}}, {"start_point": {"x": 129, "y": 287}, "end_point": {"x": 129, "y": 129}}, {"start_point": {"x": 125, "y": 288}, "end_point": {"x": 135, "y": 135}}, {"start_point": {"x": 153, "y": 288}, "end_point": {"x": 179, "y": 179}}, {"start_point": {"x": 25, "y": 365}, "end_point": {"x": 46, "y": 46}}, {"start_point": {"x": 111, "y": 365}, "end_point": {"x": 140, "y": 140}}, {"start_point": {"x": 166, "y": 365}, "end_point": {"x": 209, "y": 209}}, {"start_point": {"x": 327, "y": 365}, "end_point": {"x": 362, "y": 362}}], "win": [{"start_point": {"x": 73, "y": 108}, "end_point": {"x": 128, "y": 128}}, {"start_point": {"x": 149, "y": 108}, "end_point": {"x": 219, "y": 219}}, {"start_point": {"x": 232, "y": 108}, "end_point": {"x": 285, "y": 285}}, {"start_point": {"x": 307, "y": 108}, "end_point": {"x": 337, "y": 337}}, {"start_point": {"x": 65, "y": 115}, "end_point": {"x": 133, "y": 133}}, {"start_point": {"x": 34, "y": 203}, "end_point": {"x": 52, "y": 52}}, {"start_point": {"x": 46, "y": 365}, "end_point": {"x": 112, "y": 112}}, {"start_point": {"x": 140, "y": 365}, "end_point": {"x": 167, "y": 167}}, {"start_point": {"x": 179, "y": 368}, "end_point": {"x": 359, "y": 359}}], "door": [{"start_point": {"x": 110, "y": 203}, "end_point": {"x": 134, "y": 134}}, {"start_point": {"x": 151, "y": 203}, "end_point": {"x": 175, "y": 175}}, {"start_point": {"x": 308, "y": 203}, "end_point": {"x": 331, "y": 331}}, {"start_point": {"x": 359, "y": 207}, "end_point": {"x": 359, "y": 359}}, {"start_point": {"x": 94, "y": 235}, "end_point": {"x": 94, "y": 94}}, {"start_point": {"x": 99, "y": 260}, "end_point": {"x": 122, "y": 122}}, {"start_point": {"x": 135, "y": 288}, "end_point": {"x": 154, "y": 154}}, {"start_point": {"x": 209, "y": 365}, "end_point": {"x": 328, "y": 328}}], "bay-window": [{"start_point": {"x": 232, "y": 109}, "end_point": {"x": 296, "y": 296}}, {"start_point": {"x": 60, "y": 110}, "end_point": {"x": 135, "y": 135}}, {"start_point": {"x": 144, "y": 110}, "end_point": {"x": 225, "y": 225}}, {"start_point": {"x": 32, "y": 344}, "end_point": {"x": 124, "y": 124}}, {"start_point": {"x": 132, "y": 345}, "end_point": {"x": 173, "y": 173}}], "door_width": 20, "wall_width": 5.194805194805195}
