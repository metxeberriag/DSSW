import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body><head><link rel="stylesheet" href="/styles/main_eu.css"></head>')
        self.response.out.write('<p>Kaixo Mundua!</p><img src="/images/kaixo.gif" />')
        self.response.out.write('</body></html>')
        
class EsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body><head><link rel="stylesheet" href="/styles/main_es.css"></head>')
        self.response.out.write('<p>Hola Mundo!</p><img src="/images/kaixo.gif" />')
        self.response.out.write('</body></html>')
        
class EnHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body><head><link rel="stylesheet" href="/styles/main_en.css"></head>')
        self.response.out.write('<p>Hello World!</p><img src="/images/kaixo.gif" />')
        self.response.out.write('</body></html>')
			
app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/es', EsHandler),
	('/en', EnHandler),
], debug=True)


		