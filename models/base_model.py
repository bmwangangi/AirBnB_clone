#!/usr/bin/python3

import uuid
from datetime import datetime

"""Creates a class for the AirbnbConsole project."""

class BaseModel:
    """BaseModel class to be inherited by other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class."""
        from models import storage
        # If keyword arguments are provided, initialize instance attributes from them
        if kwargs:
            for key, value in kwargs.items():
                # Convert 'created_at' and 'updated_at' strings to datetime objects
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                # Skip setting '__class__' attribute
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # Generate a new UUID for 'id', set 'created_at' and 'updated_at' to current datetime
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute to the current datetime."""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of all instance attributes."""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

class EURJPY(BaseModel):
    """EURJPY class to represent Airbnb listings."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the EURJPY class."""
        super().__init__(*args, **kwargs)

    def save(self):
        """Save the instance to the storage."""
        from models import storage
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the EURJPY instance."""
        my_dict = super().to_dict()
        return my_dict
