import configparser
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'lhSRoUx9rN$@~n|qVK,s&u~I^E;YWI'

def init(app):
    config = configparser.ConfigParser()
    try:
        print("INIT FUNCTION")
        config_location = "Workbook/ect/defaults.cfg"
        config.read(config_location)

        app.config['DEBUG'] = config.get("config","debug")
        app.config['ip_address'] = config.get("config","ip_address")
        app.config['port'] = config.get("config","port")
        app.config['url'] = config.get("config","url")
    except:
        print("Could not read configs from: ", config_location)

init(app)

@app.route('/')
def root():
    return "Hello testing config & sessions"

@app.route('/config')
def config():
    s = []
    s.append('debug:'+str(app.config['DEBUG']))
    s.append('port:' + app.config['port'])
    s.append('url:' + app.config['url'])
    s.append('ip_address:'+app.config['ip_address'])
    return ', '.join(s)


if __name__ == '__main__':
    init(app)
    app.run(
        host=app.config['ip_address'],
        port=int(app.config['port']))
