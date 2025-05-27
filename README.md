# User Engagement Analytics

Complete analytics tool for chatbot interaction data with realistic data generation and comprehensive metrics.

## 🚀 Quick Start

### Simple Usage (Recommended)
```bash
python simple_main_script.py
```
Choose option 1 to generate **500 users over 90 days** with realistic interaction patterns.

### Command Line Usage
```bash
# Default: 500 users, 90 days
python simple_main_script.py

# Custom parameters
python simple_main_script.py --users 1000 --days 180

# Process existing file
python simple_main_script.py --input your_data.csv

# Different scenarios
python simple_main_script.py --scenario high_engagement
```

## 📊 What You Get

- **~30,000 interactions** from **500 users** over **90 days**
- **Professional reports** - HTML dashboard, JSON metrics, CSV summary
- **Realistic patterns** - Business hours, weekends, user retention curves
- **Multiple scenarios** - Standard, high engagement, low retention, rapid growth

## 📋 Data Format

Your CSV needs these columns (see `sample_data.csv`):

| Column | Example | Description |
|--------|---------|-------------|
| ID | 1 | Message ID |
| Event Date | 2024-01-01 10:00:00 | Timestamp |
| User ID | user001 | User identifier |
| Thread ID | thread001 | Conversation thread |
| Message | {"role": "human", "content": "Hello"} | JSON with role and content |

## 🎯 Metrics Calculated

- **Daily/Monthly Active Users** - User engagement over time
- **Session Duration** - Average time spent per conversation
- **Retention Rates** - Users returning after 1, 7, 30 days
- **Churn Rate** - Users who stopped using the system
- **Feature Usage** - Which features users engage with most

## 👥 User Types

| Type | Behavior | Sessions | Queries/Session |
|------|----------|----------|-----------------|
| **New Users** (30%) | Exploring basics | 1-3 | 1-4 |
| **Casual Users** (40%) | Regular usage | 2-6 | 1-6 |
| **Power Users** (30%) | Heavy usage | 3-10 | 2-12 |

## 🎨 Feature Categories

- **Help** - Getting started, guidance
- **Search** - Finding documents, data
- **Analysis** - Data insights, trends
- **Export** - Downloading, saving
- **Chat** - Conversations, questions
- **API** - Integration, documentation
- **Reporting** - Dashboards, KPIs
- **Automation** - Workflows, scheduling

## 📁 Project Structure

```
├── simple_main_script.py      # Main script - run this
├── data_processor.py          # Data processing + generation
├── metrics_calculator.py      # Engagement metrics calculation
├── html_generator.py          # Professional HTML reports
├── config_file.py             # Configuration settings
├── sample_data.csv            # Example input format
├── requirements.txt           # Dependencies
└── output/                    # Generated reports
    ├── report.html            # Interactive dashboard
    ├── metrics.json           # Detailed metrics
    ├── summary.csv            # Key metrics summary
    └── generated_data.csv     # Raw data (if generated)
```

## 💡 Example Output

```bash
🚀 Starting User Engagement Analytics...
🎲 Generating standard scenario (500 users, 90 days)...
✅ Created 28,547 interactions from 456 users
📊 Processing data...
📈 Calculating metrics...
📋 Generating reports...

🎉 Analysis Complete!
📊 Users: 456 | Interactions: 28,547
📈 DAU: 24.3 | Session: 1.8min
🔄 Retention: 45% (1d) | 28% (7d)
🎯 Top Features: help(5247), search(4891), analysis(4156)
📁 Reports: output/
```

## 🎯 Usage Scenarios

### Development & Testing
```bash
# Generate test dataset
python simple_main_script.py --users 100 --days 30
```

### Production Analysis
```bash
# Standard analysis (default)
python simple_main_script.py

# Large-scale analysis
python simple_main_script.py --users 2000 --days 180
```

### Different Scenarios
```bash
# High engagement users
python simple_main_script.py --scenario high_engagement

# Low retention simulation
python simple_main_script.py --scenario low_retention

# Rapid growth pattern
python simple_main_script.py --scenario rapid_growth
```

## 🔧 Installation

```bash
# Install dependencies
pip install pandas

# Run analysis
python simple_main_script.py
```

## 📈 Report Outputs

- **HTML Dashboard** (`output/report.html`) - Visual metrics with charts
- **JSON Metrics** (`output/metrics.json`) - Raw data for analysis
- **CSV Summary** (`output/summary.csv`) - Key metrics for spreadsheets

Perfect for understanding user behavior, measuring engagement, and making data-driven decisions! 🎯