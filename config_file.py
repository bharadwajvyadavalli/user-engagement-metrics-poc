# Configuration for User Engagement Metrics POC

# Retention periods to analyze (days)
RETENTION_PERIODS = [1, 7, 30]

# Days of inactivity to consider user churned
CHURN_THRESHOLD_DAYS = 30

# Keywords to identify feature usage
FEATURE_KEYWORDS = {
    "search": ["search", "find", "lookup"],
    "analysis": ["analyze", "analysis", "report"], 
    "export": ["export", "download", "save"],
    "chat": ["chat", "conversation", "talk"],
    "help": ["help", "support", "assistance"]
}

# Chart settings
FIGURE_SIZE = (12, 8)
DPI = 150