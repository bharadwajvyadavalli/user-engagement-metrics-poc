#!/usr/bin/env python3
"""
User Engagement Metrics POC - Main Script
"""

import argparse
import os
from data_processor import DataProcessor
from metrics_calculator import MetricsCalculator
from visualizer import Visualizer
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description='User Engagement Metrics POC')
    parser.add_argument('--input', required=True, help='Input CSV file path')
    parser.add_argument('--output', default='output', help='Output directory')
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output, exist_ok=True)
    os.makedirs(f"{args.output}/charts", exist_ok=True)
    
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
    
    # Step 3: Create visualizations
    print("📊 Creating charts...")
    visualizer = Visualizer(f"{args.output}/charts")
    charts = visualizer.create_all_charts(metrics)
    
    # Step 4: Generate report
    print("📋 Generating report...")
    reporter = ReportGenerator(args.output)
    report_file = reporter.generate_report(metrics, charts)
    
    print("\n🎉 Analysis Complete!")
    print(f"📋 Report: {report_file}")
    print(f"📊 Charts: {args.output}/charts/")
    
    # Print key findings
    print(f"\n📊 Key Findings:")
    print(f"   • Daily Active Users: {metrics['avg_dau']:.1f}")
    print(f"   • Monthly Active Users: {metrics['avg_mau']:.1f}")
    print(f"   • Avg Session Duration: {metrics['avg_session_duration']:.1f} minutes")
    print(f"   • Churn Rate: {metrics['churn_rate']:.1%}")

if __name__ == "__main__":
    main()