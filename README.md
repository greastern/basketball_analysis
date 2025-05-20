# Basketball Analysis Project

This project uses YOLO (You Only Look Once) for basketball player and ball detection and analysis, managed with [uv](https://github.com/astral-sh/uv) for fast, reproducible Python environments.

## Setup

We use uv for all dependency and environment management. **You only need to run `uv sync` to set up your environment and install all dependencies.**

If you don't have uv installed, install it with:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd basketball_analysis
    ```

2. **Sync your environment and install all dependencies:**
    ```bash
    uv sync
    ```
    This single command will:
    - Create a `.venv` in your project folder (if it doesn't exist)
    - Install the correct Python version (if needed)
    - Install all dependencies listed in `pyproject.toml` and locked in `uv.lock`
    
    > **Why only `uv sync`?**
    > Unlike traditional Python workflows that require multiple steps (creating a venv, activating it, running pip install, etc.), `uv sync` does everything in one fast, reproducible step. You do **not** need to run `pip install` or `uv add ...` to install dependencies as a user—`uv sync` handles it all.
    >
    > For more on uv, see the [uv documentation](https://docs.astral.sh/uv/).

3. **Create a `.env` file in the project root and add your Roboflow API key:**
    ```
    ROBOFLOW_API_KEY=your_api_key_here
    ```
---

## Roboflow API Key

To use this project for training, downloading datasets, or working with Roboflow resources, you will need a Roboflow API key.

- **Why do you need a Roboflow API key?**
    - To download datasets from Roboflow (as in the provided notebooks)
    - To train or retrain models using Roboflow datasets
    - To use your own Roboflow projects or datasets in new notebooks

- **How to get a Roboflow API key:**
    1. Go to [Roboflow](https://roboflow.com/).
    2. Sign up for a free account or log in.
    3. In your Roboflow dashboard, click your profile icon and select "Settings" or "API Keys".
    4. Copy your private API key.
    5. Add it to your `.env` file as shown above.

If you do not plan to use Roboflow datasets or retrain models, you may not need the API key, but it is required for the provided training notebooks.

---

## Project Structure

- `Training_notebooks/BballDetection.ipynb`: Jupyter notebook for training the model to track the ball better.
- `Training_notebooks/basketball_player_detection_training.ipynb`: Main notebook for tracking players and the ball.
- `main.py`: Main script for running predictions.
- `input_videos/`: Directory for input videos (gitignored).
- `runs/`: Directory for training outputs (gitignored).
- `Basketball-Players-25/`: Dataset directory (gitignored).

---

## Usage

1. Place your input videos in the `input_videos/` directory.

2. **To run the main script:**
    ```bash
    uv run python main.py
    ```

3. **To launch a Jupyter notebook:**
    ```bash
    uv run jupyter notebook
    ```
    Then open and use the notebooks in the `Training_notebooks/` directory.

---

## Environment Variables

- The `.env` file stores sensitive credentials such as your Roboflow API key.
- This file is gitignored and should never be committed to the repository.
- Example `.env` content:
    ```
    ROBOFLOW_API_KEY=your_api_key_here
    ```

---

## No License

No license is currently specified for this project.  
If you wish to use, modify, or distribute this code, please contact the author.

---

## Contact

For questions or support, contact: gaius@stitchit.io
