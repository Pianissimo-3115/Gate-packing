class Gate:
    def __init__(self, id, width, height, delay, pins: list["Pin"]):
        self.id = id
        self.dimensions = (width, height)
        self.pins=pins
        self.input_connections=[]
        self.output_connections=[]
        self.delay=delay
        self.neighboring_delay=0

    def info(self):
        return f"Gate(id={self.id}, dimensions={self.dimensions}, pins={self.pins}, delay={self.delay}\ninput_connections:{self.input_connections}\n output_connections:{self.output_connections})"
    def __repr__(self):
        return f"{self.id}"


class Pin:
    def __init__(self,id,x,y,gate:Gate,connections:list[tuple],network:"Network"=None):
        self.id = id
        self.position=(x,y)
        self.connections=connections        #each element is a tuple of type (gate,pin)
        self.gate=gate
        self.network=network
        self.type=None
    def __repr__(self):
        return f"{self.gate.id}.p{self.id}"
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
        self.aggregated_delay=0
    
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
        self.aggregated_delay+=pin.gate.delay
    
    def check_pin(self,coordinates:tuple):
        if self.max_x is None or self.min_x is None or self.max_y is None or self.min_y is None:
            return 0
        xdiff=max(self.max_x,coordinates[0])-min(self.min_x,coordinates[0])
        ydiff=max(self.max_y,coordinates[1])-min(self.min_y,coordinates[1])
        return xdiff+ydiff
    
    def __repr__(self):
        return f"bounding_box ({self.min_x},{self.min_y}), ({self.max_x},{self.max_y})"
    

class Queue:
    def __init__(self):
        self.front_stack = []
        self.rear_stack = []

    def enqueue(self, item):
        self.rear_stack.append(item)

    def dequeue(self):
        if not self.front_stack:
            while self.rear_stack:
                self.front_stack.append(self.rear_stack.pop())
        
        if self.front_stack:
            return self.front_stack.pop()
        else:
            raise IndexError("Dequeue from an empty queue!")

    def is_empty(self):
        return not self.front_stack and not self.rear_stack
    
    def __repr__(self):
        return f"Queue(front_stack={self.front_stack}, rear_stack={self.rear_stack})"
