# Basic Math Operations

A simple Python project demonstrating basic math operations and unit testing with `pytest`.

## Project Structure

- `math_ops.py`: Contains basic math functions (`add`, `subtract`) and their corresponding tests.
- `requirements.txt`: Project dependencies.

## Getting Started

### Using GitHub Codespaces

GitHub Codespaces provides a complete, pre-configured dev environment in the cloud.

1.  **Open in Codespaces:**
    - Click the **Code** button on your repository's GitHub page.
    - Select the **Codespaces** tab.
    - Click **Create codespace on main**.

2.  **Environment Setup:**
    Once the Codespace is ready, it will automatically open a terminal. The environment will be pre-configured with Python.

3.  **Install Dependencies:**
    Run the following command in the terminal:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Tests:**
    To run the unit tests, use:
    ```bash
    pytest math_ops.py
    ```

### Local Setup

If you prefer to run the project locally:

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd basic-unit
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Tests:**
    ```bash
    pytest math_ops.py
    ```

## Running the Code

You can use the functions in `math_ops.py` in your own Python scripts:

```python
from math_ops import add, subtract

print(add(5, 3))       # Output: 8
print(subtract(10, 4)) # Output: 6
```
