import sys
from sqlalchemy.engine.url import _parse_rfc1738_args
from sqlalchemy.exc import ArgumentError

def urlparser(url):
    try :
        _parse_rfc1738_args(url)
    except ArgumentError :
        return None
    else :
        return url

try : # A wee hack to ensure that the test database and the Flask database coincide.
    if '--database' in sys.argv and urlparser(sys.argv[sys.argv.index('--database') + 1]):
        DATABASE_URL = sys.argv[sys.argv.index('--database') + 1]
    else:
        DATABASE_URL = next((item for item in map(urlparser, sys.argv) if item))
except Exception as error :
    raise ValueError("Ensure that a valid `DATABASE_URL` is specified upon the command line when invoking flask_test or PyTest") from error

__all__ = ["DATABASE_URL"] # Hide the hack
