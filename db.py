# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:59:54 2021

@author: USER
"""



import pymysql
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       passwd = '123456789',
                       db = 'lccnet')
order = conn.cursor()