# Gate Packing

This project focuses on comparing **gate packing algorithms**, with a special emphasis on the **Tetris-based algorithm**. The project includes visualizations and performance analysis across multiple test cases, demonstrating the efficiency of different approaches.

## USP

The **Tetris-based algorithm** is the standout feature of this project, which was inspired by tetris game mechanics. Despite its **ridiculously simple implementation**, it consistently delivers better performance in terms of space optimization compared to more complex algorithms, such as the **Sleator algorithm**. This simplicity, combined with effectiveness, makes it the key innovation of this project.

## Prerequisite Libraries

- `tk`
- `pillow`

## Input File Format

Each line in the input file should follow this format:
`<name of gate> <width> <height>`

## Output File Format

The output file will contain:
`bounding_box <width> <height>`

Followed by lines in this format:
`<name of gate> <x coordinate> <y coordinate>`

## How to Run

Call the functions by:

`tetris("<inputfile_address>", "<outputfile_address>")`

or

`sleator("<inputfile_address>", "<outputfile_address>")`

## Visualize

To visualize the packing results, run the following command:

`python visualize_gates.py "<outputfile_address>" "<inputfile_address>" <height of visualization> <width of visualization>`

## Credits

The **Tetris Algorithm** implemented here is an original adaptation designed for efficient gate packing. Despite its simplicity, it achieves remarkable space optimization. Its core principles are inspired by the Tetris game, where shapes are strategically arranged to minimize unused space.

The **Sleator Algorithm** implementation is based on the original work of Daniel Sleator et al. for packing problems. The detailed analysis and improvements made in this project are inspired by their foundational work in gate packing.

## References

1. Sleator, Daniel D., et al. *A 2.5 Times Optimal Algorithm for Packing in a Single Bin*. Journal of Computer and System Sciences, 1985.
2. Garey, Michael R., and David S. Johnson. *Computers and Intractability: A Guide to the Theory of NP-Completeness*. 1979.
3. Coffman, E. G., et al. *Approximation Algorithms for Bin Packing: A Survey*. 1997.
