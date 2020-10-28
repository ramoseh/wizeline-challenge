# Database
from db.models import UsersTable
from db.database import SessionLocal

import time


def get_table():
    try:
        db = SessionLocal()
        table = db.query(UsersTable)
        result = [{'id': item.id, 'name': item.name, 'email': item.email,
                   'created_at': float(item.created_at)} for item in table]
        # for item in rippleTable:
        #     result[item.id] = {'last': item.last, 'high': item.high, 'low': item.low, 'volume': item.volume, 'vwap': item.vwap, 'bid': item.bid, 'ask': item.ask, 'change_24': item.change_24}
        return {'payload': result}
    except ValueError as e:
        return {'error': e}


def post_table(name, email):
    try:
        db = SessionLocal()
        item = UsersTable()
        item.name = name
        item.email = email
        item.created_at = time.time()
        db.add(item)
        db.commit()
        return {'payload': "User is stored"}
    except ValueError as e:
        return {'error': e}
