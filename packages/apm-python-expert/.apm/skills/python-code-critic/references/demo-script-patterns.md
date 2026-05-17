# Demo Script Patterns

This document outlines common patterns for creating small, executable demo scripts to visualize or test code functionality, focusing on Python and TypeScript.

## General Principles

- **Minimalism:** Keep demo scripts as small and focused as possible.
- **Isolation:** Aim to import only the necessary functions or classes.
- **Clear Output:** Ensure the script produces clear, easy-to-understand output.
- **Temporary:** These scripts are typically temporary and can be discarded after use.

## Python (Preferred)

### Pattern 1: Direct Function Call

For demonstrating a single function's behavior.

```python
# demo_my_function.py
import sys
import os

# Add the project's root directory to the Python path
# This allows importing modules from your project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Assuming your function is in 'src/my_module.py'
from src.my_module import my_function

def main():
    """Main function to run the demo."""
    print("--- Running Demo for my_function ---")
    
    # Example 1: Valid inputs
    try:
        result = my_function('some_input', 123)
        print(f"Result of my_function(valid): {result}")
    except Exception as e:
        print(f"An error occurred with valid inputs: {e}")

    # Example 2: Edge case
    try:
        result = my_function(None, 0)
        print(f"Result of my_function(edge case): {result}")
    except Exception as e:
        print(f"An error occurred with edge case inputs: {e}")

    print("--- Demo Finished ---")

if __name__ == "__main__":
    main()
```

### Pattern 2: Visual Output (e.g., using Matplotlib)

**Installation:** `pip install matplotlib`

```python
# demo_plot_data.py
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_generator import generate_data_points

def main():
    """Generates and plots data."""
    print("--- Generating data for plotting demo ---")
    data = generate_data_points(count=100)
    
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title("Visualization of Generated Data")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    
    # Save the plot to a file instead of showing it interactively
    # This is often better for agent-driven workflows
    output_filename = "data_plot.png"
    plt.savefig(output_filename)
    
    print(f"--- Plot saved to {output_filename} ---")

if __name__ == "__main__":
    main()
```

## TypeScript (Fallback)

### Pattern: Class Instantiation and Method Call (Node.js)

```typescript
// demoMyClass.ts
import { MyClass } from './path/to/myClass'; // Adjust path as needed

async function runDemo() {
  console.log('--- Running Demo for MyClass ---');

  try {
    // Initialize with some config
    const instance = new MyClass({ setting: 'prod' });

    // Call an async method
    const output = await instance.someAsyncMethod('test_data');
    console.log(`Output of MyClass.someAsyncMethod:`, output);

  } catch (error) {
    console.error('An error occurred during the demo:', error);
  }

  console.log('--- Demo Finished ---');
}

runDemo();
```
