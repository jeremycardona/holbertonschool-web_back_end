#!/usr/bin/env python3
""" update school topics """


def update_topics(mongo_collection, name, topics):
    """update topics"""
    return mongo_collection.update_many({ "name": name }, { "$set": { "topics": topics } })
