"""

There are two packages catering for pytest database fixtures.

`SQLAlchemy-PyTest-Fixtures <https://pypi.org/project/sqlalchemy-pytest-fixtures/>`_
    This provides a single module with the same name that one imports
`PyTest-Flask-SQLAlchemy <hhttps://pypi.org/project/pytest-flask-sqlalchemy/>`_
    This is a more concrete package.
"""
# import os
# import sys
# root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print("="*50, "\n", root, "\n", "="*50)
# sys.path.insert(0, os.sep.join(root, "examples", "phonetic"))
import pytest
from phonetic import create_app
from phonetic.models import NATO

DABANAME = "Phonetic"
DABATYPE = "mssql"
PROTOCOL = "pymssql"
USERNAME = "sa"
PASSWORD = "cvd"
HOSTNAME = "DESKTOP-1AN9JVP"
HOSTPORT = ""
DABAHOST = f"{HOSTNAME}:{HOSTPORT}" if HOSTPORT else f"{HOSTNAME}"
DABA_URL = f"{DABATYPE}+{PROTOCOL}://{USERNAME}:{PASSWORD}@{DABAHOST}/{DABANAME}" # mssql+pymssql://sa:cvd@DESKTOP-1AN9JVP/PSPDB1

@pytest.yield_fixture()
def application():
    """Provides the Flask application as reated by :meth:`create_app`"""
    # yield create_app(DABA_URL)
    application = create_app(DABA_URL, include_models=[NATO], read_only=False)
    from pprint import pprint
    pprint(application.url_map)
    yield application

@pytest.yield_fixture()
def app(application):
    """PyTest-Flask requires the fixture 'app' rather then 'application'"""
    # Note : This negates the need for the client and content fixtures below
    yield application

@pytest.yield_fixture()
def context(application):
    context = application.app_context()
    context.push()
    yield application
    context.pop()

# @pytest.yield_fixture()
# def client(application):
#     yield application.test_client()

# @pytest.fixture()
# def database():

# @pytest.fixture()
# def session():

@pytest.yield_fixture()
def database(context):
    """Exposes the applications database"""
    yield context.database

@pytest.yield_fixture()
def _db(database):
    """PyTest-Flask-SQLAlchemy requires the fixture '_db' rather then 'database'"""
    yield database

# What follows serves for documentation for the interim


    # ## Application
    # app = Flask(__package__, instance_relative_config=instance_relative_config)
    # # app = FlaskAPI(__package__)
    # ## Configuration
    # # - Configuration files
    # # configuration(app, config or os.environ.get("AIRPORT_CONFIGURATION", "config.cfg"), **kvps)
    # configuration(app, config or os.environ.get("FLASK_CONFIGURATION", "config.cfg"), **kvps)
    # # - Database
    # # if database_uri:
    # app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('SQLALCHEMY_DATABASE_URI', database_uri)
    # # - JWT
    # # app.config['JWT_AUTH_URL_RULE'] = '/login' # Changes the Authentication URL for Flask-JWT
    # # app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
    # # app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
    # # - JWT-Extended
    # # app.config['JWT_SECRET_KEY'] = f"{secrets.token_METHOD(64)}"
    # # - Sandman
    # app.config["APP_TYPE"] = type(app) # TODO : Rename this to FLASK_ENGINE or FLASK_APPLICATION
    # # Creates an application instance folder
    # if instance_relative_config :
    #     try:
    #         Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    #     except OSError:
    #         pass
    # ## Extentions
    # from .views import AUTHENTICATION
    # from .database import DATABASE
    # from .navigation import NAVIGATION
    # from .admin import administration, AdminView
    # # from flask_sandman.exception import register as register_exceptions
    # # from flask_sandman.api import register_entities, register_model_views, register_admin_views, register_root
    # # from .api import register as register_endpoints
    # from flask_sandman import sandman
    # # Database
    # app.database = DATABASE
    # app.database.init_app(app)
    # # Security
    # # Authentication
    # app.authentication = AUTHENTICATION
    # app.authentication.init_app(app)
    # # JWT
    # # jwt = JWT(app, authenticate, identify) # Deprecated in favour of JWTManager from JWT extended
    # # JWT-Extended
    # jwt = JWTManager(app)
    # # Navigation
    # app.navigation = NAVIGATION
    # app.navigation.init_app(app)
    # # Administration
    # app.administration = administration(app)
    # # Blue print
    # bpt = Blueprint('sandman', __package__, template_folder='templates', url_prefix=f"/{(url_prefix or '').strip('/')}")
    # # web = Blueprint('website', __package__, template_folder='templates', url_prefix=f"/{(url_prefix or '').strip('/')}")
    # # RESTful
    # api = Api(bpt) #, prefix=f"/{(url_prefix or '').strip('/')}"# Doubles up as a blue print
    # # Sandman
    # sdm = sandman(app, app.database, bpt, exclude_tables=exclude_tables, include_models=include_models, admin = app.administration, admin_view = AdminView, read_only=True)
    # # API
    # register_views(app)
    # register_endpoints(api)
    # # Models
    # app.register_blueprint(bpt, url_prefix=f"/{(url_prefix or '').strip('/')}")
    # @app.shell_context_processor
    # def shell_context():
    #     return {'app': app, 'db': database, 'api' : api, 'jwt' : jwt} # , "sandman" : sandman
    # return app
    # ## Sandman
    # register_exceptions(application)
    # # Router
    # router = blueprint or application
    # # app = app or current_app
    # # api = api or app
    # with application.app_context():
    #     # Database Tables
    #     router.included_models, router.excluded_models = register_entities(database, include_models, exclude_tables, read_only, schema=schema)
    #     # router.models = router.included_models + router.excluded_models # Mostly used for development
    #     router.model_views = []
    #     router.admin_views = []
    #     for model in router.included_models:
    #         # Model Views
    #         router.model_views.append(register_model_view(router, model))
    #         # Admin Views
    #         if admin:
    #             router.admin_views.append(register_admin_view(admin, model, view = admin_view))
    #     # API Index
    #     if root: register_index(router, root)
    # return router
