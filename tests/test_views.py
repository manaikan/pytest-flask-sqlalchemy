import pytest
from flask import url_for
from flask_test.models import Table

@pytest.fixture()
def session(db_session):
    data = [{"id":0, "name":"test"},]
    # If using an engine
    # db_engine.execute(Table.insert(), data)
    # If using a session
    # db_session.execute(Table.insert().va;ues(name="test"))
    for datum in data :
        table = Table(**datum)
        db_session.add(table)
        db_session.commit()
    return data

# def test_FUNCTION(client, session):
#     client.post(/some/path/, data={"name":"testing"})
#     record = session.query(Table).get(1)
#     assert record.name == "testing"

# def test_get(client):
#     url_path = url_for("table")
#     assert url_path == "/table/"
#     response = client.get(url_path)
#     assert response.status_code == 200
#     assert response.json == []

def test_get_all(client, session):
    url_path = url_for("table")
    assert url_path == "/table/"
    response = client.get("/table/")
    assert response.status_code == 200
    # assert response.json == [{"id":1, "name":"test"}]
    # assert response.json["name"] == "test"
    # record = session.query(Table).get(1)
    # assert record.name == "testing"