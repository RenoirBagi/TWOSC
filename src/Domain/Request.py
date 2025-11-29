class Request:
    def __init__(self,id,item,requester,quantity,priority,request_date,delivery_date,status,observation,reference_link):
        self.id = id
        self.item = item
        self.requester = requester
        self.quantity = quantity
        self.priority = priority
        self.request_date = request_date
        self.delivery_date = delivery_date
        self.status = status
        self.observation = observation
        self.reference_link = reference_link