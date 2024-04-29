from datetime import datetime
from uuid import uuid4

class MyBase:

    def __init__(self):
    # assign a few common default attributes to all instance of this class
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save_update(self):
      # update updated_at attribute with the current date and time
        updated_at = datetime.now()
