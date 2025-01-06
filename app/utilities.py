"""app/utilities.py.

Misc functions used in the program.
"""

import os
import json
from typing import List
from app.models.repeater import Repeaters

async def get_db():
    """Dependency function to load repeaters from JSON."""
    return load_repeaters_from_json('db')

def load_repeaters_from_json(db_dir: str) -> List[Repeaters]:
    """Loads repeaters data from JSON files in the given directory.

    Args:
        db_dir: Path to the directory containing the JSON files.

    Returns:
        List of Repeater objects.
    """
    repeaters = []
    for filename in os.listdir(db_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(db_dir, filename)
            with open(file_path, 'r') as f:
                try:
                    repeater_data = json.load(f)
                    repeater = Repeaters(**repeater_data)  # Create Repeater object
                    repeaters.append(repeater)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {file_path}")
                except KeyError as e:
                    print(f"Missing key '{e}' in file: {file_path}") 
    return repeaters
