

from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2
import jinja2
import os



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

from classes import Addingwords, Generating, Searching, SearchSubAnagram, DisplayWords


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        url = ''
        user = None
        url_string = ''
        if users.get_current_user():
            user = users.get_current_user()
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_string = 'login'
        template_values = {
            'url': url,
            'url_string': url_string,
            'user': user,
        }
        template = JINJA_ENVIRONMENT.get_template('templates/main.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([

    ('/', MainPage),
    ('/add', Addingwords),

    ('/search', Searching),
    ('/show', DisplayWords),
    ('/search_sub', SearchSubAnagram),
    # ('/generate/([\w|\W]+)', Generating),
    ('/generate', Generating)

], debug=True)
