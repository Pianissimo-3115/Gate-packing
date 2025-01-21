def generate_linear_test_case(num_gates=100):
    # Initialize list to store gates and their connections
    gates = []
    connections = []
    
    # Fixed dimensions for each gate (10x10) and pin at height 5
    width = 10
    height = 10
    pin_y = 5  # Fixed y-coordinate for all pins
    wire_delay = 20  # Fixed wire delay

    # Generate the gates
    for i in range(num_gates):
        gate_name = f"g{i+1}"
        
        # Each gate has one input pin on the left (x=0, y=5) and one output pin on the right (x=10, y=5)
        input_pins = [(0, pin_y)]
        output_pins = [(width, pin_y)]
        
        gates.append({
            'name': gate_name,
            'width': width,
            'height': height,
            'delay': 1,  # Fixed delay of 1 ns for simplicity
            'input_pins': input_pins,
            'output_pins': output_pins
        })
    
    # Create sequential connections between the gates
    for i in range(num_gates - 1):
        # Connect the output of gate `g(i+1)` to the input of gate `g(i+2)`
        source_gate = gates[i]
        target_gate = gates[i + 1]
        
        source_pin = f"{source_gate['name']}.p2"  # Output pin of the current gate
        target_pin = f"{target_gate['name']}.p1"  # Input pin of the next gate
        
        connections.append((source_pin, target_pin))
    
    # Write to file
    with open('linear100.txt', 'w') as f:
        # Write gates
        for gate in gates:
            f.write(f"{gate['name']} {gate['width']} {gate['height']} {gate['delay']}\n")
            
            # Write pins (input pin followed by output pin)
            all_pins = []
            for x, y in gate['input_pins']:
                all_pins.extend([str(x), str(y)])
            for x, y in gate['output_pins']:
                all_pins.extend([str(x), str(y)])
                
            f.write(f"pins {gate['name']} {' '.join(all_pins)}\n")
        
        # Write wire delay
        f.write(f"wire_delay {wire_delay}\n")
        
        # Write connections
        for source, target in connections:
            f.write(f"wire {source} {target}\n")

if __name__ == "__main__":
    generate_linear_test_case(100)
    print("Linear test case with 100 gates generated successfully!")
