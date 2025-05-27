#!/usr/bin/env python3
"""
Simple User Engagement Analytics
Usage: python simple_main_script.py [options]
"""

import argparse
import os
import json
import pandas as pd
from data_processor import DataProcessor, DataGenerator
from metrics_calculator import MetricsCalculator
from html_generator import HTMLGenerator


def main():
    parser = argparse.ArgumentParser(description='User Engagement Analytics')
    parser.add_argument('--input', help='Input CSV file')
    parser.add_argument('--users', type=int, default=500, help='Number of users to generate')
    parser.add_argument('--days', type=int, default=90, help='Number of days to simulate')
    parser.add_argument('--scenario', default='standard',
                        choices=['standard', 'high_engagement', 'low_retention', 'rapid_growth'],
                        help='Data generation scenario')
    parser.add_argument('--output', default='output', help='Output directory')

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)

    print("🚀 Starting User Engagement Analytics...")

    # Generate or load data
    if args.input:
        print(f"📂 Loading data from {args.input}...")
        input_file = args.input
    else:
        print(f"🎲 Generating {args.scenario} scenario ({args.users} users, {args.days} days)...")
        generator = DataGenerator()
        df_raw = generator.generate(users=args.users, days=args.days, scenario=args.scenario)

        input_file = f"{args.output}/generated_data.csv"
        df_raw.to_csv(input_file, index=False)
        print(f"✅ Created {len(df_raw)} interactions from {df_raw['User ID'].nunique()} users")

    # Process data
    print("📊 Processing data...")
    processor = DataProcessor()
    df = processor.process_csv(input_file)

    # Calculate metrics
    print("📈 Calculating metrics...")
    calculator = MetricsCalculator()
    metrics = calculator.calculate_all_metrics(df)

    # Generate reports
    print("📋 Generating reports...")

    # JSON metrics
    with open(f"{args.output}/metrics.json", 'w') as f:
        json.dump(metrics, f, indent=2, default=str)

    # CSV summary
    summary_data = {
        'Metric': [
            'Total Users', 'Total Interactions', 'Avg DAU', 'Avg Session Duration (min)',
            '1-day Retention (%)', '7-day Retention (%)', 'Churn Rate (%)'
        ],
        'Value': [
            df['User_ID'].nunique(), len(df), round(metrics['avg_dau'], 1),
            round(metrics['avg_session_duration'], 1),
            round(metrics['retention_rates']['1_day'] * 100, 1),
            round(metrics['retention_rates']['7_day'] * 100, 1),
            round(metrics['churn_rate'] * 100, 1)
        ]
    }
    pd.DataFrame(summary_data).to_csv(f"{args.output}/summary.csv", index=False)

    # HTML report
    html_generator = HTMLGenerator()
    html_generator.generate_report(metrics, f"{args.output}/report.html")

    # Results summary
    print(f"\n🎉 Analysis Complete!")
    print(f"📊 Users: {df['User_ID'].nunique()} | Interactions: {len(df)}")
    print(f"📈 DAU: {metrics['avg_dau']:.1f} | Session: {metrics['avg_session_duration']:.1f}min")
    print(
        f"🔄 Retention: {metrics['retention_rates']['1_day']:.1%} (1d) | {metrics['retention_rates']['7_day']:.1%} (7d)")

    top_features = sorted(metrics['feature_usage'].items(), key=lambda x: x[1], reverse=True)[:3]
    print(f"🎯 Top Features: {', '.join([f'{k}({v})' for k, v in top_features])}")
    print(f"📁 Reports: {args.output}/")


def interactive_mode():
    """Simple interactive mode for easy usage"""
    print("User Engagement Analytics")
    print("1. Generate Standard Data (500 users, 90 days)")
    print("2. Process Existing File")

    choice = input("Choose option (1-2): ").strip()

    if choice == "1":
        run_analysis(users=500, days=90, scenario='standard')
    elif choice == "2":
        filename = input("CSV filename: ")
        if os.path.exists(filename):
            run_analysis(input_file=filename)
        else:
            print(f"File {filename} not found")
    else:
        print("Invalid choice")


def run_analysis(users=None, days=None, scenario='standard', input_file=None):
    """Run analysis with given parameters"""
    import sys

    if input_file:
        sys.argv = ['script', '--input', input_file]
    else:
        sys.argv = ['script', '--users', str(users), '--days', str(days), '--scenario', scenario]

    main()


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        interactive_mode()
    else:
        main()