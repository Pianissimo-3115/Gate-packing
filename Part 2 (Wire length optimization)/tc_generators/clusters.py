import random

# Function to generate random gate specifications with pin restrictions
def generate_gate(gate_id):
    width = random.randint(1, 100)
    height = random.randint(2, 100)
    
    num_left_pins = random.randint(1, height)
    left_pins = [(width, random.randint(0, height)) for _ in range(num_left_pins)]
    
    # Pins on the right side (random count between 1 and height//2)
    num_right_pins = random.randint(1, height // 2 + 1)
    right_pins = [(width, random.randint(0, height)) for _ in range(num_right_pins)]

    # Combine the left and right pins
    pin_coordinates = left_pins + right_pins

    gate_str = f"g{gate_id} {width} {height}\n"
    pin_str = "pins " + f"g{gate_id} " + " ".join(f"{x} {y}" for x, y in pin_coordinates) + "\n"
    
    return gate_str, pin_str, len(pin_coordinates)

# Function to ensure each gate within the cluster has at least one wire connection
def generate_wires_within_cluster(cluster_gates, pin_counts):
    connections = []
    num_gates = len(cluster_gates)

    for i in range(num_gates):
        g1 = cluster_gates[i]
        g2 = random.choice(cluster_gates)
        while g2 == g1:  # Ensure we don't connect a gate to itself
            g2 = random.choice(cluster_gates)
        p1_idx = random.randint(1, pin_counts[i])
        p2_idx = random.randint(1, pin_counts[cluster_gates.index(g2)])
        connections.append(f"wire g{g1}.p{p1_idx} g{g2}.p{p2_idx}")

    # Now, add extra random connections within the cluster
    extra_connections = num_gates // 2  # Add some extra random connections
    for _ in range(extra_connections):
        g1 = random.choice(cluster_gates)
        g2 = random.choice(cluster_gates)
        while g2 == g1:
            g2 = random.choice(cluster_gates)
        p1_idx = random.randint(1, pin_counts[cluster_gates.index(g1)])
        p2_idx = random.randint(1, pin_counts[cluster_gates.index(g2)])
        connections.append(f"wire g{g1}.p{p1_idx} g{g2}.p{p2_idx}")
    
    return connections

# Function to generate multiple clusters of gates
def generate_clusters(num_clusters=3, min_gates=10, max_gates=30):
    total_gates = 0
    clusters = []

    for _ in range(num_clusters):
        num_gates_in_cluster = random.randint(min_gates, max_gates)
        clusters.append(num_gates_in_cluster)
        total_gates += num_gates_in_cluster

    return clusters

# Function to write test case to input.txt
def write_test_case_to_file(clusters, filename="clusters.txt"):
    gate_id = 1
    with open(filename, 'w') as file:
        for cluster_size in clusters:
            cluster_gates = list(range(gate_id, gate_id + cluster_size))
            pin_counts = []
            for g in cluster_gates:
                gate_str, pin_str, num_pins = generate_gate(g)
                file.write(gate_str)
                file.write(pin_str)
                pin_counts.append(num_pins)
            
            # Generating random wires within the current cluster
            wires = generate_wires_within_cluster(cluster_gates, pin_counts)
            for wire in wires:
                file.write(wire + "\n")
            
            gate_id += cluster_size

# Generate clusters of random sizes between 10 and 100 gates
clusters = generate_clusters()

# Write the test case to input.txt
write_test_case_to_file(clusters)
