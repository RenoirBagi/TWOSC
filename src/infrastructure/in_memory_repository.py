from src.domain.repository import PurchaseRequestRepositoryInterface

class inMemoryPurchaseResquestRepository(PurchaseRequestRepositoryInterface):
    def __init__(self):
        self.db = {}

    def save(self, purchase_request):
        new_id = len(self.db) + 1
        purchase_request.id = new_id

        self.db[new_id] = purchase_request
        
    def get_request_by_id(self, id):
        request_by_id = self.db.get(id)
        return request_by_id
        
    
