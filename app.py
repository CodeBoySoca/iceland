from bottle import run, template, static_file, error, request, route, BaseTemplate
import bottle

app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url


@route('/static/css/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root='static/css')

@route('/static/js/<filename:re:.*\.js>')
def js(filename):
    return static_file(filename, root='static/js')

@route('/static/images/<filename:re:.*\.jpeg')
def jpeg(filename):
    return static_file(filename, root='static/js')




@route('/', name='index')
def index():
    return template('index')

@route('/geography', name='geography')
def geography():
    return template('geography')

@route('/contact', name='contact')
def contact():
    return template('contact')

@route('/events', name='events')
def events():
    return template('events')

@route('/trade-and-invest', name='trade_and_invest')
def trade_and_invest():
    return template('trade-invest')

@route('/arts-and-culture', name='arts_and_culture')
def arts_and_culture():
    return template('arts-culture')

@route('/iceland-abroad', name='iceland_abroad')
def iceland_abroad():
    return template('iceland-abroad')




run(app,  host='localhost', port=8999)