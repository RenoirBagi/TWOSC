class ModelPurchaseRequest:
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item = Column(String(255), nullable=False)
    requester = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    priority = Column(String(50), nullable=False)
    request_date = Column(DateTime, nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)
    observation = Column(String(255))
    reference_link = Column(String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'item': self.item,
            'requester': self.requester,
            'quantity': self.quantity,
            'priority': self.priority,
            'request_date': self.request_date,
            'delivery_date': self.delivery_date,
            'status': self.status,
            'observation': self.observation,
            'reference_link': self.reference_link
        }