import csv
from typing import List


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
class Node:
    def __repr__(self) -> str:
        return f"{{{self.name}:{self.f_cost}}}"

    def __str__(self) -> str:
        return self.__repr__()

    def __init__(self, name: str, f_cost: int = 0, dist_to_origin: int = 0):
        self.name = name
        self.f_cost: int = f_cost
        self.dist_to_origin = dist_to_origin

    def successors(self) -> List[str]:
        successors = []
        with open("cities.csv", newline='') as dataFile:
            reader = csv.DictReader(dataFile)
            for row in reader:
                if row["city1"] == self.name:
                    successors.append(row["city2"])
        return sorted(successors)

    def g(self) -> int:
       return self.dist_to_origin

    def h(self) -> int:
        return h(self.name)
    def get_distance_to(self, to: str) -> int:
        distance = -1
        with open("cities.csv", newline='') as dataFile:
            reader = csv.DictReader(dataFile)
            for row in reader:
                if row["city1"] == self.name:
                    if row["city2"] == to:
                        distance = int(row["distance"])
        if distance == -1:
            print("Error: road from " + self.name + " to " + to + " not found")
            return -1
        return distance