import pytest
from flask_test.models import Table


@pytest.fixture()
def session(db_session):
    db_session.add(Table(id=1, name="test"))
    db_session.commit() # This triggers an error
    return db_session


def test_tables(session) :
    assert session.query(Table).count() == 1, "Confirm the number of records"


def test_set_name(session) :
    """Ensure that a value set within a test persists for it's operation"""
    row = session.query(Table).get(1) # Table.query.all()/Table.query.get(1)
    row.set_name('testing')
    assert row.name == 'testing', "Confirm the update of a value in a record"


def test_persistence(session) :
    """Ensure that a value set in another test does not persist to the next one"""
    record = session.query(Table).get(1)
    assert record.name == 'test', "Confirm the initial value of a record"
