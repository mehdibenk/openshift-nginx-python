#!/usr/bin/env python
import imp
import os

try:
   zvirtenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'],
                           'virtenv', 'bin', 'activate_this.py')
   execfile(zvirtenv, dict(__file__ = zvirtenv) )
except IOError:
   pass

def run_cherrypy_server(app, ip, port=8080):
   from cherrypy import wsgiserver
   server = wsgiserver.CherryPyWSGIServer(
               (ip, port), app, server_name=os.environ['OPENSHIFT_APP_DNS'])
   server.start()

def run_gevent_server(app, ip, port=8080):
   from gevent.pywsgi import WSGIServer
   WSGIServer((ip, port), app).serve_forever()

def run_simple_httpd_server(app, ip, port=8080):
   from wsgiref.simple_server import make_server
   make_server(ip, port, app).serve_forever()

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
# 

#
#  main():
#
if __name__ == '__main__':
   ip   = os.environ['OPENSHIFT_PYTHON_WSGI_IP']
   port = int(os.environ['OPENSHIFT_PYTHON_WSGI_PORT'])
   zapp = imp.load_source('application', 'wsgi/application')

   #  Use gevent if we have it, if fails try cherrypy, otherwise run a simple httpd server.
   try:
      run_gevent_server(zapp.application, ip, port)
   except:
       print("gevent probably not installed - trying CherryPy ...")
       try:
           run_cherrypy_server(zapp.application, ip, port)
       except:
           print("cherrypy probably not installed - using default simple server ...")
           run_simple_httpd_server(zapp.application, ip, port)
