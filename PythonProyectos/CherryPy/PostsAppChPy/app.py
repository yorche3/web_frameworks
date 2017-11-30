import cherrypy, os
from mako.lookup import TemplateLookup
from mako.template import Template


path   = os.path.abspath(os.path.dirname(__file__))
lookup = TemplateLookup(directories=[os.path.join(path, 'views/app')])

def serve_template(templatename, **kwargs):
    mytemplate = lookup.get_template(templatename)
    return mytemplate.render(**kwargs)

"""
RuidoVivo developed with CherryPy
"""

__author__    = 'Yorche Chory'
__contact__   = 'yorchek@gmail.com'
__date__      = 'November 2017'
__version__   = '0.1'

class App(object):
    """Controlador de la aplicación"""

    @cherrypy.expose
    def index(self):
        """Página de inicio"""
        return serve_template("index.html")

cherrypy.quickstart(App(), "/" ,"app.config")