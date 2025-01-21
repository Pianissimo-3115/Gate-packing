def generate_binary_tree_with_pins(num_gates=255):
    # Initialize list to store gates and their connections
    gates = []
    connections = []
    
    # Fixed dimensions for each gate (2x2) and pin at height 1
    width = 2
    height = 2
    pin_y = 1  # Fixed y-coordinate for all pins
    wire_delay = 1  # Fixed wire delay

    # Keep track of gate indices at each level
    current_level = 0
    gates_in_level = 1
    gate_idx = 0

    # Generate the gates with custom delays
    while gate_idx < num_gates:
        for i in range(gates_in_level):
            gate_name = f"g{gate_idx+1}"
            
            # Assign a delay of 100 to the first gate at each level, 1 to others
            delay = 100 if i == 0 else 1
            
            # Each gate has p1 (input pin) on the left (x=0, y=1) and p2 (output pin) on the right (x=2, y=1)
            input_pins = [(0, pin_y)]   # p1 at (0, 1)
            output_pins = [(width, pin_y)]  # p2 at (2, 1)
            
            gates.append({
                'name': gate_name,
                'width': width,
                'height': height,
                'delay': delay,
                'input_pins': input_pins,
                'output_pins': output_pins
            })
            
            gate_idx += 1
            if gate_idx >= num_gates:
                break
        
        # Move to the next level in the binary tree
        current_level += 1
        gates_in_level *= 2  # Double the number of gates for the next level
    
    # Create binary tree connections
    for i in range(num_gates // 2):
        # For each gate g(i+1), connect its p2 (output) to the p1 (input) of its left and right children
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        if left_child < num_gates:
            connections.append((
                f"g{i+1}.p2",  # Output p2 of parent gate
                f"g{left_child+1}.p1"  # Input p1 of left child gate
            ))
        if right_child < num_gates:
            connections.append((
                f"g{i+1}.p2",  # Output p2 of parent gate
                f"g{right_child+1}.p1"  # Input p1 of right child gate
            ))
    
    # Write to file
    with open('powersof2.txt', 'w') as f:
        # Write gates
        for gate in gates:
            f.write(f"{gate['name']} {gate['width']} {gate['height']} {gate['delay']}\n")
            
            # Write pins: p1 (input) followed by p2 (output)
            f.write(f"pins {gate['name']} 0 1 2 1\n")
        
        # Write wire delay
        f.write(f"wire_delay {wire_delay}\n")
        
        # Write connections
        for source, target in connections:
            f.write(f"wire {source} {target}\n")

if __name__ == "__main__":
    generate_binary_tree_with_pins(255)
    print("Binary tree test case with 255 gates and proper pin connections generated successfully!")
