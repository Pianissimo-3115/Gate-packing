import random
def generate_test_case_without_cycles(num_gates=100):
    # Initialize lists to store gates and their connections
    gates = []
    connections = []
    
    # Generate random gates
    for i in range(num_gates):
        width = random.randint(1, 100)
        height = random.randint(1, 100)
        delay = random.randint(1, 10)  # Random delay between 1-10 ns
        
        # Calculate number of pins (input on left, output on right)
        num_input_pins = random.randint(1, height)  
        num_output_pins = random.randint(1,height)
        
        # Generate pin coordinates
        input_pins = set()  # Left side pins (x=0)
        output_pins = set()  # Right side pins (x=width)
        
        # Generate random input pins on left side
        while len(input_pins) < num_input_pins:
            y = random.randint(0, height)
            input_pins.add((0, y))
            
        # Generate random output pins on right side
        while len(output_pins) < num_output_pins:
            y = random.randint(0, height)
            output_pins.add((width, y))
            
        # Convert sets to sorted lists for consistent output
        input_pins = sorted(list(input_pins), key=lambda x: x[1])
        output_pins = sorted(list(output_pins), key=lambda x: x[1])
            
        gates.append({
            'name': f'g{i+1}',
            'width': width,
            'height': height,
            'delay': delay,
            'input_pins': input_pins,
            'output_pins': output_pins
        })
    
    wire_delay = random.randint(1, 5)  # Random wire delay per unit length
    
    # Keep track of used input pins to avoid multiple connections to same input
    used_input_pins = set()
    
    # First pass: Ensure each gate (except the first) has exactly one input connection from a previous gate
    for i in range(1, len(gates)):  # Start from second gate
        # Get a random source gate from previous gates
        source_gate_idx = random.randint(0, i-1)
        source_gate = gates[source_gate_idx]
        
        # Pick random pins for connection
        source_pin_idx = random.randint(0, len(source_gate['output_pins'])-1)
        target_pin_idx = random.randint(0, len(gates[i]['input_pins'])-1)
        
        # Create connection
        source_pin_num = len(source_gate['input_pins']) + source_pin_idx + 1
        connections.append((
            f"{source_gate['name']}.p{source_pin_num}",
            f"{gates[i]['name']}.p{target_pin_idx + 1}"
        ))
        used_input_pins.add((gates[i]['name'], target_pin_idx))
    
    # Second pass: Create more connections, ensuring no cycles
    for i in range(len(gates)-1):  # Exclude last gate as source
        source_gate = gates[i]
        
        # For each output pin of the current gate
        for source_pin_idx in range(len(source_gate['output_pins'])):
            # Create multiple random connections (but only to later gates)
            for _ in range(random.randint(1, 4)):
                if random.random() < 0.7:  # 70% chance to create a connection
                    # Get a target gate with a higher index than the source
                    possible_targets = [j for j in range(i+1, len(gates))]
                    
                    if possible_targets:
                        target_gate_idx = random.choice(possible_targets)
                        target_gate = gates[target_gate_idx]
                        
                        # Find available input pins for this gate
                        available_pins = [(pin_idx, pin) for pin_idx, pin in enumerate(target_gate['input_pins'])
                                        if (target_gate['name'], pin_idx) not in used_input_pins]
                        
                        if available_pins:
                            target_pin_idx, _ = random.choice(available_pins)
                            source_pin_num = len(source_gate['input_pins']) + source_pin_idx + 1
                            
                            connections.append((
                                f"{source_gate['name']}.p{source_pin_num}",
                                f"{target_gate['name']}.p{target_pin_idx + 1}"
                            ))
                            used_input_pins.add((target_gate['name'], target_pin_idx))
    
    # Write to file
    with open('sparselyconnected.txt', 'w') as f:
        # Write gates
        for gate in gates:
            f.write(f"{gate['name']} {gate['width']} {gate['height']} {gate['delay']}\n")
            
            # Write pins
            all_pins = []
            # Add input pins
            for x, y in gate['input_pins']:
                all_pins.extend([str(x), str(y)])
            # Add output pins
            for x, y in gate['output_pins']:
                all_pins.extend([str(x), str(y)])
            
            f.write(f"pins {gate['name']} {' '.join(all_pins)}\n")
        
        # Write wire delay
        f.write(f"wire_delay {wire_delay}\n")
        
        # Write connections
        for source, target in connections:
            f.write(f"wire {source} {target}\n")

if __name__ == "__main__":
    generate_test_case_without_cycles(100)
    print("Test case without cycles generated successfully!")
