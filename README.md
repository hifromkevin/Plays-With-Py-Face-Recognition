# Plays-With-Py-Face-Recognition

A facial recognition app designed to integrate with my Magic Mirror, building user profiles based on recognized faces.

## Setup Instructions (Mac)

### Prerequisites

Ensure you have the following installed:

- **Xcode Command Line Tools**
- **Homebrew**
- **Python 3**

### Installation Steps

1. **Install Xcode Command Line Tools**

   ```bash
   xcode-select --install
   ```

2. **Install Homebrew (if not already installed)**

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Install Python**

   ```bash
   brew install python3
   ```

4. **Install CMake**

   ```bash
   brew install cmake
   ```

5. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

6. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

7. **Run the Project**

   ```bash
   python main.py
   ```

8. **Deactivate the Virtual Environment (when done)**
   ```bash
   deactivate
   ```
