#!/usr/bin/env python3
"""
Simple User Engagement Analysis
Usage: python main.py --input sample_data.csv
"""

import argparse
import os
import json
import pandas as pd
from data_processor import DataProcessor
from metrics_calculator import MetricsCalculator
from html_generator import HTMLGenerator


def main():
    parser = argparse.ArgumentParser(description='User Engagement Analysis')
    parser.add_argument('--input', required=True, help='Input CSV file')
    parser.add_argument('--output', default='output', help='Output directory')

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    print("🚀 Starting User Engagement Analysis...")

    # Step 1: Process data
    print("📊 Processing data...")
    processor = DataProcessor()
    df = processor.process_csv(args.input)
    print(f"✅ Processed {len(df)} interactions from {df['User_ID'].nunique()} users")

    # Step 2: Calculate metrics
    print("📈 Calculating metrics...")
    calculator = MetricsCalculator()
    metrics = calculator.calculate_all_metrics(df)

    # Step 3: Generate outputs
    print("📋 Generating reports...")

    # Save JSON report
    with open(f"{args.output}/metrics.json", 'w') as f:
        json.dump(metrics, f, indent=2, default=str)

    # Save CSV summary
    summary_data = {
        'Metric': [
            'Average DAU', 'Average MAU', 'Avg Session Duration (min)',
            'Avg Sessions per User', 'Avg Queries per Session', 'Churn Rate (%)'
        ],
        'Value': [
            round(metrics['avg_dau'], 1),
            round(metrics['avg_mau'], 1),
            round(metrics['avg_session_duration'], 1),
            round(metrics['avg_sessions_per_user'], 1),
            round(metrics['avg_queries_per_session'], 1),
            round(metrics['churn_rate'] * 100, 1)
        ]
    }
    pd.DataFrame(summary_data).to_csv(f"{args.output}/summary.csv", index=False)

    # Generate HTML report
    html_generator = HTMLGenerator()
    html_generator.generate_report(metrics, f"{args.output}/report.html")

    # Print key results
    print("\n🎉 Analysis Complete!")
    print(f"📊 Key Results:")
    print(f"   Daily Active Users: {metrics['avg_dau']:.1f}")
    print(f"   Monthly Active Users: {metrics['avg_mau']:.1f}")
    print(f"   Avg Session Duration: {metrics['avg_session_duration']:.1f} minutes")
    print(f"   Churn Rate: {metrics['churn_rate']:.1%}")

    print(f"\n🎯 Feature Usage:")
    for feature, count in metrics['feature_usage'].items():
        print(f"   {feature}: {count} uses")

    print(f"\n📈 Retention Rates:")
    for period, rate in metrics['retention_rates'].items():
        print(f"   {period}: {rate:.1%}")

    print(f"\n📁 Reports saved to: {args.output}/")
    print(f"   📊 JSON: metrics.json")
    print(f"   📈 CSV: summary.csv")
    print(f"   🌐 HTML: report.html")


if __name__ == "__main__":
    main()