import json
import random

def generate_unique_coordinates(occupied):
    while True:
        coords = [random.randint(0, 14), random.randint(0, 14)]
        if tuple(coords) not in occupied:
            occupied.add(tuple(coords))
            return coords

def generate_unit(unit_id, agent_id, occupied):
    return {
        "coordinates": generate_unique_coordinates(occupied),
        "hp": 3,
        "inventory": {"bombs": random.randint(1, 9999)},
        "blast_diameter": 3,
        "unit_id": unit_id,
        "agent_id": agent_id,
        "invulnerable": 0,
        "stunned": 0
    }

def generate_observation(index):
    occupied = set()
    agents = {
        "a": {"agent_id": "a", "unit_ids": ["c", "d", "e"]},
        "b": {"agent_id": "b", "unit_ids": ["f", "g", "h"]}
    }
    units = ["c", "d", "e", "f", "g", "h"]
    unit_states = {unit: generate_unit(unit, "a" if unit < "f" else "b", occupied) for unit in units}
    entities = [{"created": 0, 
                 "x": coord[0], 
                 "y": coord[1], 
                 "type": random.choice(["m", "w", "o"]), 
                 "hp": 1 if random.choice([True, False]) else 3} 
                for coord in [generate_unique_coordinates(occupied) for _ in range(20)]]
    
    observation = {
        "game_id": f"mock_game_{index}",
        "agents": agents,
        "unit_state": unit_states,
        "entities": entities,
        "world": {"width": 15, "height": 15},
        "tick": random.randint(0, 300),
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    }
    return observation

def generate_observations(num_observations):
    return [generate_observation(i) for i in range(num_observations)]

def main():
    observations = generate_observations(10)
    with open("mock_observations.json", "w") as file:
        json.dump(observations, file, indent=4)

if __name__ == "__main__":
    main()
