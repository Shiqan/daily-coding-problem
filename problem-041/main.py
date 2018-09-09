#!/usr/bin/env python
""" Problem 41 daily-coding-problem.com """
from typing import List


def compute_itinerary(flights: List[str], starting_airport: str) -> List[str]:  
    if not flights:
        return [starting_airport]

    destinations = [(s,e) for s, e in flights if s == starting_airport]

    for i in destinations:
        remaining_flights = [f for f in flights if i != f]

        next_flight = compute_itinerary(remaining_flights, i[1])
        if next_flight is not None:
            return [starting_airport] + next_flight

    return None


if __name__ == "__main__":
    assert compute_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') == None
    assert compute_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')  == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
    assert compute_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A') == ['A', 'B', 'C', 'A', 'C'] 
