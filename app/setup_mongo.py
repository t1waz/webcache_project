from pymongo import (
    MongoClient,
    ASCENDING
)

import settings


if __name__ == '__main__':
    mongo_client = MongoClient(**settings.MONGO_SETTINGS)

    db = mongo_client.webdata
    db.webpages.create_index([('urlKey', ASCENDING)], unique=True)
    db.webpages.create_index([('creationDate', ASCENDING)])

    mongo_client.close()

