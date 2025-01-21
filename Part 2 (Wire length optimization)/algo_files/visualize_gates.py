#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Installing tkinter and PIL
1) pip install tk
2) pip install pillow
"""


import argparse
from tkinter import *
from PIL import Image, ImageTk
import random as random
def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  

random.seed(42)
class draw_gate_packing(Tk):
    """
    Source: https://stackoverflow.com/questions/54637795/how-to-make-a-tkinter-canvas-rectangle-transparent
    """
    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            # fill = self.winfo_rgb(fill) + (alpha,)
            fill = fill + (alpha,)
            image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            self.images.append(ImageTk.PhotoImage(image))
            self.canvas.create_image(x1, y1, image=self.images[-1], anchor='nw')
        self.canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

    def draw_grid(self, canvas, width, height, grid_size):
        """Draws the grid lines on the canvas."""
        for i in range(0, width, grid_size):
            self.canvas.create_line([(i, 0), (i, height)], tag="grid_line", fill="lightgray")
        for i in range(0, height, grid_size):
            self.canvas.create_line([(0, i), (width, i)], tag="grid_line", fill="lightgray")

    def __init__(self, input_f, output_f, grid_dimensions, wires):   
        self.scale = 0
        self.shift = 0
        super(draw_gate_packing, self).__init__()
        self.images = []
        self.title("Gate Placement Visualization")
        
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Set the canvas size based on the screen size
        canvas_width = int(screen_width * 0.9)
        canvas_height = int(screen_height * 0.9)
        
        row_size, column_size = grid_dimensions
        grid_size_x = canvas_width // column_size
        grid_size_y = canvas_height // row_size
        grid_size = min(grid_size_x, grid_size_y)
        self.scale = grid_size

        self.canvas = Canvas(self, width=canvas_width, height=canvas_height, bg="white")


        
        for g,sz in output_f.items():
            print(g,sz)
            if g == 'bounding_box':
                self.shift = self.scale*(sz[1])

                self.draw_grid(self, canvas_width, canvas_height, grid_size)
                self.create_rectangle(0, 0, self.scale*sz[0], self.scale*sz[1], outline = 'black', width=5)
            else:
                # print(g)
                de=random.randint(0,255)
                re=random.randint(0,255)
                we=random.randint(0,255)
                color=(de,re,we)
                x1 = self.scale*sz[0]
                y1 = self.shift-self.scale*input_f[g][1]-self.scale*sz[1]
                x2 = self.scale*sz[0]+self.scale*input_f[g][0]
                y2 = self.shift-self.scale*sz[1]
                print(x1,y1,x2,y2)
                self.create_rectangle(x1, y1, x2, y2, outline = 'black', fill=color, width=1, alpha=0.5)
                self.canvas.create_text(x1+(x2-x1)/2, y1+(y2-y1)/2, font=("Arial", grid_size), text=g)

        i=1
        
        for wire in wires:
            # wire.sort()
            de=random.randint(0,255)
            re=random.randint(0,255)
            we=random.randint(0,255)
            color=(de,re,we)
            x1 = self.scale*wire[0][0]
            y1 = self.shift-self.scale*wire[0][1]
            x2 = self.scale*wire[1][0]
            y2 = self.shift-self.scale*wire[1][1]
            print(x1,y1,x2,y2)
            # self.canvas.create_line([(, tag="wire", fill=from_rgb(color)) ((x2+x1)//2,y1),((x2+x1)//2,y2),,(x2+10,y2+10),(x2+10,y2-10),(x2,y2)
            self.canvas.create_line([(x1+5,y1+5),(x1+5,y1-5),(x1-5,y1-5),(x1-5,y1+5),(x1+5,y1+5),(x1,y1),((x2+x1)//2,y1),((x2+x1)//2,y2),(x2,y2)], tag="wire", fill=from_rgb(color), width=3,arrow='last')
            self.canvas.create_text(x1, y1, font=("Arial", grid_size//3), text=str(i))
            i+=1
        
        self.canvas.pack()

def visualize_gates(coordinates_file, dimensions_file, grid_dimensions):
    """Visualizes gates and their grid cell coverage."""
    # Read the dimensions file
    gate_dimensions = {}
    pins_info = {}
    wire_data = []
    with open(dimensions_file, "r") as file:
        lines = file.readlines()
        i=0
        while i<len(lines):
            if not lines[i].startswith("wire"):
                line = lines[i]
                gate_info = line.split()
                name = gate_info[0]
                width = int(gate_info[1])
                height = int(gate_info[2])
                i+=1
                line = lines[i].split()
                pins_info[name] = {"p"+str(x+1) : (int(line[2+2*x]),int(line[2+2*x+1])) for x in range(len(line[2:])//2)}
                gate_dimensions[name] = (width, height)
                i+=1
            else:
                line = lines[i].split()
                print(line)
                g1,p1 = line[1].split(".")
                g2,p2 = line[2].split(".")
                wire_data.append(((g1,p1),(g2,p2)))
                i+=1

    # Read the coordinates file
    gates = {}
    with open(coordinates_file, "r") as file:
        lines = file.readlines()[:-1]
        for line in lines:
            gate_info = line.split()
            if len(gate_info) != 3:
                print(f"Skipping line in coordinates file: {line.strip()}")
                continue
            name = gate_info[0]
            x = int(gate_info[1])
            y = int(gate_info[2])
            # if name in gate_dimensions:
            gates[name] = (x, y)

    wires = []
    for i in wire_data:
        g1,p1 = i[0]
        g2,p2 = i[1]
        wires.append([(gates[g1][0]+pins_info[g1][p1][0],gates[g1][1]+pins_info[g1][p1][1]),(gates[g2][0]+pins_info[g2][p2][0],gates[g2][1]+pins_info[g2][p2][1])])


    # Draw gates and grid cells covered by the gates
    print(grid_dimensions)
    root = draw_gate_packing(gate_dimensions, gates, tuple(grid_dimensions), wires)

    root.mainloop()

   
    
if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Visualize gate placement on a grid.")
    # parser.add_argument(
    #     "coordinates_file", type=str, help="File containing gate coordinates."
    # )
    # parser.add_argument(
    #     "dimensions_file", type=str, help="File containing gate dimensions."
    # )
    # parser.add_argument(
    #     "grid_dimensions",
    #     type=int,
    #     nargs=2,
    #     help="Grid dimensions as row_size column_size.",
    # )

    # args = parser.parse_args()

    visualize_gates(r"D:\Study-Work\Study\Sem 3\COL 215\Assignments\SW 2\newone\output.txt", r"D:\Study-Work\Study\Sem 3\COL 215\Assignments\SW 2\newone\input.txt", (300,300))
