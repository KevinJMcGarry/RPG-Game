# classes related to inventory

class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop  # property is a reserved name, so we used prop

