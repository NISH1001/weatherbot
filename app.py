import falcon

class BotAPI:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'I am a bot...'

api = application = falcon.API()

bot = BotAPI()

# things will handle all requests to the '/things' URL path
api.add_route('/', bot)

