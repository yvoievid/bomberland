import json
import random

def generate_coordinates():
    return [random.randint(0, 14), random.randint(0, 14)]

def generate_unit(unit_id, agent_id):
    return {
        "coordinates": generate_coordinates(),
        "hp": 3,
        "inventory": {"bombs": random.randint(1, 9999)},
        "blast_diameter": 3,
        "unit_id": unit_id,
        "agent_id": agent_id,
        "invulnerable": 0,
        "stunned": 0
    }

def generate_observation(index):
    agents = {
        "a": {"agent_id": "a", "unit_ids": ["a1", "a2", "a3"]},
        "b": {"agent_id": "b", "unit_ids": ["b1", "b2", "b3"]}
    }
    units = ["a1", "a2", "a3", "b1", "b2", "b3"]
    unit_states = {unit: generate_unit(unit, "a" if unit.startswith("a") else "b") for unit in units}
    entities = [{"created": 0, "x": random.randint(0, 14), "y": random.randint(0, 14), "type": random.choice(["m", "w", "o"]), "hp": 1 if random.choice([True, False]) else 3} for _ in range(20)]
    
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
