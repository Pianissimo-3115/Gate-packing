# Gate Packing - Assignment 3

## Overview

In this assignment, we build upon the logic gate placement from Assignment 2, but with an added focus on optimizing the **critical path delay** rather than just minimizing wire length. The goal is to minimize the delay between primary input and primary output ports, considering both **gate delays** and **wire delays**.

## What Makes This Assignment Different?

In **Assignment 2**, the primary focus was minimizing wire length by placing gates efficiently. In **Assignment 3**, however, we aim to minimize the **critical path delay**, which is the longest path delay between any primary input port and any primary output port. To achieve this, we incorporate the **gate delay** and **wire delay** into our optimization process.

- **Gate delay**: Each gate has its own inherent delay.
- **Wire delay**: This is proportional to the wire length connecting the gates.

By adjusting the placement of gates to minimize the combined impact of both delays, we can reduce the critical path delay.

## The Algorithm

We use a **Greedy algorithm**, similar to the one in Assignment 2, but with some key differences:
1. **Gate Sorting**: Gates are sorted in descending order based on the sum of the gate delays of their neighboring gates. This ensures that gates with higher accumulated delays are prioritized for placement, where their wire length can be minimized.
   
2. **Custom Comparator**: Instead of minimizing just the wire length, the comparator function now uses the formula:

   - **Aggregate gate delay**: This is the sum of delays of all the gates already placed and those that will be connected to the current gate.
   - **Wire length**: This refers to the wire length connecting the current gate to the already placed gates.

3. **Cycle Detection**: To ensure valid inputs, we detect any infinite loops using a special function that checks for cycles in the gate connections. We verify the inputs by examining the size of the stack used during iteration.

## Input File Format

Your input file should follow this format:

```
<name of gate> <width> <height> <delay>
<wire_delay> <delay>
<pins> <name of gate> <x_1, y_1> ... <x_m, y_m>
<wire> <g_x.p_x> <g_y.p_y>
```

- Each gate has a name, width, height, and a delay.
- The wire delay specifies the delay per unit of wire length.
- The pins section defines the gate and its connections.
- The wire section connects gates through wire.

## Output File Format

The output will contain the following:

```
bounding_box <width> <height>
critical_path <g_x.p_x> <g_y.p_y> ... <g_z.p_z>
critical_path_delay <delay>
```

Followed by `n` lines (where `n` is the number of gates):

```
<name of gate> <x coordinate> <y coordinate>
```

- The bounding box is the area containing all the gates.
- The critical path specifies the sequence of gates that forms the longest path delay.
- The critical path delay is the total delay along this path.

## How to Run It

Run the `solve` function in `main.py` like this:

```python
solve("<inputfile_address>", "<outputfile_address>")
```

This will solve the problem and generate the output file.

## Visualizing the Results

To visualize the placement of the gates, use the following command:

```bash
python visualize_gates.py "<outputfile_address>" "<inputfile_address>" <height_of_visualization> <width_of_visualization>
```

This command will generate a visual representation of the gate layout.

## Acknowledgements

The **Greedy algorithm** used here is an adaptation of the one in Assignment 2. It focuses on minimizing the combined delays of both gates and wire lengths to optimize the critical path delay.

## References

No specific references were used. The methods are based on standard algorithms and general knowledge.