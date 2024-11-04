# Project Name

This project classifies documents in the `20news-bydate` dataset using the Llama API.

## Project Structure
- `20news-bydate/`: The dataset directory containing news articles.
- `.env`: Environment file storing your API key.
- `config.json`: Configuration file containing model and cost parameters.
- `functions.py`: Contains the core functions for data loading, token counting, and cost estimation.
- `run.py`: Script for running different parts of the classification process.
- `requirements.txt`: Python dependencies.

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

## Running the Model

You can use `run.py` to execute different tasks in the project. This script accepts command-line arguments for flexibility, allowing you to load data and run specific models.

### Load the Dataset Only

To load the dataset without running a model:

```bash
python run.py data
```

### Load Data and Run a Specific Model

Run with both `data` and `test` targets, and specify the model name as the last argument:

```bash
python run.py data test Meta-Llama-3.1-8B-Instruct
```
