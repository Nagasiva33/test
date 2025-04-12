import unittest
from collections import deque

def are_connected(graph, city1, city2):
    if city1 not in graph or city2 not in graph:
        return False
    visited = set()
    queue = deque([city1])
    while queue:
        current = queue.popleft()
        if current == city2:
            return True
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False

class TestCityConnections(unittest.TestCase):

    def setUp(self):
        # Custom graph setup
        self.graph = {
            "Badvel": {"Kadapa"},
            "Kadapa": {"Badvel", "Hyderabad"},
            "Hyderabad": {"Kadapa", "Mumbai"},
            "Mumbai": {"Hyderabad", "Goa"},
            "Goa": {"Mumbai", "Chennai"},
            "Chennai": {"Goa"}
        }

    def test_connected_badvel_mumbai(self):
        self.assertTrue(are_connected(self.graph, "Badvel", "Mumbai"))

    def test_connected_badvel_chennai(self):
        self.assertTrue(are_connected(self.graph, "Badvel", "Chennai"))

    def test_connected_goa_chennai(self):
        self.assertTrue(are_connected(self.graph, "Goa", "Chennai"))

    def test_not_connected_badvel_unknown(self):
        self.assertFalse(are_connected(self.graph, "Badvel", "Delhi"))  # Delhi not in graph

    def test_same_city(self):
        self.assertTrue(are_connected(self.graph, "Goa", "Goa"))

if _name_ == "_main_":
    unittest.main()