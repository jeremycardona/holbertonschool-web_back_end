#!/usr/bin/env python3
"""find schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """returns a list of school by topic"""
    return mongo_collection.find({"topics": topic})