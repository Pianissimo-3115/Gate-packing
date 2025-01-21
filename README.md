# Gate Packing Project

## Overview

This project explores different strategies for arranging logic gates efficiently, focusing on minimizing various factors like area, wire length, and critical path delay. The project is divided into three assignments, each addressing a specific optimization challenge.

## Assignment 1: Minimizing Bounding Box Area

In this assignment, the goal was to arrange a set of rectangle gates in a way that the **bounding box** (the smallest rectangle enclosing all the gates) has the **minimum possible area**. The challenge was to find an optimal layout that reduces the overall space while accommodating all the gates.

## Assignment 2: Minimizing Wire Length

Building on the first assignment, the focus shifted to **minimizing the total wire length** required to connect the logic gates with ports. The aim was to arrange the gates in a way that keeps the wire connections as short as possible, thereby improving efficiency and reducing signal propagation delays. A **Greedy algorithm** was used to select optimal placement points based on the perimeter of the layout.

## Assignment 3: Minimizing Critical Path Delay

The final assignment introduced the concept of **critical path delay**, which is the longest delay from any primary input port to any primary output port. The goal was to minimize this delay by considering both **gate delays** and **wire delays**. A modified **Greedy algorithm** was employed, prioritizing gate placements based on their impact on the critical path delay, using a custom comparator to evaluate potential positions.

## Conclusion

Throughout these assignments, different aspects of gate placement were explored, each focusing on a unique optimization goal. The progression from minimizing area to wire length, and finally to critical path delay, showcases the complexity and multifaceted nature of logic gate placement in VLSI design.

## Acknowledgements

The algorithms and methods used in these assignments are based on standard principles and techniques in VLSI design and graph theory, with custom implementations tailored for the specific challenges presented in each assignment.