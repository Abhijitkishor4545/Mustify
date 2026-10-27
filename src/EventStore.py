class EventStore:
    categories = {
        "Wedding": [],
        "Birthday": [],
        "Conference": []
    }

    @classmethod
    def add_category(cls, event_type, category):
        if category not in cls.categories[event_type]:
            cls.categories[event_type].append(category)

    @classmethod
    def get_categories(cls, event_type):
        return cls.categories.get(event_type, [])
