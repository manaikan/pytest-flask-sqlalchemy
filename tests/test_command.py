from flask_test.config import DATABASE_URL

def test_database_url(database_url):
    """Ensure that the database URL is consistent both within the tests and the flask application"""
    assert DATABASE_URL == database_url, "Ensure that both the flask application and the tests are working off of the same database"
