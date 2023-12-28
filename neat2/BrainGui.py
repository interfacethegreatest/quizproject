from globalVariables import *

import tkinter as tk

class DrawBrain:
    
    def __init__(self, brain = Brain()):
        self.brain = Brain(self.globalVariable)
        self.num_layers = len(self.brain.nodeLayer)
        self.num_nodes = self.brain.nodeLayer
        self.create_tkinter_window()
        self.canvas, self.rectangle_indexes = self.create_outlined_rectangle(1400, 900, self.num_layers)
        self.nodes = self.draw_nodes(self.canvas, self.rectangle_indexes, self.num_nodes, self.brain.nodeList)
        self.draw_connections(self.canvas, self.nodes, self.brain.connList, self.brain.nodeList)
        self.root.mainloop()
    
    
    
    def run_test(self,inputs, output):
        self.brain.loadInputs(inputs)
        self.brain.run_network()
        out = self.brain.get_output(output)
    
    def draw_connections(self, canvas, node_indexes, conn_list, node_list):
        for i in range(len(conn_list)):
            origin_node = conn_list[i].in_node_ID-1
            end_node = conn_list[i].out_Node_ID-1
            origin_coordinate = node_indexes[origin_node]
            end_coordinate = node_indexes[end_node]
            # Draw a line between the origin and end coordinates
            if conn_list[i].ennabled:
             canvas.create_line(origin_coordinate[0], origin_coordinate[1],
                               end_coordinate[0], end_coordinate[1], fill="Green", width=2)
            else:
                 canvas.create_line(origin_coordinate[0], origin_coordinate[1],
                                   end_coordinate[0], end_coordinate[1], fill="Red", width=2)
                 
            
            # Calculate the center point of the line
            center_x = (origin_coordinate[0] + end_coordinate[0]) / 2
            center_y = (origin_coordinate[1] + end_coordinate[1]) / 2

            # Loop through node indexes and print conn_list text slightly to the right
            offset_right = 15  # Adjust this value for the right offset
            for index, node_index in enumerate(node_indexes):
            # Offset slightly to the right
             text_x = node_index[0] + offset_right
             text_y = node_index[1]
             '''
            # Print conn_list text to the right of each node
             canvas.create_text(text_x, text_y, text=conn_list[index], fill="blue", font=("Arial", 8), anchor="w")
              '''            
       
                
    
    def draw_nodes(self, canvas, rectangle_indexes, num_nodes_list, nodes):
     centreList = list()
     for rect_index, num_nodes in zip(rectangle_indexes, num_nodes_list):
        # Get the coordinates of the rectangle
        x0, y0, x1, y1 = canvas.coords(rect_index)

        # Calculate the height of each node
        if num_nodes > 0:
         node_height = (y1 - y0) / num_nodes
        else:
            pass
        
        # Draw nodes vertically within each rectangle
        for i in range(num_nodes):
            node_x0 = x0
            node_y0 = y0 + i * node_height
            node_x1 = x1
            node_y1 = node_y0 + node_height
            canvas.create_rectangle(node_x0, node_y0, node_x1, node_y1, fill="black") 

            # Calculate the center of the node
            center_x = (node_x0 + node_x1) / 2
            center_y = (node_y0 + node_y1) / 2
            centreList.append((center_x, center_y))
            # Draw a white circle at the center
            radius = 10  # Set your desired radius value
            canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="white")
            
            
     for y in range(len(centreList)):
      canvas.create_text(centreList[y][0],centreList[y][1]+5, text= nodes[y], fill="blue", font=("Arial", 8), anchor = "center")
     canvas.pack()
     return centreList





    def create_tkinter_window(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("My Tkinter Window")

        # Add widgets and functionality here if needed
        self.root.geometry("1400x900")
        self.root.configure(bg="black")

    def create_outlined_rectangle(self, width, height, num_subrectangles):
        # Set the default border percentage
        border_percentage = 10

        # Calculate the dimensions of the inner rectangle
        inner_width = width * (1 - border_percentage / 100)
        inner_height = height * (1 - border_percentage / 100)

        # Calculate the border size
        border_width = (width - inner_width) / 2
        border_height = (height - inner_height) / 2

        # Calculate the dimensions of each smaller rectangle
        subrect_width = inner_width / num_subrectangles
        subrect_height = inner_height

        # Create a Canvas widget
        canvas = tk.Canvas(self.root, width=width, height=height, bg="black")
        canvas.pack()

        # Draw the outer rectangle (border)
        canvas.create_rectangle(0, 0, width, height, outline="black", width=border_width, fill="")

        # Draw the inner rectangle
        canvas.create_rectangle(border_width, border_height, width - border_width, height - border_height, fill="black")

        # Draw the smaller rectangles and store their indexes
        rectangle_indexes = []
        for i in range(num_subrectangles):
            x0 = border_width + i * subrect_width
            y0 = border_height
            x1 = x0 + subrect_width
            y1 = height - border_height
            rect_index = canvas.create_rectangle(x0, y0, x1, y1, fill="black")
            rectangle_indexes.append(rect_index)

        # Return the canvas and the list of rectangle indexes
        return canvas, rectangle_indexes

if __name__ == "__main__":
    inputNodes = 2
    hiddenNodes = 0
    outputNodes = 1
    percConnections = 0
    inputs = (0,1)
    output = 4
    gv = GlobalVariables(inputNodes, outputNodes, hiddenNodes, percConnections)
    brain = Brain()
    window = DrawBrain(brain)
