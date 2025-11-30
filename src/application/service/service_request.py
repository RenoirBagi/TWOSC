from src.infrastructure.model.model_purchase_request import ModelPurchaseRequest
from src.domain.purchase_request import PurchaseRequest

class ServicePurchaseRequest:
    def create_purchase_request(purchase_request_data):

        new_purchase_request = PurchaseRequest(
            item = purchase_request_data['item'],
            requester = purchase_request_data['requester'],
            quantity = purchase_request_data['quantity']
            priority = purchase_request_data['priority']
            request_date = purchase_request_data['request_date']
            delivery_date = purchase_request_data['delivery_date']
            status = purchase_request_data['status']
            observation = purchase_request_data['observation']
            reference_link = purchase_request_data['reference_link']
        )