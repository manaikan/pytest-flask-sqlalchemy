import csv
import json
import pytest
from collections import OrderedDict
from pathlib import Path
from flask import request, url_for
from flask_sandman import Model
from pytest_flask.fixtures import client
from phonetic.models import NATO # The path is modified to include SQLTest

with open(Path(__file__).parent/"nato.txt", "rt") as file:
    # nato = list({"id":int(item["id"]),"letter":item["letter"]} for item in csv.DictReader(file))
    cast = {"id" : int}
    nato = list(map(lambda item : OrderedDict((key, cast[key](val) if key in cast else val) for key, val in item.items()), csv.DictReader(file)))

def test_Consistency(client):
    """This tests that the alphabet on file and the one in the database are consistent"""
    response = client.get(url_for("nato"), content_type="application/json")
    answer = nato
    result = response.json
    assert answer == result

@pytest.mark.parametrize("id,name", [item.values() for item in nato])
def test_ORM_vs_API_review(id,name,client, db_session):
    """Iterate over the records in a table and ensure that those retrieved via API are equivalent to those obtained via SQLAlchemy"""
    # Test ORM Response
    record = db_session.query(NATO).get(id)
    answer = name
    result = record.letter
    assert answer == result
    # Test API Response
    response = client.get(url_for("nato", resource_id=id))
    answer = name
    result = response.json["letter"]
    assert answer == result
    # Note : One also has access to the request object within Flask e.g. request.path.split('/') == ["nato","1"]

@pytest.mark.parametrize("id,letter", [item.values() for item in nato])
def test_ORM_with_ORM_update(id,letter,client, db_session):
    """Iterate over the records in a table and ensure that those retrieved via API are equivalent to those obtained via SQLAlchemy"""
    # Test Database Response
    record = db_session.query(NATO).get(id)
    answer = letter
    result = record.letter
    assert result == answer
    # Test Update
    record.letter = record.letter.upper()
    db_session.add(record)
    # record.name = record.update({"name":name.upper()})
    db_session.commit()
    # Test Database Response
    record = db_session.query(NATO).get(id)
    answer = letter.upper()
    result = record.letter
    assert result == answer

@pytest.mark.parametrize("id,letter", [item.values() for item in nato[:3]])
def test_API_with_API_update(id,letter,client, db_session):
    """Iterate over the records in a table and ensure that those retrieved via API are equivalent to those obtained via SQLAlchemy"""
    # Test Database Response
    response = client.get(url_for("nato", resource_id=id), content_type="application/json")
    answer = letter
    result = response.json["letter"]
    assert result == answer
    # Test Update
    # response = client.post(url_for("nato"), data = json.dumps({"id":id, "letter":letter.upper()}), content_type="application/json")
    # assert response.code == 200 # not in (405 - Invalid method, 204 - No Content)
    response = client.put(url_for("nato", resource_id=id), data=json.dumps({"id":id, "letter":letter.upper()}), headers={'Content-type': 'application/json'})
    assert response.status_code == 200
    # assert json.loads(response.get_data(as_text=True)) == NEW_ALBUM
    # Test Database Response
    response = client.get(url_for("nato", resource_id=id), content_type="application/json")
    answer = letter.upper()
    result = response.json["letter"]
    assert result == answer

# @pytest.mark.parametrize("id,name", [(1,"Alpha     "), (2,"Bravo     "), (3, "Charlie   ")])
# def test_API_with_API_update(id,name,client, db_session):
#     """Iterate over the records in a table and ensure that those retrieved via API are equivalent to those obtained via SQLAlchemy"""
#
#     # Test API Response
#     response = client.get(url_for("nato", resource_id=id))
#     answer = name
#     result = response.json["letter"]
#     assert result == answer
#
#     # Test ORM Response
#     # record = db_session.query(NATO).get(id)
#     # answer = name
#     # result = record.name
#     # assert result == answer
#
#     # Test Database Request
#     record = db_session.query(NATO).get(id)
#     record.name = name.upper()
#     db_session.add(record)
#     db_session.commit()
#
#     # Test API Response - This times out without reason
#     # response = client.get(url_for("name", resource_id=id))
#     # answer = name.upper()
#     # result = response.json["name"]
#     # assert result == answer
#
#     # Test ORM Response
#     # record = db_session.query(NATO).get(id)
#     # answer = name.upper()
#     # result = record.name
#     # assert result == answer
#
# @pytest.mark.parametrize("id,letter", [(1,"Alpha     "), (2,"Bravo     "), (3, "Charlie   ")])
# def test_orm_with_api_update(id,letter,client, db_session):
#     """Iterate over the records in a table and ensure that those retrieved via API are equivalent to those obtained via SQLAlchemy"""
#     # Test Database Response
#     record = db_session.query(NATO).get(id)
#     answer = letter
#     result = record.letter
#     assert result == answer
#     # Test Endpoint
#     payload = {"id":id,"name":letter.upper()}
#     response = client.post(url_for("nato"), data = json.dumps(payload), content_type='application/json')
#     # Test Endpoint Request
#     answer = payload
#     result = request.json
#     assert result == answer
#     # Test Endpoint Response
#     record = db_session.query(NATO).get(id)
#     answer = letter.upper()
#     result = record.letter
#     assert result == answer
#
# @pytest.mark.parametrize("id,letter", [(1,"Alpha     "), (2,"Bravo     "), (3, "Charlie   ")])
# def test_api_with_orm_update(id,letter,client, db_session):
#     """Iterate over the records in a table and ensure that those retrieved via API are equivalent to those obtained via SQLAlchemy"""
#
#     # Test API Response
#     response = client.get(url_for("nato", resource_id=id))
#     answer = letter
#     result = response.json["letter"]
#     assert result == answer
#
#     # Test ORM Response
#     # record = db_session.query(NATO).get(id)
#     # answer = name
#     # result = record.name
#     # assert result == answer
#
#     # Test Database Request
#     record = db_session.query(NATO).get(id)
#     record.name = letter.upper()
#     db_session.add(record)
#     db_session.commit()
#
#     # Test API Response - This times out without reason
#     # response = client.get(url_for("name", resource_id=id))
#     # answer = name.upper()
#     # result = response.json["name"]
#     # assert result == answer
#
#     # Test ORM Response
#     # record = db_session.query(NATO).get(id)
#     # answer = name.upper()
#     # result = record.name
#     # assert result == answer
