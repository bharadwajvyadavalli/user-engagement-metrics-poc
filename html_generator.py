"""
Professional HTML Report Generator with Enhanced Visualizations
"""

from datetime import datetime
import json

class HTMLGenerator:
    def generate_report(self, metrics, output_path):
        """Generate a professional HTML report with charts and modern design"""

        # Prepare data for charts
        dau_dates = list(metrics['dau_data'].keys())[-30:]  # Last 30 days
        dau_values = [metrics['dau_data'][d] for d in dau_dates]

        # Feature usage data
        features = list(metrics['feature_usage'].keys())
        feature_values = list(metrics['feature_usage'].values())

        # Calculate additional insights
        total_users = len(set([k for k in metrics.get('mau_data', {}).values()]))
        total_interactions = sum(metrics['dau_data'].values()) * metrics['avg_queries_per_session']

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>User Engagement Analytics Dashboard</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0f0f23;
            color: #e0e0e0;
            line-height: 1.6;
        }}
        
        .dashboard {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        /* Header */
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            border-radius: 20px;
            padding: 3rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }}
        
        .header::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 300px;
            height: 300px;
            background: rgba(255,255,255,0.05);
            border-radius: 50%;
        }}
        
        .header h1 {{
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(to right, #fff, #e0e0e0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .header .subtitle {{
            font-size: 1.1rem;
            opacity: 0.9;
            color: #e0e0e0;
        }}
        
        /* Executive Summary */
        .executive-summary {{
            background: #1a1a2e;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid #2a2a3e;
        }}
        
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }}
        
        .summary-item {{
            text-align: center;
        }}
        
        .summary-value {{
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .summary-label {{
            color: #888;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        /* Metrics Grid */
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        
        .metric-card {{
            background: #1a1a2e;
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid #2a2a3e;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        
        .metric-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
            border-color: #667eea;
        }}
        
        .metric-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(to right, #667eea, #764ba2);
        }}
        
        .metric-header {{
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
        }}
        
        .metric-icon {{
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 1rem;
            font-size: 1.5rem;
        }}
        
        .metric-title {{
            font-size: 1.1rem;
            font-weight: 600;
            color: #e0e0e0;
        }}
        
        .metric-content {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }}
        
        .metric-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.5rem 0;
            border-bottom: 1px solid #2a2a3e;
        }}
        
        .metric-row:last-child {{
            border-bottom: none;
        }}
        
        .metric-label {{
            color: #888;
            font-size: 0.9rem;
        }}
        
        .metric-value {{
            font-size: 1.5rem;
            font-weight: 700;
            color: #667eea;
        }}
        
        /* Charts */
        .chart-container {{
            background: #1a1a2e;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid #2a2a3e;
        }}
        
        .chart-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }}
        
        .chart-title {{
            font-size: 1.3rem;
            font-weight: 600;
            color: #e0e0e0;
        }}
        
        .chart-wrapper {{
            position: relative;
            height: 300px;
        }}
        
        /* Feature Tags */
        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }}
        
        .feature-card {{
            background: #242438;
            border: 1px solid #3a3a4e;
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
            transition: all 0.3s ease;
        }}
        
        .feature-card:hover {{
            background: #2a2a3e;
            border-color: #667eea;
            transform: scale(1.05);
        }}
        
        .feature-name {{
            font-weight: 600;
            color: #e0e0e0;
            margin-bottom: 0.5rem;
            text-transform: capitalize;
        }}
        
        .feature-count {{
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .feature-label {{
            color: #888;
            font-size: 0.8rem;
        }}
        
        /* Status Indicators */
        .status {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
        }}
        
        .status-excellent {{
            background: rgba(16, 185, 129, 0.2);
            color: #10b981;
        }}
        
        .status-good {{
            background: rgba(59, 130, 246, 0.2);
            color: #3b82f6;
        }}
        
        .status-warning {{
            background: rgba(245, 158, 11, 0.2);
            color: #f59e0b;
        }}
        
        .status-poor {{
            background: rgba(239, 68, 68, 0.2);
            color: #ef4444;
        }}
        
        /* Footer */
        .footer {{
            text-align: center;
            padding: 3rem 2rem;
            color: #666;
            font-size: 0.9rem;
        }}
        
        .footer a {{
            color: #667eea;
            text-decoration: none;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .dashboard {{ padding: 1rem; }}
            .header {{ padding: 2rem; }}
            .header h1 {{ font-size: 2rem; }}
            .metrics-grid {{ grid-template-columns: 1fr; }}
        }}
        
        /* Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .metric-card, .chart-container {{
            animation: fadeIn 0.6s ease-out;
        }}
        
        /* Print Styles */
        @media print {{
            body {{ background: white; color: black; }}
            .metric-card, .chart-container {{ 
                background: white; 
                border: 1px solid #ddd;
                break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
    <div class="dashboard">
        <!-- Header -->
        <div class="header">
            <h1>User Engagement Analytics</h1>
            <p class="subtitle">Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
        
        <!-- Executive Summary -->
        <div class="executive-summary">
            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">Executive Summary</h2>
            <div class="summary-grid">
                <div class="summary-item">
                    <div class="summary-value">{int(metrics['avg_dau'])}</div>
                    <div class="summary-label">Daily Active Users</div>
                </div>
                <div class="summary-item">
                    <div class="summary-value">{metrics['retention_rates']['7_day']:.0%}</div>
                    <div class="summary-label">7-Day Retention</div>
                </div>
                <div class="summary-item">
                    <div class="summary-value">{metrics['avg_session_duration']:.1f}m</div>
                    <div class="summary-label">Avg Session Time</div>
                </div>
                <div class="summary-item">
                    <div class="summary-value">{sum(feature_values):,}</div>
                    <div class="summary-label">Total Interactions</div>
                </div>
            </div>
        </div>
        
        <!-- Metrics Cards -->
        <div class="metrics-grid">
            <!-- User Activity -->
            <div class="metric-card">
                <div class="metric-header">
                    <div class="metric-icon">👥</div>
                    <div class="metric-title">User Activity</div>
                </div>
                <div class="metric-content">
                    <div class="metric-row">
                        <span class="metric-label">Daily Active Users</span>
                        <span class="metric-value">{metrics['avg_dau']:.0f}</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Monthly Active Users</span>
                        <span class="metric-value">{metrics['avg_mau']:.0f}</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Growth Trend</span>
                        <span class="status status-{'excellent' if metrics['avg_dau'] > 100 else 'good' if metrics['avg_dau'] > 50 else 'warning'}">
                            {'Excellent' if metrics['avg_dau'] > 100 else 'Good' if metrics['avg_dau'] > 50 else 'Moderate'}
                        </span>
                    </div>
                </div>
            </div>
            
            <!-- Session Metrics -->
            <div class="metric-card">
                <div class="metric-header">
                    <div class="metric-icon">⏱️</div>
                    <div class="metric-title">Session Analytics</div>
                </div>
                <div class="metric-content">
                    <div class="metric-row">
                        <span class="metric-label">Avg Duration</span>
                        <span class="metric-value">{metrics['avg_session_duration']:.1f}m</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Sessions per User</span>
                        <span class="metric-value">{metrics['avg_sessions_per_user']:.1f}</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Queries per Session</span>
                        <span class="metric-value">{metrics['avg_queries_per_session']:.1f}</span>
                    </div>
                </div>
            </div>
            
            <!-- Retention & Health -->
            <div class="metric-card">
                <div class="metric-header">
                    <div class="metric-icon">📈</div>
                    <div class="metric-title">Retention & Health</div>
                </div>
                <div class="metric-content">
                    <div class="metric-row">
                        <span class="metric-label">1-Day Retention</span>
                        <span class="metric-value">{metrics['retention_rates']['1_day']:.0%}</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">7-Day Retention</span>
                        <span class="metric-value">{metrics['retention_rates']['7_day']:.0%}</span>
                    </div>
                    <div class="metric-row">
                        <span class="metric-label">Churn Rate</span>
                        <span class="status status-{'excellent' if metrics['churn_rate'] < 0.1 else 'good' if metrics['churn_rate'] < 0.3 else 'warning'}">
                            {metrics['churn_rate']:.0%}
                        </span>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Daily Active Users Chart -->
        <div class="chart-container">
            <div class="chart-header">
                <h3 class="chart-title">Daily Active Users Trend (Last 30 Days)</h3>
            </div>
            <div class="chart-wrapper">
                <canvas id="dauChart"></canvas>
            </div>
        </div>
        
        <!-- Feature Usage -->
        <div class="chart-container">
            <div class="chart-header">
                <h3 class="chart-title">Feature Usage Analytics</h3>
            </div>
            <div class="features-grid">
                {self._generate_feature_cards(metrics['feature_usage'])}
            </div>
            <div class="chart-wrapper" style="margin-top: 2rem;">
                <canvas id="featureChart"></canvas>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <p>Powered by User Engagement Analytics Platform • {datetime.now().year}</p>
        </div>
    </div>
    
    <script>
        // Chart.js configuration
        Chart.defaults.color = '#888';
        Chart.defaults.borderColor = '#2a2a3e';
        
        // Daily Active Users Chart
        const dauCtx = document.getElementById('dauChart').getContext('2d');
        new Chart(dauCtx, {{
            type: 'line',
            data: {{
                labels: {json.dumps(dau_dates)},
                datasets: [{{
                    label: 'Daily Active Users',
                    data: {json.dumps(dau_values)},
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    borderWidth: 3,
                    pointRadius: 5,
                    pointBackgroundColor: '#667eea',
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2,
                    tension: 0.4,
                    fill: true
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }},
                    tooltip: {{
                        backgroundColor: '#1a1a2e',
                        titleColor: '#e0e0e0',
                        bodyColor: '#e0e0e0',
                        borderColor: '#667eea',
                        borderWidth: 1,
                        cornerRadius: 8,
                        displayColors: false
                    }}
                }},
                scales: {{
                    x: {{
                        grid: {{ color: '#2a2a3e' }},
                        ticks: {{ maxRotation: 45, minRotation: 45 }}
                    }},
                    y: {{
                        grid: {{ color: '#2a2a3e' }},
                        beginAtZero: true
                    }}
                }}
            }}
        }});
        
        // Feature Usage Chart
        const featureCtx = document.getElementById('featureChart').getContext('2d');
        new Chart(featureCtx, {{
            type: 'bar',
            data: {{
                labels: {json.dumps([f.title() for f in features])},
                datasets: [{{
                    label: 'Usage Count',
                    data: {json.dumps(feature_values)},
                    backgroundColor: [
                        'rgba(102, 126, 234, 0.8)',
                        'rgba(118, 75, 162, 0.8)',
                        'rgba(129, 140, 248, 0.8)',
                        'rgba(139, 92, 246, 0.8)',
                        'rgba(124, 58, 237, 0.8)'
                    ],
                    borderWidth: 0,
                    borderRadius: 8
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }},
                    tooltip: {{
                        backgroundColor: '#1a1a2e',
                        titleColor: '#e0e0e0',
                        bodyColor: '#e0e0e0',
                        borderColor: '#667eea',
                        borderWidth: 1,
                        cornerRadius: 8
                    }}
                }},
                scales: {{
                    x: {{ grid: {{ display: false }} }},
                    y: {{
                        grid: {{ color: '#2a2a3e' }},
                        beginAtZero: true
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

        # Save HTML file
        with open(output_path, 'w') as f:
            f.write(html)

        return output_path

    def _generate_feature_cards(self, feature_usage):
        """Generate feature cards HTML"""
        cards = []
        for feature, count in sorted(feature_usage.items(), key=lambda x: x[1], reverse=True):
            cards.append(f"""
                <div class="feature-card">
                    <div class="feature-name">{feature}</div>
                    <div class="feature-count">{count:,}</div>
                    <div class="feature-label">interactions</div>
                </div>
            """)
        return ''.join(cards)