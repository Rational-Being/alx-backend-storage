#!/usr/bin/env python3
"""
a funtion that inserts a new doument
"""


def insert_school(mongo_collection, **kwargs):
    """
    funtion inserts a new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
