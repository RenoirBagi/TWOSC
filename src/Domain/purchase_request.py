from enum import Enum

class Priority(Enum):
    BAIXA = 'Baixa'
    MEDIA = 'Média'
    ALTA = 'Alta'

class Status(Enum):
    PENDENTE = 'Pendente'
    APROVADO = 'Aprovado'
    REJEITADO = 'Rejeitado'
    ENTREGUE ='Entregue'

class PurchaseRequest:
    def __init__(self,item,requester,quantity,priority,status,request_date,delivery_date=None,observation=None,reference_link=None,id=None):
        self.id = id
        self.item = item
        self.requester = requester               # Vinculo com a Entidade Requester
        self.quantity = self.validate_quantity(quantity)
        self.priority = priority                 # (Baixa, Média, Alta)
        self.status = status                     # (Pendente, Aprovado, Rejeitado, Entregue)
        self.request_date = request_date         # Registrado no momento da Solicitação é realizada
        self.delivery_date = delivery_date       # Inicia como None, é preenchido quando o TI receber o pedido
        self.observation = observation
        self.reference_link = reference_link
    
    def validate_quantity(self,quantity):
        if quantity <= 0:
            raise ValueError("A quantidade deve ser maior que zero")
        return quantity
    
    def to_dict(self,):
        purchase_request = {
            "id":self.id,
            "item":self.item,
            "requester":self.requester,
            "quantity":self.quantity,
            "priority":self.priority,
            "status":self.status,
            "request_date":self.request_date,
            "delivery_date":self.delivery_date,
            "observation":self.observation,
            "reference_link":self.reference_link
        }
        return purchase_request
        
    
        
pedido_renoir = PurchaseRequest(item="Monitor",requester="Renoir",quantity=1,priority=Priority.ALTA,status=Status.PENDENTE,request_date="03-12-2025")

print(pedido_renoir.to_dict())