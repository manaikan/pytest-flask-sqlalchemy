import pytest
from flask_test.manage import create, delete
import flask
import flask_sqlalchemy


def pytest_addoption(parser):
    """Adds the command line option `--database`

    This value is used to set the database URL used in testing PyTest-Flask_SQLAlchemy against the respective database"""
    parser.addoption("--database",
                     action="store",
                     help="Database URL, `DATABASE+PROTOCOL://USERNAME:PASSWORD@DOMAIN:PORT/DATASTORE`, for the database one is testing against",
                     default = None) # Setting a default, ``default="sqlite+pysqlite:///test.sqlite3"``, has no effect since setting flask_test.config:DATABASE_URL will fail if `--database DATABASE_URL` is not present in the command line invocation


def pytest_generate_tests(metafunc):
    """Ensures that users have set a database URL"""
    database = metafunc.config.option.database # Alternatively : metafunc.config.getoption("database_url", "sqlite+pysqlite:///test.sqlite3")
    if "database_url" in metafunc.fixturenames and database is not None :
        metafunc.parametrize("database_url", [database], scope="session")


@pytest.fixture(scope='session')
def database(request, database_url):
    """Creates a database before all of the tests are executed"""
    # restore(DATAFILE, DABA_URL)

    yield database_url

    @request.addfinalizer
    def drop_database():
        """Removes the database once all of the tests have completed"""
        # drop_postgresql_database(pg_user, pg_host, pg_port, pg_db, 9.6)
        # delete(DABA_URL)


@pytest.fixture(scope='session')
def app(database):
    """Create a Flask app context for the tests."""
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database
    return app


@pytest.fixture(scope='session')
def _db(app):
    '''
    Provide the transactional fixtures with access to the database via a Flask-SQLAlchemy
    database connection.
    '''
    db = flask_sqlalchemy.SQLAlchemy(app=app)

    return db

