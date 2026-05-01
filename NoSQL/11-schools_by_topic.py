#!/usr/bin/env python3
"""
Module for task 11: Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of documents (schools) that include the topic.
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    pass
