# -*- coding: UTF-8 -*-
'''
@Project -> File   ：mongodb_demo -> manage
@IDE    ：PyCharm
@Author ：Mr. Dong
@Date   ：2020/6/10 0:16
'''

import pymongo


def run():
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client.mydb

    myset = db.testset
    print(myset.find_one())

if __name__ == '__main__':
    run()