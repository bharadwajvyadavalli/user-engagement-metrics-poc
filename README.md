# User Engagement Analytics

Simple tool to analyze user engagement from chatbot interaction data.

## What it calculates

- **Daily Active Users (DAU)** - Unique users per day
- **Monthly Active Users (MAU)** - Unique users per month  
- **Session Duration** - How long users stay engaged
- **Session Frequency** - How many sessions per user
- **Queries per Session** - Questions asked per conversation
- **Feature Usage** - Which features users engage with most
- **Retention Rate** - Users who return after 1, 7, 30 days
- **Churn Rate** - Users who stopped using the system

## Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run analysis (super simple - no arguments needed!):**
```bash
python main.py
```

**Or with custom data:**
```bash
python main.py --input your_data.csv --output results/
```

3. **View results:**
- Check console output for key metrics
- Open `output/metrics.json` for detailed data
- Open `output/summary.csv` for spreadsheet format
- Open `output/report.html` for visual dashboard

## Data Format

Your CSV needs these columns:

| Column | Example |
|--------|---------|
| ID | 1 |
| Event Date | 2024-01-01 10:00:00 |
| User ID | user001 |
| Thread ID | thread001 |  
| Message | {"role": "human", "content": "Hello"} |

## Files

- `data_processor.py` - Cleans and processes raw data
- `metrics_calculator.py` - Calculates engagement metrics  
- `html_generator.py` - Creates HTML dashboard
- `main.py` - Main script to run everything
- `sample_data.csv` - Example data to test with

## Example Output

```
python main.py

🚀 Starting User Engagement Analysis...
📊 Processing data...
✅ Processed 20 interactions from 5 users
📈 Calculating metrics...
📋 Generating reports...

🎉 Analysis Complete!
📊 Key Results:
   Daily Active Users: 2.0
   Monthly Active Users: 5.0
   Avg Session Duration: 0.6 minutes
   Churn Rate: 0.0%

🎯 Feature Usage:
   help: 5 uses
   search: 4 uses
   analysis: 4 uses

📈 Retention Rates:
   1_day: 40.0%
   7_day: 0.0%
   30_day: 0.0%
```

That's it! Simple and effective user engagement analysis.