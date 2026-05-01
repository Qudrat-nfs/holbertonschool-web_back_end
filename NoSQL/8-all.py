#!/usr/bin/env python3
"""
Module for task 8: list all documents.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    Args:
        mongo_collection: PyMongo collection object.
    Returns:
        List of all documents, or an empty list if there are no documents.
    """
    return list(mongo_collection.find())


if __name__ == "__main__":
    pass
