uwsgifun
========

a bunch of test apps meant to be run under uWSGI server







uwsgi -H /var/local/venv/uwsgifun --show-config --py-autoreload 3 --master --socket 127.0.0.1:7310 --module simple_app


uwsgi -H /var/local/venv/uwsgifun --show-config --py-autoreload 3 --master --socket 127.0.0.1:7310 --module werkzeug.testapp:test_app


--zeromq tcp://127.0.0.1:9999,tcp://127.0.0.1:9998

uwsgi -H /var/local/venv/uwsgifun --show-config --master --socket 127.0.0.1:7320 zeromq:tcp://127.0.0.1:9191  --module werkzeug.testapp:test_app

uwsgi -H /var/local/venv/uwsgifun --show-config --master --socket 127.0.0.1:7320 --logger zeromq:tcp://127.0.0.1:9191 --log-encoder 'json {"unix":${unix}, "msg":"${msg}"}'   --mule write_to_logger


#emperor
#   Sending SIGUSR1 to the emperor will print vassal status in its log.
#   Sending SIGHUP to the Emperor will reload all vassals
./uwsgi --emperor /opt/apps --binary-path /usr/local/bin/uwsgi