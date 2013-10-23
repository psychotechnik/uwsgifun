import uwsgi

def application(env, start_response):
    start_response('200 Ok', [('Content-type', 'text/plain')])
    yield "hello"
    uwsgi.log("this is supposed to be a message to the log srv. read me?")
