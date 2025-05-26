# Quick Setup Guide - User Engagement Metrics POC

## Files to Download/Create

Save each file in the same directory:

1. **README.md** - Project documentation
2. **requirements.txt** - Python dependencies  
3. **config.py** - Configuration settings
4. **main.py** - Main script to run
5. **data_processor.py** - Data processing logic
6. **metrics_calculator.py** - Metrics calculation
7. **visualizer.py** - Chart generation
8. **report_generator.py** - HTML report creation
9. **sample_data.csv** - Test data

## Quick Start

1. **Create project folder:**
```bash
mkdir user-engagement-poc
cd user-engagement-poc
```

2. **Save all the files above to this folder**

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the POC:**
```bash
python main.py --input sample_data.csv
```

5. **View results:**
- Open `output/executive_summary.html` in your browser
- Check `output/charts/` for individual chart files
- Review `output/metrics_summary.csv` for raw data

## Using Your Own Data

Replace `sample_data.csv` with your CSV file that has:
- ID, Event Date, User ID, Thread ID, Message columns
- Message column with JSON: `{"role": "human|ai", "content": "text"}`

## Customization

Edit `config.py` to:
- Change retention periods 
- Modify churn threshold
- Add/remove feature keywords
- Adjust chart settings

That's it! Simple POC ready to run. 🚀