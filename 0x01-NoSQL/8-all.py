#!/usr/bin/env python3
"""
a funtion that ist all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    funtion lists all documents in a collection
    """
    return list(mongo_collection.find())
