#!/usr/bin/env python3
# In our case heuristic represents the distance in straight line from any city to bycarest
from enum import Enum
from operator import attrgetter
import os
from sre_constants import SUCCESS
import sys
from typing import List
from Node import Node

def cls():
    os.system('cls' if os.name=='nt' else 'clear') 
heuristic = {"arad": 366,
             "bucharest": 0,
             "craiova": 160,
             "dobetra": 242,
             "eforie": 161,
             "fagaras": 178,
             "giurgi": 77,
             "hirsova": 151,
             "iasi": 226,
             "lugoj": 244,
             "mehadia": 241,
             "neamt": 234,
             "oradea": 380,
             "pitesti": 98,
             "ramnicu": 193,
             "sibiu": 253,
             "timisoara": 329,
             "urziceni": 80,
             "vaslui": 199,
             "zerind": 374
             }

# the h function will return the distance if city is found
def h(name: str) -> int:
    if not name in heuristic.keys():
        print("City not found: " + name)
        return -1
    else:
        return heuristic[name]

# The goal is to find the shortest path to Bucharest
def recursive_best_first_search(start: str):
    start_node = Node(start)
    return RBFS(start_node, sys.maxsize)

class Result(Enum):
    SUCCESS = 1
    FAILURE = 2

def RBFS( current_node: Node, f_limit: int):
    if current_node.name == "bucharest":
        return Result.SUCCESS
    successors: List[Node] = []
    for succ in current_node.successors():
        succ_node = Node(succ)
        succ_node.f_cost = max(succ_node.g(current_node.name) + h(succ), current_node.f_cost)
        successors.append(succ_node)
    successors.sort(key=attrgetter("f_cost"))
    print(*successors)

def start():
    print("Romanian City Problem using the RBFS\n")
    #print(f"Available start city\n -> {[key  for key in heuristic.keys()]}")
    start_city = input("Insert the start city: ")
    while not start_city in heuristic.keys():
        cls()
        print("The city you enterd is not valid, please try another one.\n")
        start_city = input("Insert the start city: ")
        
    recursive_best_first_search(start_city)
     


def main():
    start()
    
###########################################################


if __name__ == '__main__':
    main()
