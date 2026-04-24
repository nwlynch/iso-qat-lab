import os
from typing import Dict, Any
from .generator import generate_playwright_test, generate_markdown_report

# This module handles the parsing of raw mock requirement documents.
# It reads markdown files from the specified directory and transforms them 
# into structured JSON/Dict format usable by the generator.

REQUIREMENTS_DIR = "tests/requirements"

def parse_requirement_file(file_path: str) -> Dict[str, Any]:
    """
    Reads a single markdown requirement file and extracts structured test data.
    """
    print(f"Parsing: {os.path.basename(file_path)}")
    
    # Placeholder logic: A complex NLP/Regex parsing logic would go here.
    # For now, we simulate reading the structure from the first line of the file.
    
    return {
        "source_file": os.path.basename(file_path),
        "title": "Parsed Title from file",
        "description": "Mock description extracted from the file content.",
        "steps": [
            {"description": "Step 1: Navigate and Locate element X."},
            {"description": "Step 2: Assert state change Y."}
        ],
        "selector": "#mock-element"
    }

def load_all_requirements() -> List[Dict[str, Any]]:
    """
    Loads and parses all requirement documents in the directory.
    """
    all_scenarios = []
    if not os.path.exists(REQUIREMENTS_DIR):
        print(f"Error: Requirements directory {REQUIREMENTS_DIR} not found.")
        return []

    for filename in os.listdir(REQUIREMENTS_DIR):
        if filename.endswith(".md"):
            file_path = os.path.join(REQUIREMENTS_DIR, filename)
            try:
                scenario = parse_requirement_file(file_path)
                all_scenarios.append(scenario)
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
                
    return all_scenarios

# Example usage:
if __name__ == "__main__":
    scenarios = load_all_requirements()
    if scenarios:
        print(f"Successfully parsed {len(scenarios)} scenarios.")
