import random

# Function to generate random gate specifications with pin restrictions
def generate_gate(gate_id):
    width = random.randint(50, 50)
    height = random.randint(2, 100)
    
    num_left_pins = random.randint(1, height)
    left_pins = [(width, random.randint(0, height)) for _ in range(num_left_pins)]

    # Pins on the right side (random count between 1 and height)
    num_right_pins = random.randint(1, height//2+1)
    right_pins = [(width, random.randint(0, height)) for _ in range(num_right_pins)]

    # Combine the left and right pins
    pin_coordinates = left_pins + right_pins

    gate_str = f"g{gate_id} {width} {height}\n"
    pin_str = "pins " + f"g{gate_id} " + " ".join(f"{x} {y}" for x, y in pin_coordinates) + "\n"
    
    return gate_str, pin_str, len(pin_coordinates)

# Function to ensure each gate has at least one wire connection
def generate_wires(num_gates, pin_counts):
    connections = []
    connected_gates = set()

    # Ensure each gate has at least one wire connection
    for i in range(num_gates):
        g1 = i + 1
        g2 = random.randint(1, num_gates)
        while g2 == g1:  # Ensure we don't connect a gate to itself
            g2 = random.randint(1, num_gates)
        p1_idx = random.randint(1, pin_counts[i])
        p2_idx = random.randint(1, pin_counts[g2 - 1])
        connections.append(f"wire g{g1}.p{p1_idx} g{g2}.p{p2_idx}")
        connected_gates.add(g1)
        connected_gates.add(g2)

    # Now, randomly add more connections (if desired)
    extra_connections = num_gates // 2  # Add some extra random connections
    for _ in range(extra_connections):
        g1 = random.randint(1, num_gates)
        g2 = random.randint(1, num_gates)
        while g2 == g1:
            g2 = random.randint(1, num_gates)
        p1_idx = random.randint(1, pin_counts[g1 - 1])
        p2_idx = random.randint(1, pin_counts[g2 - 1])
        connections.append(f"wire g{g1}.p{p1_idx} g{g2}.p{p2_idx}")
    
    return connections

# Function to write test case to input.txt
def write_test_case_to_file(num_gates=1000, filename="input.txt"):
    with open(filename, 'w') as file:
        pin_counts = []
        for i in range(1, num_gates + 1):
            gate_str, pin_str, num_pins = generate_gate(i)
            file.write(gate_str)
            file.write(pin_str)
            pin_counts.append(num_pins)
        
        # Generating random wires
        wires = generate_wires(num_gates, pin_counts)
        for wire in wires:
            file.write(wire + "\n")

# Generate a test case with 1000 gates
write_test_case_to_file()
