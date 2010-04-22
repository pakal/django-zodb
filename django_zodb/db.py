# -*- coding: utf-8 -*-
#
# django-zodb - using Django and ZODB together
#
# Copyright (c) 2009, Triveos Tecnologia Ltda.
# See COPYING for license
#

from django_zodb.config import get_configuration_from_uri
from django_zodb.storage import get_storage

from ZODB.DB import DB


class Database(object):
    def __init__(self, zodb_db):
        self.zodb_db = zodb_db


def get_database_from_uri(uri):
    config = get_configuration_from_uri(uri)
    storage = get_storage(config.storage_settings)
    zodb_db = DB(storage, config.db_settings)
    return Database(zodb_db)

def open_database(database, test=False):
    pass # TODO



# Recycle Bin
# ===========
#
# from threading import local
#
# import ZODB
# import ZODB.config
# import transaction
#
#
# __all__ = ('db',)
#
# class ZODBConnection(local):
#     def __init__(self, config): #pylint:disable-msg=W0231
#         self._db = None
#         self._connection = None
#         self._root = None
#         self._commit = True
#
#     def open(self):
#         self._db = ZODB.config.databaseFromURL(settings.ZODB_CONFIG_URL)
#         self._connection = self._db.open()
#         self._root = self._connection.root()
#
#     def close(self):
#         self.rollback()
#
#         self._root = None
#
#         self._connection.close()
#         self._connection = None
#
#         self._db.close()
#         self._db = None
#
#     @property
#     def root(self):
#         if not self._root:
#             self.open()
#         return self._root
#
#     def rollback(self, *args, **kw):
#         return transaction.abort(*args, **kw)
#
#     def commit(self, *args, **kw):
#         if self._commit:
#             return transaction.commit(*args, **kw)
#
#     def disable_commit(self):
#         self._commit = False
#
#     def enable_commit(self):
#         self._commit = True
#
#     def zap(self, confirm):
#         if confirm != "Yes, I know what I'm doing.":
#             return
#
#         for key in list(self.root):
#             del self.root[key]
#
#         transaction.commit()
#         self._db.pack()
#
# db = ZODBConnection(settings.ZODB_CONFIG_URL)