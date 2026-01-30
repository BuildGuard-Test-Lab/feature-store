from datetime import timedelta

def get_user_features():
    """Return user features for ML model training."""
    return {
        "user_id": "entity",
        "features": [
            "total_purchases_30d",
            "avg_order_value",
            "days_since_last_login",
            "account_age_days",
        ],
        "ttl": timedelta(hours=1),
    }

def get_product_features():
    """Return product features."""
    return {
        "product_id": "entity",
        "features": [
            "category",
            "price",
            "avg_rating",
            "total_reviews",
        ],
    }
