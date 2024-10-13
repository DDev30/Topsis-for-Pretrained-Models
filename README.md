
---

# TOPSIS Model Evaluation

## Overview
This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) methodology for evaluating different models based on multiple performance metrics. The project consists of two main Python scripts: `main.py` and `Topsis.py`.

### Files
- **`main.py`**: The main script that loads the data, applies the TOPSIS algorithm, and outputs the results.
- **`Topsis.py`**: Contains the implementation of the TOPSIS algorithm.

## Installation
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Required Libraries
You need the following Python libraries to run the scripts:
- NumPy
- Pandas

You can install them using pip:
```bash
pip install numpy pandas
```

## Usage

To run the TOPSIS evaluation, use the following command in your terminal:

```bash
python main.py <Sample_Input.csv> <output_file.csv> [--weights <weight1> <weight2> <weight3> <weight4> <weight5>]
```

### Parameters:
- **`Sample_Input.csv`**: The input CSV file containing the model performance metrics.
- **`output_file.csv`**: The output CSV file where the results will be saved.
- **`--weights`**: Optional weights for the metrics. If not provided, default weights of 0.25 will be used for each metric.

## Sample Input

### Sample CSV Format
Your input CSV file should have the following structure:

| Text | Models | Accuracy | Precision | Recall | F1_score | ROC-AUC |
|------|--------|----------|-----------|--------|----------|---------|
| T1   | M1     | 0.85     | 0.75      | 0.80   | 0.77     | 0.88    |
| T1   | M2     | 0.90     | 0.80      | 0.85   | 0.82     | 0.91    |
| T2   | M1     | 0.88     | 0.76      | 0.79   | 0.78     | 0.90    |

### Example Commands
With specified weights:
```bash
python main.py Sample_Input.csv output_file.csv --weights 0.3 0.2 0.2 0.2 0.1
```

Without specifying weights (default weights of 0.25 will be used):
```bash
python main.py Sample_Input.csv output_file.csv
```

## Output
The output will be saved in the specified output CSV file, containing the TOPSIS scores and rankings for each model based on the input metrics.

---
