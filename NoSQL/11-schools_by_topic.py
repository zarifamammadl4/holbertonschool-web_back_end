#!/usr/bin/env python3
"""
Function that returns the list of schools having a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns list of schools having a specific topic.
    
    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for
    
    Returns:
        list: documents where topic is present in the topics array
    """
    return list(mongo_collection.find({"topics": topic}))
