"""
Report Generator for User Engagement Metrics POC
"""

import os
from datetime import datetime
import pandas as pd

class ReportGenerator:
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    def generate_report(self, metrics, charts):
        """Generate HTML report"""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>User Engagement Metrics Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
                .metric-box {{ background-color: #e8f4f8; padding: 15px; margin: 10px 0; border-radius: 5px; }}
                .chart {{ text-align: center; margin: 20px 0; }}
                h1, h2 {{ color: #333; }}
                .key-metric {{ font-size: 24px; font-weight: bold; color: #0066cc; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>📊 User Engagement Metrics Report</h1>
                <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <h2>📈 Key Metrics</h2>
            
            <div class="metric-box">
                <h3>User Activity</h3>
                <p>Average Daily Active Users: <span class="key-metric">{metrics['avg_dau']:.1f}</span></p>
                <p>Average Monthly Active Users: <span class="key-metric">{metrics['avg_mau']:.1f}</span></p>
            </div>
            
            <div class="metric-box">
                <h3>Session Behavior</h3>
                <p>Average Session Duration: <span class="key-metric">{metrics['avg_session_duration']:.1f}</span> minutes</p>
                <p>Average Sessions per User: <span class="key-metric">{metrics['avg_sessions_per_user']:.1f}</span></p>
                <p>Average Queries per Session: <span class="key-metric">{metrics['avg_queries_per_session']:.1f}</span></p>
            </div>
            
            <div class="metric-box">
                <h3>User Retention</h3>
                <p>1-day Retention: <span class="key-metric">{metrics['retention_rates']['1_day']:.1%}</span></p>
                <p>7-day Retention: <span class="key-metric">{metrics['retention_rates']['7_day']:.1%}</span></p>
                <p>30-day Retention: <span class="key-metric">{metrics['retention_rates']['30_day']:.1%}</span></p>
                <p>Churn Rate: <span class="key-metric">{metrics['churn_rate']:.1%}</span></p>
            </div>
            
            <h2>🎯 Feature Usage</h2>
            <div class="metric-box">
                <ul>
        """
        
        for feature, count in metrics['feature_usage'].items():
            html += f"<li><strong>{feature.title()}:</strong> {count} uses</li>"
        
        html += f"""
                </ul>
            </div>
            
            <h2>📊 Charts</h2>
            
            <div class="chart">
                <h3>Daily/Monthly Active Users</h3>
                <img src="charts/{os.path.basename(charts['dau_mau'])}" style="max-width: 100%;">
            </div>
            
            <div class="chart">
                <h3>Session Duration Distribution</h3>
                <img src="charts/{os.path.basename(charts['session_duration'])}" style="max-width: 100%;">
            </div>
            
            <div class="chart">
                <h3>Feature Usage</h3>
                <img src="charts/{os.path.basename(charts['feature_usage'])}" style="max-width: 100%;">
            </div>
            
            <div class="chart">
                <h3>Retention Rates</h3>
                <img src="charts/{os.path.basename(charts['retention'])}" style="max-width: 100%;">
            </div>
            
            <h2>💡 Key Insights</h2>
            <div class="metric-box">
                {self._generate_insights(metrics)}
            </div>
            
        </body>
        </html>
        """
        
        # Save report
        report_file = os.path.join(self.output_dir, 'executive_summary.html')
        with open(report_file, 'w') as f:
            f.write(html)
        
        # Save CSV summary
        self._save_csv_summary(metrics)
        
        return report_file
    
    def _generate_insights(self, metrics):
        """Generate key insights"""
        insights = []
        
        # DAU/MAU ratio
        ratio = metrics['avg_dau'] / metrics['avg_mau'] if metrics['avg_mau'] > 0 else 0
        if ratio > 0.3:
            insights.append("🟢 Strong daily engagement - users are highly active")
        elif ratio > 0.15:
            insights.append("🟡 Moderate engagement - opportunity for improvement")
        else:
            insights.append("🔴 Low daily engagement - focus on user activation")
        
        # Session duration
        if metrics['avg_session_duration'] > 10:
            insights.append("🟢 Good session duration - users are engaged")
        else:
            insights.append("🔴 Short sessions - consider improving user experience")
        
        # Churn rate
        if metrics['churn_rate'] < 0.2:
            insights.append("🟢 Low churn rate - good user retention")
        elif metrics['churn_rate'] < 0.4:
            insights.append("🟡 Moderate churn - monitor user satisfaction")
        else:
            insights.append("🔴 High churn rate - urgent attention needed")
        
        return "<br>".join([f"<p>{insight}</p>" for insight in insights])
    
    def _save_csv_summary(self, metrics):
        """Save metrics summary as CSV"""
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
        
        df = pd.DataFrame(summary_data)
        csv_file = os.path.join(self.output_dir, 'metrics_summary.csv')
        df.to_csv(csv_file, index=False)