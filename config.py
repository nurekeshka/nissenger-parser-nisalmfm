import configparser


config = configparser.ConfigParser()
config.read('./settings.ini')

YEAR = int(config['PARSER']['YEAR'])
