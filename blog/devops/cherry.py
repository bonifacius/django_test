import logging.config
import os

import cherrypy
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from paste.translogger import TransLogger

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

app = get_wsgi_application()
app_logger = TransLogger(app, setup_console_handler=True)

logging.config.dictConfig(settings.LOGGING)

cherrypy.config.update({
    'server.socket_host': "0.0.0.0",
    'server.socket_port': 8080,
    'server.thread_pool': 4,
})

cherrypy.tree.graft(app_logger, "/")

cherrypy.engine.start()
cherrypy.engine.block()
