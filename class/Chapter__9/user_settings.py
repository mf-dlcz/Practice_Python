import json

user_settings = {
    "user_id": "12345",
    "theme": "dark",
    "notifications": {
        "email": True,
        "push": False
    },
    "default_view": "kanban",
    "custom_tags": ["work", "personal", "urgent"]
}

# Saving settings to a file
with open('user_settings.json', 'w') as file:
    json.dump(user_settings, file)


