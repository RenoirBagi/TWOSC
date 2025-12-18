from src.infrastructure.in_memory_repository import inMemoryPurchaseResquestRepository
from src.application.service.service_request import ServicePurchaseRequest

repository = inMemoryPurchaseResquestRepository()
service = ServicePurchaseRequest(repository)



print(repository.get_request_by_id(2))

'''
#Aqui é criado a instância do app com flask e inicia as rotas

def create_app():
    app = Flask(__name__)
    init_routes(app)
    return app

app = create_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
'''

