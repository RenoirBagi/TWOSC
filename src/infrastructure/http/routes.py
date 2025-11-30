from src.application.controller.request_controller import 

def init_routes(app):
    @app.route('/')
    def home():
        return 'Hello, this aplications is up and running'
    
    @app.route('/api/requests', methods=['POST'])
    def create_request():
        return
         