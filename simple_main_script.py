#!/usr/bin/env python3
"""
Complete End-to-End User Engagement Analytics
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
    parser = argparse.ArgumentParser(description='Complete User Engagement Analytics')
    parser.add_argument('--users', type=int, default=500, help='Number of users to generate (default: 500)')
    parser.add_argument('--days', type=int, default=60, help='Number of days to simulate (default: 60)')
    parser.add_argument('--input', type=str, help='Use existing CSV file instead of generating new data')
    parser.add_argument('--output', default='output', help='Output directory (default: output)')

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    print("🚀 Starting Complete User Engagement Analytics...")

    # Step 1: Generate or load data
    if args.input:
        print(f"📂 Loading existing data from {args.input}...")
        input_file = args.input
    else:
        print(f"🎲 Generating realistic data ({args.users} users, {args.days} days)...")
        generator = DataGenerator()
        df_raw = generator.generate_data(num_users=args.users, num_days=args.days)

        input_file = f"{args.output}/generated_data.csv"
        df_raw.to_csv(input_file, index=False)
        print(f"💾 Generated data saved to {input_file}")
        print(f"✅ Created {len(df_raw)} interactions from {df_raw['User ID'].nunique()} users")

    # Step 2: Process data
    print("📊 Processing data...")
    processor = DataProcessor()
    df = processor.process_csv(input_file)
    print(f"✅ Processed {len(df)} interactions from {df['User_ID'].nunique()} users")

    # Step 3: Calculate metrics
    print("📈 Calculating engagement metrics...")
    calculator = MetricsCalculator()
    metrics = calculator.calculate_all_metrics(df)

    # Step 4: Generate outputs
    print("📋 Generating reports...")

    # Save JSON report
    json_file = f"{args.output}/metrics.json"
    with open(json_file, 'w') as f:
        json.dump(metrics, f, indent=2, default=str)

    # Save CSV summary
    summary_data = {
        'Metric': [
            'Total Users', 'Total Interactions', 'Average DAU', 'Average MAU',
            'Avg Session Duration (min)', 'Avg Sessions per User', 'Avg Queries per Session',
            '1-day Retention (%)', '7-day Retention (%)', '30-day Retention (%)', 'Churn Rate (%)'
        ],
        'Value': [
            df['User_ID'].nunique(),
            len(df),
            round(metrics['avg_dau'], 1),
            round(metrics['avg_mau'], 1),
            round(metrics['avg_session_duration'], 1),
            round(metrics['avg_sessions_per_user'], 1),
            round(metrics['avg_queries_per_session'], 1),
            round(metrics['retention_rates']['1_day'] * 100, 1),
            round(metrics['retention_rates']['7_day'] * 100, 1),
            round(metrics['retention_rates']['30_day'] * 100, 1),
            round(metrics['churn_rate'] * 100, 1)
        ]
    }
    summary_file = f"{args.output}/summary.csv"
    pd.DataFrame(summary_data).to_csv(summary_file, index=False)

    # Generate HTML report
    html_file = f"{args.output}/report.html"
    html_generator = HTMLGenerator()
    html_generator.generate_report(metrics, html_file)

    # Print results
    print("\n🎉 Analysis Complete!")
    print(f"📊 Key Results:")
    print(f"   Total Users: {df['User_ID'].nunique()}")
    print(f"   Total Interactions: {len(df)}")
    print(f"   Average Daily Active Users: {metrics['avg_dau']:.1f}")
    print(f"   Average Session Duration: {metrics['avg_session_duration']:.1f} minutes")
    print(f"   1-day Retention: {metrics['retention_rates']['1_day']:.1%}")
    print(f"   7-day Retention: {metrics['retention_rates']['7_day']:.1%}")
    print(f"   Churn Rate: {metrics['churn_rate']:.1%}")

    print(f"\n🎯 Top Features:")
    sorted_features = sorted(metrics['feature_usage'].items(), key=lambda x: x[1], reverse=True)
    for feature, count in sorted_features[:5]:
        print(f"   {feature}: {count} uses")

    print(f"\n📁 Reports Generated:")
    print(f"   📊 Metrics: {json_file}")
    print(f"   📈 Summary: {summary_file}")
    print(f"   🌐 Dashboard: {html_file}")

    if not args.input:
        print(f"   📂 Raw Data: {input_file}")


def quick_demo():
    """Run a quick demo with default settings"""
    print("🚀 Running Quick Demo...")
    print("Generating 200 users over 30 days...")

    # Generate data
    generator = DataGenerator()
    df_raw = generator.generate_data(num_users=200, num_days=30)
    df_raw.to_csv('demo_data.csv', index=False)

    # Process and analyze
    processor = DataProcessor()
    df = processor.process_csv('demo_data.csv')

    calculator = MetricsCalculator()
    metrics = calculator.calculate_all_metrics(df)

    # Quick results
    print(f"\n📊 Demo Results:")
    print(f"   Users: {df['User_ID'].nunique()}")
    print(f"   Interactions: {len(df)}")
    print(f"   Avg DAU: {metrics['avg_dau']:.1f}")
    print(f"   1-day Retention: {metrics['retention_rates']['1_day']:.1%}")
    print(f"   7-day Retention: {metrics['retention_rates']['7_day']:.1%}")

    print(f"\n📁 Demo data saved to: demo_data.csv")


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        # No arguments - run interactive mode
        print("User Engagement Analytics")
        print("1. Quick Demo (200 users, 30 days)")
        print("2. Custom Analysis")
        print("3. Process Existing File")

        choice = input("Choose option (1-3): ").strip()

        if choice == "1":
            quick_demo()
        elif choice == "2":
            users = int(input("Number of users (default 500): ") or "500")
            days = int(input("Number of days (default 60): ") or "60")

            # Run with custom parameters
            import sys

            sys.argv = ['script', '--users', str(users), '--days', str(days)]
            main()
        elif choice == "3":
            filename = input("CSV filename: ")
            if os.path.exists(filename):
                import sys

                sys.argv = ['script', '--input', filename]
                main()
            else:
                print(f"File {filename} not found")
        else:
            print("Invalid choice")
    else:
        # Command line arguments provided
        main()