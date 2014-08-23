# -*- coding: utf-8 -*-


class BaseModel(object):
    """ Abstract class for model """

    db_collection = None

    def connect_database(self):
        pass

    @property
    def collection(self):
        db = self.connect_database()
        return getattr(db, self.db_collection)

    def save(self):
        data = self.to_mongo()
