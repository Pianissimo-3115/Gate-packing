# Gate Packing - Assignment 2

This project is all about figuring out the best way to arrange **logic gates with ports** to keep the total wire length as short as possible. The main goal is to place these gates in a way that uses the least amount of wire.

## What's Special

What makes this project stand out is how we handle the perimeter when placing gates. We keep track of every point along the edge of the current layout and choose the spot that keeps the wire length as short as possible. This simple but smart approach makes the whole process much more efficient.

## The Algorithm

We use a **Greedy algorithm** that treats the gates as nodes and the wires as edges in a graph. First, we find all the separate parts of the graph. Then, for each part, we sort the gates by how many connections they have and place them layer by layer, like a BFS. Each time we place a gate, we look for the spot that keeps the wire length as short as possible.

## What You Need

- `tk`
- `pillow`

## Input File Format

Your input file should look like this:
```
<name of gate> <width> <height>
<pins> <name of gate> <x_1, y_1> ... <x_m, y_m>
<wire> <g_x.p_x> <g_y.p_y>
```

## Output File Format

The output will have:
```
bounding_box <width> <height>
wire_length <wire_length>
```
Then for each gate:
```
<name of gate> <x coordinate> <y coordinate>
```

## How to Run It

Run the `solve` function in `main.py` like this:

```python
solve("<inputfile_address>", "<outputfile_address>")
```

## Visualizing the Results

To see how the gates are packed, use this command:

```bash
python visualize_gates.py "<outputfile_address>" "<inputfile_address>" <height of visualization> <width of visualization>
```

## Acknowledgements

The **Greedy algorithm** used here is a custom solution for placing logic gates efficiently. By focusing on breaking down the graph into parts and using BFS for placement, we make sure to keep the wire length as short as possible.

## References

No specific references were used. The methods are based on general knowledge and standard algorithms.

