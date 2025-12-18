from src.domain.purchase_request import PurchaseRequest, Status

class ServicePurchaseRequest:
    def __init__ (self, repository):
        self.repository = repository

    def create_purchase_request(self,item,requester,quantity,priority,request_date,observation,reference_link):
        new_purchase_request = PurchaseRequest(
            item=item,
            requester=requester,
            quantity=quantity,
            priority=priority,
            status=Status.PENDENTE,
            request_date=request_date,
            observation=observation,
            reference_link=reference_link,
            )

        self.repository.save(new_purchase_request)
