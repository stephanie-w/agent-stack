import ast
import sys
from pathlib import Path

def summarize(file_path: str):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: {file_path} not found.")
        sys.exit(1)
    
    with path.open("r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    print(f"Summary of {file_path}:")
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            print(f"  Class: {node.name}")
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    print(f"    Method: {item.name}")
        elif isinstance(node, ast.FunctionDef):
            print(f"  Function: {node.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarize_module.py <path_to_python_file>")
        sys.exit(1)
    summarize(sys.argv[1])
