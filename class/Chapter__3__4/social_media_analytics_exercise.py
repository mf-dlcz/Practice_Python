'''
Social Media Analytics - Real World Application
In today's digital marketing industry, social media analysts and marketers work with data structures very 
similar to this exercise. Major social media provide data through their APIs (Application Programming Interfaces)
in comparable nested JSON formats.
'''
social_media_data = {
    "campaign_metrics": {
        "summer_sale_2024": {
            "posts": [
                {
                    "post_id": "P1001",
                    "platform": "A",
                    "content_type": "image",
                    "engagement": {
                        "likes": 1500,
                        "comments": 300,
                        "shares": 100,
                        "saves": 50
                    },
                    "hashtags": ["#summersale", "#fashion", "#discount"],
                    "reach": 15000,
                    "demographics": {
                        "age_groups": {
                            "18-24": 0.3,
                            "25-34": 0.4,
                            "35-44": 0.2,
                            "45+": 0.1
                        },
                        "top_locations": ["New York", "Los Angeles", "Chicago"]
                    }
                },
                {
                    "post_id": "P1002",
                    "platform": "B",
                    "content_type": "video",
                    "engagement": {
                        "likes": 2500,
                        "comments": 450,
                        "shares": 800,
                        "saves": 120
                    },
                    "hashtags": ["#summersale", "#summerfashion"],
                    "reach": 25000,
                    "demographics": {
                        "age_groups": {
                            "18-24": 0.25,
                            "25-34": 0.45,
                            "35-44": 0.20,
                            "45+": 0.10
                        },
                        "top_locations": ["Miami", "Houston", "Phoenix"]
                    }
                }
            ],
            "campaign_budget": 5000,
            "campaign_duration": 15
        }
    }
}
