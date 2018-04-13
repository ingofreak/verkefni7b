#Ingólfur Óskarsson
from bottle import *
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

testlist=[]



@route('/')
def index():
    return testlist,"""
            <a href='/vara/1'>Vara 1</a><br>
            <a href='/vara/2'>Vara 2</a><br>
            <a href='/vara/3'>Vara 3</a><br>
            <a href='/vara/4'>Vara 4</a><br>
            <a href='/versla'>Versla</a><br>
            <a href='/eyda'>Eyða Vörum</a><br>"""


# Búum til session
@route('/vara/<numer>')
def byrja(numer):
    s = request.environ.get('beaker.session')

    s[numer] = 'Vara '
    #testlist.append(numer)
    s.save()
    return "Vara valin <br><a href='/'>Heim</a>"

# Athugum hvort tiltekið session sé til
@route('/versla')
def skoda():
    s = request.environ.get('beaker.session')

    vorur = str()

    for i in range(1,5):
        if s.get(str(i)):
            vorur = vorur + ("Vara "+str(i)+"<br>")
    if s.get('1') or s.get('2') or s.get('3') or s.get('4'):
        return vorur , "<br><a href='/'>Heim</a>"
    else:
        return "Ekkert í körfu!<br><a href='/'>Heim</a>"
"""
    if s.get('1'):
        return s['1'],"<br><a href='/'>Heim</a>"
    if s.get('2'):
        return s['2'],"<br><a href='/'>Heim</a>"
    if s.get('3'):
        return s['3'],"<br><a href='/'>Heim</a>"
    if s.get('4'):
        return s['4'],"<br><a href='/'>Heim</a>"
    else:
        return "Ekkert í körfu!<br><a href='/'>Heim</a>"
"""
# Eyðum session
@route('/eyda')
def eyda():
    s = request.environ.get('beaker.session')
    #eða einni vöru
    #s['1'] = None
    s.delete()
    return "Vörum eytt!<br><a href='/'>Heim</a>"

# Muna eftir app=app í run fallinu
run(app=app)