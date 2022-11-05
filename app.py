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
    pass

@route('/contact', name='contact')
def contact():
    pass

@route('/events', name='events')
def events():
    pass

@route('/trade-and-invest', name='trade_and_invest')
def trade_and_invest():
    pass

@route('/arts-and-culture', name='arts_and_culture')
def arts_and_culture():
    pass

@route('/iceland-abroad', name='iceland_abroad')
def iceland_abroad():
    pass




run(app,  host='localhost', port=8999)