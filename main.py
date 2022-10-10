#!/usr/bin/env python3
# In our case heuristic represents the distance in straight line from any city to bycarest
from enum import Enum
from operator import attrgetter
import os
from sre_constants import SUCCESS
import sys
from traceback import print_tb
from typing import List, Tuple
from Node import Node


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    start_node = Node(start, f_cost=h(start))
    return RBFS(start_node, sys.maxsize)


class Result(Enum):
    SUCCESS = 1
    FAILURE = 2

count = 0 
def RBFS(current_node: Node, f_limit: int) -> Tuple[Result, int]:
    global count
    print(f"RBFS[{count}], f_limit: {f_limit}, node: {current_node}")
    count = count + 1
    if current_node.name == "bucharest":
        return Result.SUCCESS, 0
    successors: List[Node] = []
    for succ in current_node.successors():
        succ_node = Node(succ)
        print(f"before f_cost update: {succ_node}")
        succ_node.f_cost = max(succ_node.g(
            current_node.name) + h(succ), current_node.f_cost)
        print(f"after f_cost update: {succ_node}")
        successors.append(succ_node)
    print(f"\tsuccs: {successors}")
    if len(successors) == 0:
        return Result.FAILURE, sys.maxsize
    while True:
        successors.sort(key=attrgetter("f_cost"))
        best = min(successors, key=attrgetter("f_cost"))
        if best.f_cost > f_limit:
            return Result.FAILURE, best.f_cost
        alternative: int = sys.maxsize
        if len(successors) > 1:
                alternative = successors[1].f_cost
        print(f"\talternative: {alternative}")
        print(f"best: {best}")
        result, best.f_cost = RBFS(best, min(f_limit, alternative))
        print(f"\tbest: {best}")
        if result != Result.FAILURE:
            return result, 0

def start():
    cls()
    print("Romanian City Problem using the RBFS\n")
    #print(f"Available start city\n -> {[key  for key in heuristic.keys()]}")
    start_city = input("Insert the start city: ")
    while not start_city in heuristic.keys():
        cls()
        print("The city you enterd is not valid, please try another one.\n")
        start_city = input("Insert the start city: ")
    if start_city == "bucharest":
        print("You are already at the goal!")
        return Result.SUCCESS
    return recursive_best_first_search(start_city)


def main():
    if start():
        ty = 1 if input("Do you want to try again? y/n:  ") == "y" else 0
        if ty:
            start()


###########################################################

if __name__ == '__main__':
    main()
