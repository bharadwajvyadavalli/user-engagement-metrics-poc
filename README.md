# User Engagement Metrics POC

Simple proof-of-concept for analyzing user engagement from chatbot interaction data.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run analysis:
```bash
python main.py --input sample_data.csv
```

## Data Format

CSV with columns:
- **ID**: Auto-generated key
- **Event Date**: Timestamp (YYYY-MM-DD HH:MM:SS)
- **User ID**: Unique user identifier  
- **Thread ID**: Session identifier
- **Message**: JSON with `{"role": "human|ai", "content": "text"}`

## Metrics Calculated

- Daily Active Users (DAU)
- Monthly Active Users (MAU)
- Session Duration
- Session Frequency  
- Queries per Session
- Feature Usage
- Retention Rate (1, 7, 30 days)
- Churn Rate

## Output

- `output/executive_summary.html` - Main report
- `output/metrics_summary.csv` - Data export
- `output/charts/` - Visualizations

## Usage

```bash
python main.py --input your_data.csv --output results/
```

Simple POC - modify `config.py` to customize settings.