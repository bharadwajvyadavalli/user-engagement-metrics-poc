# User Engagement Analytics

Complete analytics tool for chatbot interaction data with realistic data generation and comprehensive metrics.

## ✨ Features

- **Generate Realistic Data** - Create datasets with 3 user types, 8 feature categories, and temporal patterns
- **Comprehensive Analytics** - DAU, MAU, retention, churn, session metrics, and feature usage
- **Professional Reports** - Interactive HTML dashboard, JSON metrics, and CSV summaries
- **Flexible Usage** - Process existing data or generate new datasets for testing

## 🚀 Quick Start

### Option 1: Interactive Mode (Recommended)
```bash
python simple_main_script.py
```
Choose from:
1. **Quick Demo** (200 users, 30 days) - Perfect for testing
2. **Custom Analysis** - Specify user count and time period
3. **Process Existing File** - Use your own CSV data

### Option 2: Command Line
```bash
# Generate realistic dataset and analyze
python simple_main_script.py --users 1000 --days 90

# Process existing file
python simple_main_script.py --input sample_data.csv

# Custom output directory
python simple_main_script.py --users 500 --output results/
```

## 📊 What You Get

### Realistic Data Generation
- 10,000+ interactions from 500+ users over 60+ days
- Meaningful retention curves (e.g., 45% → 28% → 15%)
- Rich temporal patterns and user segmentation
- Feature adoption analysis

### Reports Generated
- **📈 HTML Dashboard** (`output/report.html`) - Interactive visual report
- **📊 JSON Metrics** (`output/metrics.json`) - Detailed data for further analysis  
- **📋 CSV Summary** (`output/summary.csv`) - Key metrics for spreadsheets
- **📂 Raw Data** (`output/generated_data.csv`) - Generated dataset (if applicable)

## 📋 Data Format

Your CSV needs these columns (see `sample_data.csv` for example):

| Column | Example | Description |
|--------|---------|-------------|
| ID | 1 | Message ID |
| Event Date | 2024-01-01 10:00:00 | Timestamp |
| User ID | user001 | User identifier |
| Thread ID | thread001 | Conversation thread |
| Message | {"role": "human", "content": "Hello"} | JSON with role and content |

## 🎯 Metrics Calculated

### User Activity
- **Daily Active Users (DAU)** - Unique users per day
- **Monthly Active Users (MAU)** - Unique users per month
- **User Growth** - New user acquisition patterns

### Engagement Quality  
- **Session Duration** - Average time spent per session
- **Queries per Session** - Depth of user engagement
- **Sessions per User** - Usage frequency

### Retention & Health
- **Retention Rates** - Users returning after 1, 7, 30 days
- **Churn Rate** - Users who stopped using the system
- **Activity Patterns** - Business hours vs off-hours usage

### Feature Analytics
- **Feature Usage** - Which features users engage with most
- **Feature Adoption** - How features spread through user base
- **User Journey** - Path from new user to power user

## 👥 User Types Generated

The data generator creates three distinct user personas:

| Type | Behavior | Sessions | Queries/Session | Retention |
|------|----------|----------|-----------------|-----------|
| **New Users** (30%) | Exploring basics | 1-3 | 1-4 | 60% |
| **Casual Users** (40%) | Regular but light usage | 2-6 | 1-6 | 70% |
| **Power Users** (30%) | Heavy, advanced usage | 3-10 | 2-12 | 85% |

## 🎨 Feature Categories

- **Help** - Getting started, guidance, support
- **Search** - Finding documents, data, files
- **Analysis** - Data insights, trends, reports  
- **Export** - Downloading, saving, sharing
- **Chat** - Conversations, questions, discussions
- **API** - Integration, documentation, endpoints
- **Reporting** - Dashboards, KPIs, summaries
- **Automation** - Workflows, scheduling, alerts

## 📁 Project Structure

```
├── simple_main_script.py      # Main script - run this
├── data_processor.py          # Data processing + generation
├── metrics_calculator.py      # Engagement metrics calculation
├── html_generator.py          # Professional HTML reports
├── config_file.py             # Configuration settings
├── sample_data.csv            # Example input format
├── requirements.txt           # Dependencies (pandas>=1.5.0)
└── output/                    # Generated reports
    ├── report.html            # Interactive dashboard
    ├── metrics.json           # Detailed metrics
    ├── summary.csv            # Key metrics summary
    └── generated_data.csv     # Raw data (if generated)
```

## 🔧 Installation

```bash
# Install dependencies
pip install pandas

# Run analysis
python simple_main_script.py
```

## 💡 Example Output

```
🚀 Starting Complete User Engagement Analytics...
🎲 Generating realistic data (500 users, 60 days)...
✅ Created 15,847 interactions from 423 users
📊 Processing data...
📈 Calculating engagement metrics...
📋 Generating reports...

🎉 Analysis Complete!
📊 Key Results:
   Total Users: 423
   Average Daily Active Users: 28.5
   1-day Retention: 45.2%
   7-day Retention: 28.7%  
   Churn Rate: 12.3%

🎯 Top Features:
   help: 3,247 uses
   search: 2,891 uses
   analysis: 2,456 uses

📁 Reports Generated:
   📊 Metrics: output/metrics.json
   📈 Summary: output/summary.csv
   🌐 Dashboard: output/report.html
```

## 🎯 Use Cases

### Testing & Development
```bash
# Quick validation with sample data
python simple_main_script.py --input sample_data.csv

# Generate test dataset
python simple_main_script.py --users 200 --days 30
```

### Production Analysis
```bash
# Large-scale insights
python simple_main_script.py --users 5000 --days 180
```

### Historical Data Analysis
```bash
# Process your existing data
python simple_main_script.py --input your_chatbot_data.csv
```

### Comparative Analysis
```bash
# Compare different periods
python simple_main_script.py --input q1_data.csv --output q1_results/
python simple_main_script.py --input q2_data.csv --output q2_results/
```

## ⚙️ Configuration

Customize behavior by editing `config_file.py`:

- **Retention periods** - Adjust analysis timeframes
- **Churn threshold** - Define inactive user criteria  
- **Feature keywords** - Modify feature detection
- **Chart settings** - Customize report appearance

## 🚀 Advanced Features

- **Temporal Patterns** - Business hours, weekends, seasonal trends
- **Realistic User Behavior** - Gradual activity decay over time
- **Feature Extraction** - Automatic categorization of user intents
- **Session Analysis** - Conversation flow and engagement depth
- **Multiple Output Formats** - HTML, JSON, CSV for different use cases

## 🔍 Understanding the Reports

### HTML Dashboard (`output/report.html`)
- Visual metrics with charts and indicators
- Color-coded performance levels
- Daily activity breakdown
- Feature usage analytics

### JSON Metrics (`output/metrics.json`)
- Raw data for programmatic analysis
- All calculated metrics with timestamps
- Detailed breakdowns by date and feature

### CSV Summary (`output/summary.csv`)
- Key metrics in spreadsheet format
- Easy to import into other tools
- Perfect for executive reporting

Transform your chatbot data into actionable insights with professional-grade analytics! 🎯