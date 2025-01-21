class Gate:
    def __init__(self, id, width, height, pins: list["Pin"]):
        self.id = id
        self.dimensions = (width, height)
        self.pins = pins
        self.connections=set()
    def info(self):
        return f"Gate(id={self.id}, dimensions={self.dimensions}, pins={self.pins})"
    def __repr__(self):
        return f"{self.id}:{self.dimensions[0]}x{self.dimensions[1]}"

class Pin:
    def __init__(self,id,x,y,gate:Gate,connections:list[tuple],network:"Network"=None):
        self.id = id
        self.position=(x,y)
        self.connections=connections
        self.gate=gate
        self.network=network
    def __repr__(self):
        return f"{self.gate.id}.{self.id}"
    def info(self):
        return f"Pin(id={self.id}, relative coordinates={self.position}, connections={self.connections})"

class Network:
    def __init__(self):
        self.pins=[]
        self.max_x=None
        self.min_x=None
        self.max_y=None
        self.min_y=None
        self.wire_length=0 #equal to semi-perimeter of the bounding box of the network
    
    def addpin(self,pin:Pin,coordinates:tuple):
        self.pins.append((pin,coordinates))
        if self.max_x is None or coordinates[0] > self.max_x:
            self.max_x = coordinates[0]
        if self.min_x is None or coordinates[0] < self.min_x:
            self.min_x = coordinates[0]
        if self.max_y is None or coordinates[1] > self.max_y:
            self.max_y = coordinates[1]
        if self.min_y is None or coordinates[1] < self.min_y:
            self.min_y = coordinates[1]
        assert self.min_x<=self.max_x, ValueError("max_x is less than min_x")
        assert self.min_y<=self.max_y, ValueError("max_y is less than min_y")
        self.wire_length=self.max_x-self.min_x+self.max_y-self.min_y
    
    def check_pin(self,coordinates:tuple):
        if self.max_x is None or self.min_x is None or self.max_y is None or self.min_y is None:
            return 0
        if coordinates[0] > self.max_x:
            x_distance = coordinates[0] - self.max_x
        elif coordinates[0] < self.min_x:
            x_distance = self.min_x - coordinates[0]
        else:
            x_distance = 0

        if coordinates[1] > self.max_y:
            y_distance = coordinates[1] - self.max_y
        elif coordinates[1] < self.min_y:
            y_distance = self.min_y - coordinates[1]
        else:
            y_distance = 0

        distance = x_distance + y_distance
        return distance
    def __repr__(self):
        return f"bounding_box ({self.min_x},{self.min_y}), ({self.max_x},{self.max_y})"
    def repr(self):
        return f"bounding_box ({self.min_x},{self.min_y}), ({self.max_x},{self.max_y}); wire_length {self.wire_length}"
    