from components.types import Observation

MOCK_15x15_INITIAL_OBSERVATION: Observation = {
    "game_id":"dev",
    "agents":{
        "a":{
            "agent_id":"a",
            "unit_ids":[
                "c",
                "e",
                "g"
            ]
        },
        "b":{
            "agent_id":"b",
            "unit_ids":[
                "d",
                "f",
                "h"
            ]
        }
    },
    "unit_state":{
        "c":{
            "coordinates":[
                3,
                10
            ],
            "hp":3,
            "inventory":{
                "bombs":3
            },
            "blast_diameter":3,
            "unit_id":"c",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "d":{
            "coordinates":[
                11,
                10
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"d",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        },
        "e":{
            "coordinates":[
                1,
                9
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"e",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "f":{
            "coordinates":[
                13,
                9
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"f",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        },
        "g":{
            "coordinates":[
                12,
                7
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"g",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "h":{
            "coordinates":[
                2,
                7
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"h",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        }
    },
    "entities":[
        {
            "created":0,
            "x":11,
            "y":7,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":7,
            "type":"m"
        },
        {
            "created":0,
            "x":10,
            "y":11,
            "type":"m"
        },
        {
            "created":0,
            "x":4,
            "y":11,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":4,
            "y":8,
            "type":"m"
        },
        {
            "created":0,
            "x":10,
            "y":8,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":13,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":1,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":0,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":0,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":3,
            "type":"m"
        },
        {
            "created":0,
            "x":12,
            "y":3,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":1,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":1,
            "type":"m"
        },
        {
            "created":0,
            "x":5,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":9,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":9,
            "y":6,
            "type":"m"
        },
        {
            "created":0,
            "x":5,
            "y":6,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":10,
            "type":"m"
        },
        {
            "created":0,
            "x":12,
            "y":10,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":13,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":13,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":2,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":10,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":10,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":0,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":0,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":2,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":2,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":10,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":4,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":11,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":3,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":5,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":2,
            "y":5,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":14,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":14,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":9,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":9,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":3,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":11,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":11,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":11,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":6,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":6,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":9,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":9,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":12,
            "type":"o",
            "hp":3
        }
    ],
    "world":{
        "width":15,
        "height":15
    },
    "tick":0,
    "config":{
        "tick_rate_hz":10,
        "game_duration_ticks":300,
        "fire_spawn_interval_ticks":2
    }
}


TEN_RANDOM_MOCK_15x15_INITIAL_OBSERVATIONS: list = [
    {
    "game_id":"dev",
    "agents":{
        "a":{
            "agent_id":"a",
            "unit_ids":[
                "c",
                "e",
                "g"
            ]
        },
        "b":{
            "agent_id":"b",
            "unit_ids":[
                "d",
                "f",
                "h"
            ]
        }
    },
    "unit_state":{
        "c":{
            "coordinates":[
                3,
                10
            ],
            "hp":3,
            "inventory":{
                "bombs":3
            },
            "blast_diameter":3,
            "unit_id":"c",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "d":{
            "coordinates":[
                11,
                10
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"d",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        },
        "e":{
            "coordinates":[
                1,
                9
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"e",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "f":{
            "coordinates":[
                13,
                9
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"f",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        },
        "g":{
            "coordinates":[
                12,
                7
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"g",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "h":{
            "coordinates":[
                2,
                7
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"h",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        }
    },
    "entities":[
        {
            "created":0,
            "x":11,
            "y":7,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":7,
            "type":"m"
        },
        {
            "created":0,
            "x":10,
            "y":11,
            "type":"m"
        },
        {
            "created":0,
            "x":4,
            "y":11,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":4,
            "y":8,
            "type":"m"
        },
        {
            "created":0,
            "x":10,
            "y":8,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":13,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":1,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":0,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":0,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":3,
            "type":"m"
        },
        {
            "created":0,
            "x":12,
            "y":3,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":1,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":1,
            "type":"m"
        },
        {
            "created":0,
            "x":5,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":9,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":9,
            "y":6,
            "type":"m"
        },
        {
            "created":0,
            "x":5,
            "y":6,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":10,
            "type":"m"
        },
        {
            "created":0,
            "x":12,
            "y":10,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":13,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":13,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":2,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":10,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":10,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":0,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":0,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":2,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":2,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":10,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":4,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":11,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":3,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":5,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":2,
            "y":5,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":14,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":14,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":9,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":9,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":3,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":11,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":11,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":11,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":6,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":6,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":9,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":9,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":12,
            "type":"o",
            "hp":3
        }
    ],
    "world":{
        "width":15,
        "height":15
    },
    "tick":0,
    "config":{
        "tick_rate_hz":10,
        "game_duration_ticks":300,
        "fire_spawn_interval_ticks":2
    }
},
{
    "game_id":"dev",
    "agents":{
        "a":{
            "agent_id":"a",
            "unit_ids":[
                "c",
                "e",
                "g"
            ]
        },
        "b":{
            "agent_id":"b",
            "unit_ids":[
                "d",
                "f",
                "h"
            ]
        }
    },
    "unit_state":{
        "c":{
            "coordinates":[
                3,
                10
            ],
            "hp":3,
            "inventory":{
                "bombs":3
            },
            "blast_diameter":3,
            "unit_id":"c",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "d":{
            "coordinates":[
                11,
                10
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"d",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        },
        "e":{
            "coordinates":[
                1,
                9
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"e",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "f":{
            "coordinates":[
                13,
                9
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"f",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        },
        "g":{
            "coordinates":[
                12,
                7
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"g",
            "agent_id":"a",
            "invulnerable":0,
            "stunned":0
        },
        "h":{
            "coordinates":[
                2,
                7
            ],
            "hp":3,
            "inventory":{
                "bombs":9999
            },
            "blast_diameter":3,
            "unit_id":"h",
            "agent_id":"b",
            "invulnerable":0,
            "stunned":0
        }
    },
    "entities":[
        {
            "created":0,
            "x":11,
            "y":7,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":7,
            "type":"m"
        },
        {
            "created":0,
            "x":10,
            "y":11,
            "type":"m"
        },
        {
            "created":0,
            "x":4,
            "y":11,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":4,
            "y":8,
            "type":"m"
        },
        {
            "created":0,
            "x":10,
            "y":8,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":13,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":1,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":0,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":0,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":3,
            "type":"m"
        },
        {
            "created":0,
            "x":12,
            "y":3,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":14,
            "type":"m"
        },
        {
            "created":0,
            "x":0,
            "y":1,
            "type":"m"
        },
        {
            "created":0,
            "x":14,
            "y":1,
            "type":"m"
        },
        {
            "created":0,
            "x":5,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":9,
            "y":2,
            "type":"m"
        },
        {
            "created":0,
            "x":9,
            "y":6,
            "type":"m"
        },
        {
            "created":0,
            "x":5,
            "y":6,
            "type":"m"
        },
        {
            "created":0,
            "x":11,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":3,
            "y":13,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":10,
            "type":"m"
        },
        {
            "created":0,
            "x":12,
            "y":10,
            "type":"m"
        },
        {
            "created":0,
            "x":2,
            "y":13,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":13,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":2,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":10,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":10,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":0,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":0,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":2,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":2,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":10,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":4,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":11,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":3,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":6,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":12,
            "y":5,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":2,
            "y":5,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":0,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":8,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":3,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":14,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":14,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":5,
            "y":9,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":9,
            "y":9,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":3,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":11,
            "y":1,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":13,
            "y":11,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":1,
            "y":11,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":8,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":6,
            "y":12,
            "type":"w",
            "hp":1
        },
        {
            "created":0,
            "x":14,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":2,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":11,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":1,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":6,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":6,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":3,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":4,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":14,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":13,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":3,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":11,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":4,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":10,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":9,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":9,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":12,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":2,
            "y":0,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":7,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":8,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":6,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":8,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":14,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":0,
            "y":5,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":5,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":9,
            "y":10,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":13,
            "y":12,
            "type":"o",
            "hp":3
        },
        {
            "created":0,
            "x":1,
            "y":12,
            "type":"o",
            "hp":3
        }
    ],
    "world":{
        "width":15,
        "height":15
    },
    "tick":0,
    "config":{
        "tick_rate_hz":10,
        "game_duration_ticks":300,
        "fire_spawn_interval_ticks":2
    }
},
    {
        "game_id": "mock_game_0",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    4,
                    9
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 8031
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    3,
                    13
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 4281
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    10,
                    9
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 6665
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    3,
                    11
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 5272
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    10,
                    1
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 7188
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    14,
                    5
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3486
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 7,
                "y": 6,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 13,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 9,
                "y": 5,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 7,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 4,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 7,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 5,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 7,
                "y": 12,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 2,
                "y": 10,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 9,
                "y": 11,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 0,
                "y": 8,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 4,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 14,
                "y": 14,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 0,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 3,
                "y": 14,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 2,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 9,
                "y": 14,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 0,
                "y": 1,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 8,
                "y": 4,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 8,
                "y": 9,
                "type": "m",
                "hp": 3
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 282,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_1",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    11,
                    5
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 1856
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    8,
                    2
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3596
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    3,
                    0
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 6303
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    5,
                    7
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 183
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    1,
                    4
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 5922
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    11,
                    14
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 5572
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 2,
                "y": 3,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 8,
                "y": 0,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 6,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 7,
                "y": 6,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 11,
                "y": 13,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 10,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 11,
                "y": 9,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 9,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 13,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 14,
                "y": 10,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 0,
                "y": 8,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 8,
                "y": 5,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 2,
                "y": 0,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 9,
                "y": 14,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 1,
                "y": 0,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 7,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 10,
                "y": 1,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 0,
                "y": 12,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 0,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 12,
                "type": "m",
                "hp": 1
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 255,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_2",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    6,
                    8
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3734
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    5,
                    1
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3254
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    0,
                    1
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 1738
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    8,
                    7
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 4546
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    10,
                    8
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 8725
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    6,
                    11
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 7864
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 13,
                "y": 2,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 3,
                "y": 4,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 4,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 10,
                "y": 11,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 6,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 0,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 12,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 2,
                "y": 0,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 4,
                "y": 13,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 8,
                "y": 13,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 9,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 5,
                "y": 2,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 4,
                "y": 10,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 4,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 5,
                "y": 6,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 0,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 5,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 7,
                "y": 5,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 8,
                "y": 1,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 11,
                "y": 7,
                "type": "w",
                "hp": 1
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 18,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_3",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    6,
                    4
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 919
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    9,
                    0
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 4724
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    2,
                    1
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 7037
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    4,
                    14
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 6709
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    1,
                    7
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 7749
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    11,
                    6
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 7229
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 5,
                "y": 5,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 8,
                "y": 7,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 5,
                "y": 7,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 10,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 0,
                "y": 1,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 12,
                "y": 1,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 8,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 0,
                "y": 4,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 7,
                "y": 7,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 8,
                "y": 9,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 14,
                "y": 0,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 2,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 11,
                "y": 11,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 12,
                "y": 9,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 5,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 9,
                "y": 1,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 3,
                "y": 8,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 8,
                "y": 14,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 3,
                "y": 4,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 6,
                "y": 14,
                "type": "w",
                "hp": 1
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 186,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_4",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    0,
                    2
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 2255
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    4,
                    6
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 8355
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    2,
                    14
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 7381
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    12,
                    0
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3075
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    3,
                    12
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 9546
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    8,
                    10
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 2064
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 7,
                "y": 0,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 3,
                "y": 9,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 14,
                "y": 11,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 6,
                "y": 14,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 10,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 5,
                "y": 12,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 12,
                "y": 13,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 6,
                "y": 6,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 9,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 2,
                "y": 0,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 14,
                "y": 4,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 3,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 7,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 7,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 3,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 12,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 1,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 7,
                "y": 10,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 2,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 4,
                "y": 10,
                "type": "m",
                "hp": 3
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 270,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_5",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    9,
                    14
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 82
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    0,
                    3
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 126
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    7,
                    8
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 4329
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    2,
                    7
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 733
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    8,
                    12
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 92
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    2,
                    4
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3590
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 10,
                "y": 4,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 10,
                "y": 12,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 0,
                "y": 7,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 6,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 4,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 5,
                "y": 14,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 11,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 12,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 0,
                "y": 11,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 2,
                "y": 6,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 1,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 8,
                "y": 5,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 5,
                "y": 0,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 0,
                "y": 6,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 2,
                "y": 11,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 2,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 9,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 2,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 0,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 11,
                "y": 13,
                "type": "o",
                "hp": 3
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 86,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_6",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    6,
                    14
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 6145
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    2,
                    11
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 7734
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    12,
                    7
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 6979
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    6,
                    4
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 1488
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    3,
                    13
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 8176
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    12,
                    8
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3520
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 2,
                "y": 5,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 5,
                "y": 14,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 5,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 6,
                "y": 0,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 5,
                "y": 13,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 14,
                "y": 11,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 1,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 4,
                "y": 6,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 14,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 0,
                "y": 3,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 3,
                "y": 11,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 12,
                "y": 10,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 9,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 0,
                "y": 14,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 9,
                "y": 8,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 1,
                "y": 3,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 11,
                "y": 11,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 7,
                "y": 12,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 2,
                "y": 0,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 14,
                "type": "w",
                "hp": 1
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 0,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_7",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    6,
                    4
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 9441
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    1,
                    9
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 5867
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    0,
                    12
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 1123
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    13,
                    3
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 4136
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    0,
                    8
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 4395
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    12,
                    12
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3133
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 1,
                "y": 11,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 3,
                "y": 4,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 0,
                "y": 9,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 1,
                "y": 12,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 12,
                "y": 10,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 7,
                "y": 14,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 6,
                "y": 3,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 1,
                "y": 5,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 2,
                "y": 0,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 5,
                "y": 3,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 14,
                "y": 2,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 6,
                "y": 13,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 8,
                "y": 2,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 7,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 14,
                "y": 0,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 13,
                "y": 4,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 0,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 8,
                "y": 4,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 2,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 5,
                "type": "o",
                "hp": 3
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 40,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_8",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    13,
                    9
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 6500
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    3,
                    14
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 7550
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    11,
                    8
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 9085
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    14,
                    14
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 8189
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    6,
                    3
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 9361
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    0,
                    14
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 6414
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 10,
                "y": 13,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 10,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 7,
                "y": 10,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 5,
                "y": 13,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 12,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 9,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 5,
                "y": 1,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 8,
                "y": 5,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 9,
                "y": 6,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 2,
                "y": 1,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 8,
                "y": 8,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 0,
                "y": 8,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 0,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 0,
                "y": 6,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 5,
                "y": 6,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 0,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 9,
                "y": 2,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 0,
                "y": 3,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 11,
                "y": 10,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 7,
                "type": "m",
                "hp": 3
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 120,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    },
    {
        "game_id": "mock_game_9",
        "agents": {
            "a": {
                "agent_id": "a",
                "unit_ids": [
                    "c",
                    "d",
                    "e"
                ]
            },
            "b": {
                "agent_id": "b",
                "unit_ids": [
                    "f",
                    "g",
                    "h"
                ]
            }
        },
        "unit_state": {
            "c": {
                "coordinates": [
                    10,
                    12
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 9262
                },
                "blast_diameter": 3,
                "unit_id": "c",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "d": {
                "coordinates": [
                    8,
                    11
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 5565
                },
                "blast_diameter": 3,
                "unit_id": "d",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "e": {
                "coordinates": [
                    6,
                    5
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 21
                },
                "blast_diameter": 3,
                "unit_id": "e",
                "agent_id": "a",
                "invulnerable": 0,
                "stunned": 0
            },
            "f": {
                "coordinates": [
                    4,
                    2
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 1711
                },
                "blast_diameter": 3,
                "unit_id": "f",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "g": {
                "coordinates": [
                    10,
                    2
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 694
                },
                "blast_diameter": 3,
                "unit_id": "g",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            },
            "h": {
                "coordinates": [
                    1,
                    0
                ],
                "hp": 3,
                "inventory": {
                    "bombs": 3871
                },
                "blast_diameter": 3,
                "unit_id": "h",
                "agent_id": "b",
                "invulnerable": 0,
                "stunned": 0
            }
        },
        "entities": [
            {
                "created": 0,
                "x": 7,
                "y": 5,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 4,
                "y": 0,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 2,
                "y": 14,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 3,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 4,
                "y": 1,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 0,
                "y": 12,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 6,
                "type": "w",
                "hp": 3
            },
            {
                "created": 0,
                "x": 7,
                "y": 10,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 10,
                "y": 8,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 7,
                "y": 6,
                "type": "o",
                "hp": 3
            },
            {
                "created": 0,
                "x": 9,
                "y": 9,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 6,
                "y": 7,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 7,
                "y": 4,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 14,
                "y": 6,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 10,
                "y": 10,
                "type": "o",
                "hp": 1
            },
            {
                "created": 0,
                "x": 2,
                "y": 4,
                "type": "m",
                "hp": 3
            },
            {
                "created": 0,
                "x": 7,
                "y": 11,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 13,
                "y": 4,
                "type": "w",
                "hp": 1
            },
            {
                "created": 0,
                "x": 1,
                "y": 12,
                "type": "m",
                "hp": 1
            },
            {
                "created": 0,
                "x": 12,
                "y": 9,
                "type": "o",
                "hp": 3
            }
        ],
        "world": {
            "width": 15,
            "height": 15
        },
        "tick": 282,
        "config": {
            "tick_rate_hz": 10,
            "game_duration_ticks": 300,
            "fire_spawn_interval_ticks": 2
        }
    }

]