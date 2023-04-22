#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 00:53:38 2023

@author: vinay
"""

# Importing the Graphviz Module
import graphviz

# Create a new Graphviz graph
graph = graphviz.Digraph()

# Add nodes A, B, C, D, and E
graph.node('A')
graph.node('B')
graph.node('C')
graph.node('D')
graph.node('E')

# Add edges from A to B and from B to D
graph.edge('A', 'B')
graph.edge('B', 'D')

# Add edges from C and D to E
graph.edge('C', 'E')
graph.edge('D', 'E')

# Add an edge from A to E
graph.edge('A', 'E')

# Render the graph
graph.render('flowchart', format='png', view=True)
