import mysql
import mysql.connector
import pymysql


mydb = mysql.connector.connect(
    host ="localhost", user ="root", password= "insecure",  database= "Infinity cafe", port= "33066")

cursor = mydb.cursor()




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'db': {
            'level': 'INFO',
            'class': 'path.to.handlers.DBHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'WARN',
        },
        'log': {
            'level': 'DEBUG',
            'handlers': ['db', 'console'],
        },
    },
}