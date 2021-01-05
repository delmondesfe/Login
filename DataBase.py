import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Fe270495',
                             db='usuarios',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print('Conectado ao DB')