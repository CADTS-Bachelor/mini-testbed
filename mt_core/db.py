# coding=UTF-8

import sqlalchemy
import sqlite3

# TODO save scene instances info into sqlite3 database use SQLAlchemy package
class Database:
    def __init__(self, url):
        self.ur = url

    def create_tables(self):
        pass