"""
Visualizer for User Engagement Metrics POC
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os
import config

class Visualizer:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        plt.style.use('default')
    
    def create_all_charts(self, metrics):
        """Create all visualization charts"""
        charts = {}
        
        # DAU/MAU Chart
        charts['dau_mau'] = self.plot_dau_mau(metrics)
        
        # Session Duration Chart
        charts['session_duration'] = self.plot_session_duration(metrics)
        
        # Feature Usage Chart
        charts['feature_usage'] = self.plot_feature_usage(metrics)
        
        # Retention Chart
        charts['retention'] = self.plot_retention(metrics)
        
        return charts
    
    def plot_dau_mau(self, metrics):
        """Plot DAU and MAU trends"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=config.FIGURE_SIZE)
        
        # DAU
        dau_data = metrics['dau_data']
        ax1.plot(dau_data.index, dau_data.values, marker='o', linewidth=2)
        ax1.set_title('Daily Active Users', fontweight='bold')
        ax1.set_ylabel('Users')
        ax1.grid(True, alpha=0.3)
        
        # MAU
        mau_data = metrics['mau_data']
        ax2.plot(range(len(mau_data)), mau_data.values, marker='s', linewidth=2, color='orange')
        ax2.set_title('Monthly Active Users', fontweight='bold')
        ax2.set_ylabel('Users')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        filename = os.path.join(self.output_dir, 'dau_mau.png')
        plt.savefig(filename, dpi=config.DPI, bbox_inches='tight')
        plt.close()
        return filename
    
    def plot_session_duration(self, metrics):
        """Plot session duration distribution"""
        plt.figure(figsize=config.FIGURE_SIZE)
        
        durations = metrics['session_durations']
        plt.hist(durations, bins=20, alpha=0.7, edgecolor='black')
        plt.axvline(metrics['avg_session_duration'], color='red', linestyle='--', 
                   label=f'Average: {metrics["avg_session_duration"]:.1f} min')
        
        plt.title('Session Duration Distribution', fontweight='bold')
        plt.xlabel('Duration (minutes)')
        plt.ylabel('Number of Sessions')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        filename = os.path.join(self.output_dir, 'session_duration.png')
        plt.savefig(filename, dpi=config.DPI, bbox_inches='tight')
        plt.close()
        return filename
    
    def plot_feature_usage(self, metrics):
        """Plot feature usage"""
        plt.figure(figsize=config.FIGURE_SIZE)
        
        features = list(metrics['feature_usage'].keys())
        counts = list(metrics['feature_usage'].values())
        
        plt.bar(features, counts, alpha=0.8)
        plt.title('Feature Usage Count', fontweight='bold')
        plt.xlabel('Features')
        plt.ylabel('Usage Count')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        filename = os.path.join(self.output_dir, 'feature_usage.png')
        plt.savefig(filename, dpi=config.DPI, bbox_inches='tight')
        plt.close()
        return filename
    
    def plot_retention(self, metrics):
        """Plot retention rates"""
        plt.figure(figsize=config.FIGURE_SIZE)
        
        retention_data = metrics['retention_rates']
        periods = list(retention_data.keys())
        rates = [rate * 100 for rate in retention_data.values()]
        
        plt.bar(periods, rates, alpha=0.8, color='green')
        plt.title('User Retention Rates', fontweight='bold')
        plt.xlabel('Period')
        plt.ylabel('Retention Rate (%)')
        plt.grid(True, alpha=0.3)
        
        filename = os.path.join(self.output_dir, 'retention.png')
        plt.savefig(filename, dpi=config.DPI, bbox_inches='tight')
        plt.close()
        return filename