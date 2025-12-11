from abc import ABC, abstractmethod

class PurchaseRequestRepositoryInterface(ABC):
    @abstractmethod
    def save(self, purchase_request):
        pass

    @abstractmethod
    def get_request_by_id(self, id):
        pass