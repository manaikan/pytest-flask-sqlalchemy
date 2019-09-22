import pytest
from flask_test.models import Table


@pytest.fixture()
def records(db_session):
    db_session.add(Table(id=0, name="test"))
    db_session.commit() # This triggers an error


def test_tables(db_session, records) :
    assert db_session.query(Table).count() == 1, "Confirm the number of records"


def test_set_name(session):
    row = session.query(Table).get(1)
    row.set_name('testing')
    assert row.name == 'testing', "Confirm the update of a value in a record"


def test_transaction_doesnt_persist(session):
   row = session.query(Table).get(1)
   assert row.name != 'test', "Confirm the initial value of a record"
