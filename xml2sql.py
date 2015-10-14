__author__ = 'Tharun'

import MySQLdb as MS
import os


#contains all the unzipped stackexchange folders with their xml dumps
root_path = 'F:\Code\Python\ResearchAide\StackExchange\Test'

#Gets all immediate sub directories under root
sites = [name for name in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, name))]

#Connection to the database. The SQL Server must be running at localhost, before execution of script
connection = MS.connect(host="localhost",user="root",passwd="geek")
cursor = connection.cursor()

#All sql statements separated by ;. So splitting them.
sql_file = open('load.sql')
commands = sql_file.read().split(';')

#Loop through the stackexchange folder sites
for site in sites:
    site_path = root_path + '\\' + site
    #correcting path for usage in MySQL query
    corrected_path = site_path.replace('\\','\\\\')
    print corrected_path
    print site.split('.')[0]
    for cmd in commands:
        try:
            #Exploiting generic format strings in python to plug in values dynamically for reusing queeries.
            if 'create database' in cmd:
                newcmd= cmd.format(site.split('.')[0])
            elif 'use' in cmd:
                newcmd= cmd.format(site.split('.')[0])
            elif 'load xml' in cmd:
                newcmd= cmd.format(corrected_path)
            else:
                newcmd = cmd
            print "For {} Executing: {}".format(site,newcmd)
            cursor.execute(newcmd)

        except Exception, e:
            print e



