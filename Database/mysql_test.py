#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:55:28 2019

@author: donghoon
"""

import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='ehdgns4232',db='mysql')

cur=conn.cursor()
cur.execute("USE test1")

def store(comment, num, tablename):
    cur.execute(
        "INSERT INTO url1 (title, content) VALUES (\"%s\",\"%s\")",(comment, num)
    )
    cur.connection.commit()
    print("성공")

comment="Toobig"
tablename="url1"
store(comment,500,tablename)