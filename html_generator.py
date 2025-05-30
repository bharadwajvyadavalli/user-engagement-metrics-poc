"""
Professional HTML Report Generator
"""

from datetime import datetime

class HTMLGenerator:
    def generate_report(self, metrics, output_path):
        """Generate a professional HTML report"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>User Engagement Dashboard</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f7fa; color: #2c3e50; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                   color: white; padding: 40px; border-radius: 12px; margin-bottom: 30px; 
                   box-shadow: 0 8px 32px rgba(0,0,0,0.1); }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .header p {{ opacity: 0.9; font-size: 1.1em; }}
        
        .metrics-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
                        gap: 25px; margin-bottom: 40px; }}
        
        .metric-card {{ background: white; border-radius: 12px; padding: 25px; 
                       box-shadow: 0 4px 20px rgba(0,0,0,0.08); border: 1px solid #e3e8ee;
                       transition: transform 0.2s ease; }}
        .metric-card:hover {{ transform: translateY(-2px); }}
        
        .card-header {{ display: flex; align-items: center; margin-bottom: 20px; }}
        .card-icon {{ font-size: 1.5em; margin-right: 10px; }}
        .card-title {{ font-size: 1.2em; font-weight: 600; color: #2c3e50; }}
        
        .metric-value {{ font-size: 2.2em; font-weight: bold; color: #3498db; margin: 10px 0; }}
        .metric-label {{ color: #7f8c8d; font-size: 0.9em; margin-bottom: 8px; }}
        .metric-item {{ display: flex; justify-content: space-between; padding: 8px 0; 
                       border-bottom: 1px solid #ecf0f1; }}
        .metric-item:last-child {{ border-bottom: none; }}
        
        .features-section {{ background: white; border-radius: 12px; padding: 25px; 
                            box-shadow: 0 4px 20px rgba(0,0,0,0.08); margin-bottom: 30px; }}
        .feature-tags {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 15px; }}
        .feature-tag {{ background: #e8f4f8; color: #2c3e50; padding: 8px 16px; 
                       border-radius: 20px; font-weight: 500; border: 1px solid #bee5eb; }}
        
        .activity-table {{ background: white; border-radius: 12px; padding: 25px; 
                          box-shadow: 0 4px 20px rgba(0,0,0,0.08); }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
        th {{ background: #f8f9fa; padding: 15px; text-align: left; font-weight: 600; 
             border-bottom: 2px solid #dee2e6; }}
        td {{ padding: 12px 15px; border-bottom: 1px solid #f1f3f4; }}
        tr:hover {{ background: #f8f9fa; }}
        
        .footer {{ text-align: center; margin-top: 40px; padding: 20px; 
                  background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }}
        .footer p {{ color: #7f8c8d; }}
        
        .success {{ color: #27ae60; }}
        .warning {{ color: #f39c12; }}
        .danger {{ color: #e74c3c; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 User Engagement Dashboard</h1>
            <p>Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
        
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="card-header">
                    <span class="card-icon">👥</span>
                    <span class="card-title">User Activity</span>
                </div>
                <div class="metric-item">
                    <span class="metric-label">Daily Active Users</span>
                    <span class="metric-value">{metrics['avg_dau']:.1f}</span>
                </div>
                <div class="metric-item">
                    <span class="metric-label">Monthly Active Users</span>
                    <span class="metric-value">{metrics['avg_mau']:.1f}</span>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="card-header">
                    <span class="card-icon">⏱️</span>
                    <span class="card-title">Session Metrics</span>
                </div>
                <div class="metric-item">
                    <span class="metric-label">Avg Duration</span>
                    <span class="metric-value">{metrics['avg_session_duration']:.1f}<small style="font-size:0.5em"> min</small></span>
                </div>
                <div class="metric-item">
                    <span class="metric-label">Sessions per User</span>
                    <span class="metric-value">{metrics['avg_sessions_per_user']:.1f}</span>
                </div>
                <div class="metric-item">
                    <span class="metric-label">Queries per Session</span>
                    <span class="metric-value">{metrics['avg_queries_per_session']:.1f}</span>
                </div>
            </div>
            
            <div class="metric-card">
                <div class="card-header">
                    <span class="card-icon">📈</span>
                    <span class="card-title">Retention & Health</span>
                </div>
                <div class="metric-item">
                    <span class="metric-label">1-day Retention</span>
                    <span class="metric-value {'success' if metrics['retention_rates']['1_day'] > 0.3 else 'warning' if metrics['retention_rates']['1_day'] > 0.15 else 'danger'}">{metrics['retention_rates']['1_day']:.0%}</span>
                </div>
                <div class="metric-item">
                    <span class="metric-label">7-day Retention</span>
                    <span class="metric-value {'success' if metrics['retention_rates']['7_day'] > 0.3 else 'warning' if metrics['retention_rates']['7_day'] > 0.15 else 'danger'}">{metrics['retention_rates']['7_day']:.0%}</span>
                </div>
                <div class="metric-item">
                    <span class="metric-label">Churn Rate</span>
                    <span class="metric-value {'success' if metrics['churn_rate'] < 0.2 else 'warning' if metrics['churn_rate'] < 0.4 else 'danger'}">{metrics['churn_rate']:.0%}</span>
                </div>
            </div>
        </div>
        
        <div class="features-section">
            <div class="card-header">
                <span class="card-icon">🎯</span>
                <span class="card-title">Feature Usage Analytics</span>
            </div>
            <div class="feature-tags">
"""

        # Add feature usage tags
        for feature, count in sorted(metrics['feature_usage'].items(), key=lambda x: x[1], reverse=True):
            html += f'<div class="feature-tag"><strong>{feature.title()}</strong> • {count} uses</div>'

        html += f"""
            </div>
        </div>
        
        <div class="activity-table">
            <div class="card-header">
                <span class="card-icon">📊</span>
                <span class="card-title">Daily User Activity</span>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Active Users</th>
                        <th>Activity Level</th>
                    </tr>
                </thead>
                <tbody>
"""

        # Add daily activity with visual indicators
        max_users = max(metrics['dau_data'].values()) if metrics['dau_data'] else 1
        for date, users in sorted(metrics['dau_data'].items()):
            percentage = (users / max_users) * 100
            level = "High" if percentage > 80 else "Medium" if percentage > 40 else "Low"
            level_class = "success" if percentage > 80 else "warning" if percentage > 40 else "danger"

            html += f"""
                    <tr>
                        <td><strong>{date}</strong></td>
                        <td>{users}</td>
                        <td><span class="{level_class}">{level}</span></td>
                    </tr>
"""

        html += """
                </tbody>
            </table>
        </div>
        
        <div class="footer">
            <p><strong>🚀 User Engagement Analytics</strong> • Professional insights for data-driven decisions</p>
        </div>
    </div>
</body>
</html>
"""

        # Save HTML file
        with open(output_path, 'w') as f:
            f.write(html)

        return output_path