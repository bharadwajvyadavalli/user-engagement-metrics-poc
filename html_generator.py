"""
Simple HTML Report Generator
"""

from datetime import datetime


class HTMLGenerator:
    def generate_report(self, metrics, output_path):
        """Generate a simple HTML report"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>User Engagement Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 30px; }}
        .metric-card {{ background: #fff; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px; }}
        .metric-value {{ font-size: 24px; font-weight: bold; color: #007bff; }}
        .feature-item {{ display: inline-block; background: #e9ecef; padding: 8px 12px; margin: 5px; border-radius: 4px; }}
        h1 {{ color: #333; margin: 0; }}
        h2 {{ color: #666; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 User Engagement Report</h1>
        <p>Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}</p>
    </div>

    <h2>Key Metrics</h2>
    <div class="grid">
        <div class="metric-card">
            <h3>👥 User Activity</h3>
            <p>Daily Active Users: <span class="metric-value">{metrics['avg_dau']:.1f}</span></p>
            <p>Monthly Active Users: <span class="metric-value">{metrics['avg_mau']:.1f}</span></p>
        </div>

        <div class="metric-card">
            <h3>⏱️ Session Metrics</h3>
            <p>Avg Duration: <span class="metric-value">{metrics['avg_session_duration']:.1f}</span> min</p>
            <p>Sessions per User: <span class="metric-value">{metrics['avg_sessions_per_user']:.1f}</span></p>
            <p>Queries per Session: <span class="metric-value">{metrics['avg_queries_per_session']:.1f}</span></p>
        </div>

        <div class="metric-card">
            <h3>📈 Retention & Churn</h3>
            <p>1-day Retention: <span class="metric-value">{metrics['retention_rates']['1_day']:.1%}</span></p>
            <p>7-day Retention: <span class="metric-value">{metrics['retention_rates']['7_day']:.1%}</span></p>
            <p>Churn Rate: <span class="metric-value">{metrics['churn_rate']:.1%}</span></p>
        </div>
    </div>

    <h2>🎯 Feature Usage</h2>
    <div class="metric-card">
        <div>
"""

        # Add feature usage
        for feature, count in metrics['feature_usage'].items():
            html += f'<span class="feature-item"><strong>{feature}:</strong> {count} uses</span>'

        html += f"""
        </div>
    </div>

    <h2>📊 Daily Activity</h2>
    <div class="metric-card">
        <table style="width: 100%; border-collapse: collapse;">
            <tr style="background: #f8f9fa;">
                <th style="padding: 10px; border: 1px solid #ddd;">Date</th>
                <th style="padding: 10px; border: 1px solid #ddd;">Active Users</th>
            </tr>
"""

        # Add daily activity table
        for date, users in metrics['dau_data'].items():
            html += f"""
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;">{date}</td>
                <td style="padding: 10px; border: 1px solid #ddd; text-align: center;">{users}</td>
            </tr>
"""

        html += """
        </table>
    </div>

    <div style="margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 5px; text-align: center;">
        <p><strong>🚀 User Engagement Analytics</strong> - Simple and effective engagement insights</p>
    </div>
</body>
</html>
"""

        # Save HTML file
        with open(output_path, 'w') as f:
            f.write(html)

        return output_path