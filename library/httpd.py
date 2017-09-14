import cherrypy
from cherrypy.lib import auth_basic
from library.logger import logger


#@cherrypy.expose
class httpd(object):

    def __init__(self):
        self._callback = None
        self._log = logger()

    def register_callback(self,_callback):
        self._callback = _callback

    @cherrypy.expose
    def single(self):
        self._callback('SINGLE',cherrypy.request.headers['Remote-Addr'])
        self._log.debug('httpd received Single')

    @cherrypy.expose
    def long(self):
        self._callback('LONG',cherrypy.request.headers['Remote-Addr'])
     #   self._log.debug('httpd received Long')

    @cherrypy.expose
    def double(self):
        self._callback('DOUBLE',cherrypy.request.headers['Remote-Addr'])
      #  self._log.debug('httpd received DOUBLE')

    @cherrypy.expose
    def touch(self):
        self._callback('TOUCH',cherrypy.request.headers['Remote-Addr'])
       # self._log.debug('httpd received TOUCH')
