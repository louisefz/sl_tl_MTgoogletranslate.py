import werobot
from werobot import WeRoBot

robot = werobot.WeRoBot(token='louise_database9999')


@robot.handler
def hello(message):
    return 'Hello World!'


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()