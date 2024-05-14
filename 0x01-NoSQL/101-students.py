#!/usr/bin/env python3
"""
function returns all students sorted by score
"""


def top_students(mongo_collection):
    """
    funtion returns all students sorted byaverage score
    """
    return mongo_collection.aggregate(
        [
            {"$project":
                {"name": "$name",
                "averageScore": {"$avg": "$topics.score"}
                }
            },
            {"$sort": {"avarageScore": -1}},
        ]
    )
