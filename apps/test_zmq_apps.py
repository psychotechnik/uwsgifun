import uwsgi
import zmq
import os

print("!!! uWSGI version:", uwsgi.version)


def run_forwarder():
    sub_addr = 'tcp://*:5759'
    pub_addr = 'tcp://*:5760'
    print "starting forwarder device. sub: '%s', pub: '%s' " % (sub_addr, pub_addr)
    print os.getpid()

    backend = None
    frontend = None
    context = None

    try:
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.SUB)
        frontend.bind(sub_addr)
        #print "started forwarder with subs bound at '%s'" % sub_addr

        frontend.setsockopt(zmq.SUBSCRIBE, "")

        # Socket facing services
        backend = context.socket(zmq.PUB)
        backend.bind(pub_addr)
        #print "started forwarder with pub bound at '%s'" % pub_addr

        zmq.device(zmq.FORWARDER, frontend, backend)
    except Exception, e:
        print e
        print "bringing down zmq device"
    finally:
        if frontend:
            frontend.close()
        if backend:
            backend.close()
        if context:
            context.term()


def log_srv():
    print os.getpid()
    ctx = zmq.Context()

    puller = ctx.socket(zmq.PULL)
    puller.bind("tcp://127.0.0.1:9191")

    while True:
        message = puller.recv()
        print message,


#uwsgi.post_fork_hook = run_forwarder
uwsgi.post_fork_hook = log_srv


def application(env, start_response):
    start_response('200 Ok', [('Content-type', 'text/plain')])
    yield "hello"
    yield "hello again."
