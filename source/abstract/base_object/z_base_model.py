import math, uuid
from datetime import datetime, timedelta

from controller import controller
from model import model
from view import view

class BaseModel(controller.Controller, model.Model, view.View):
    uuid    = None
    created = None
    parent  = None

    def __init__(self, parent = None):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent)
        view.View.__init__(self)
        self.parent = parent
        self.uuid = uuid.uuid4()
        self.created = datetime.now()
        pass

    def created_delta(self):
        return (datetime.now() - self.created).total_seconds()
