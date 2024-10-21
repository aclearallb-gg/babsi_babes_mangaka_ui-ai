import json
import os
from typing import Dict, Any, Tuple, List

PROJECTS_DIR = 'projects'
UNDO_STACK: List[Tuple[str, str]] = []

def save_project(project_data: Dict[str, Any]) -> str:
    """
    Save a project to a JSON file.

    Args:
        project_data (Dict[str, Any]): The project data to save.

    Returns:
        str: A message indicating the success of the operation.

    Raises:
        IOError: If there's an error writing to the file.
    """
    if not os.path.exists(PROJECTS_DIR):
        os.makedirs(PROJECTS_DIR)
    
    project_id = len(os.listdir(PROJECTS_DIR)) + 1
    filename = f"{PROJECTS_DIR}/project_{project_id}.json"
    
    try:
        with open(filename, 'w') as f:
            json.dump(project_data, f)
    except IOError as e:
        raise IOError(f"Error saving project: {e}")
    
    UNDO_STACK.append(('save', filename))
    return f"Project saved successfully with ID: {project_id}"

def load_project(project_id: int) -> Dict[str, Any]:
    """
    Load a project from a JSON file.

    Args:
        project_id (int): The ID of the project to load.

    Returns:
        Dict[str, Any]: The loaded project data.

    Raises:
        FileNotFoundError: If the project file is not found.
        json.JSONDecodeError: If there's an error decoding the JSON file.
    """
    filename = f"{PROJECTS_DIR}/project_{project_id}.json"
    
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Project with ID {project_id} not found")
    
    try:
        with open(filename, 'r') as f:
            project_data = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error decoding project file: {e}")
    
    return project_data

def undo_action(action_id: str) -> str:
    """
    Undo the last action.

    Args:
        action_id (str): The ID of the action to undo (currently unused).

    Returns:
        str: A message indicating the result of the undo operation.
    """
    if not UNDO_STACK:
        return "No actions to undo"
    
    action, data = UNDO_STACK.pop()
    
    if action == 'save':
        try:
            os.remove(data)
            return f"Removed saved project: {data}"
        except OSError as e:
            return f"Error removing saved project: {e}"
    
    return "Undo action not supported"
