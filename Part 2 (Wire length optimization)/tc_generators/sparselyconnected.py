import random

# Function to generate random gate specifications with pin restrictions
def generate_gate(gate_id):
    width = random.randint(1, 100)
    height = random.randint(70, 100)
    
    # Pin on the left side
    num_left_pins = random.randint(1, height)
    left_pins = [(width, random.randint(0, height)) for _ in range(num_left_pins)]

    
    # Pins on the right side (random count between 1 and height//2)
    num_right_pins = random.randint(1, height)
    right_pins = [(width, random.randint(0, height)) for _ in range(num_right_pins)]

    # Combine the left and right pins
    pin_coordinates = left_pins + right_pins

    gate_str = f"g{gate_id} {width} {height}\n"
    pin_str = "pins " + f"g{gate_id} " + " ".join(f"{x} {y}" for x, y in pin_coordinates) + "\n"
    
    return gate_str, pin_str, len(pin_coordinates)

# Function to generate dense wire connections among gates
def generate_sparse_wires(num_gates, pin_counts):
    connections = []
    
    # Ensure sparse connections: each gate will be connected to multiple other gates
    for i in range(num_gates):
        g1 = i + 1
        connected_gates = random.sample(range(1, num_gates + 1), k=random.randint(1, 3)) 
        for g2 in connected_gates:
            if g2 != g1:  # Avoid self-connections
                p1_idx = random.randint(1, pin_counts[i])
                p2_idx = random.randint(1, pin_counts[g2 - 1])
                connections.append(f"wire g{g1}.p{p1_idx} g{g2}.p{p2_idx}")
    
    return connections

# Function to write test case to input.txt
def write_test_case_to_file(num_gates=500, filename="sparselyconnected.txt"):
    with open(filename, 'w') as file:
        pin_counts = []
        for i in range(1, num_gates + 1):
            gate_str, pin_str, num_pins = generate_gate(i)
            file.write(gate_str)
            file.write(pin_str)
            pin_counts.append(num_pins)
        
        # Generating random wires among all gates
        wires = generate_sparse_wires(num_gates, pin_counts)
        for wire in wires:
            file.write(wire + "\n")

# Generate a test case with 500 sparsely connected gates
write_test_case_to_file()
