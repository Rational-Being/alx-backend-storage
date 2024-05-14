#!/usr/bin/env python3
"""
funtion returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    funtiion returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
