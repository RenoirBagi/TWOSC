from src.domain.repository import PurchaseRequestRepositoryInterface

class inMemoryPurchaseResquestRepository(PurchaseRequestRepositoryInterface):
    def __init__(self):
        self.db = {}

    def save(self, purchase_request):
        new_id = len(self.db) + 1
        purchase_request.id = new_id

        self.db[new_id] = purchase_request
        