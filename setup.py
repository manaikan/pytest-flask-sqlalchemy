from setuptools import setup

project = 'pytest-flask-sqlalchemy'
release = '1.0.2'
version = '.'.join(release.split('.')[:-1])

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name=project,
    author='Jean Cochrane',
    author_email='jean@jeancochrane.com',
    url='https://github.com/jeancochrane/pytest-flask-sqlalchemy',
    description='A pytest plugin for preserving test isolation in Flask-SQlAlchemy using database transactions.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    version= release,
    packages=['pytest_flask_sqlalchemy'],
    install_requires=['pytest>=3.2.1',
                      'pytest-mock>=1.6.2',
                      'SQLAlchemy>=1.2.2',
                      'Flask-SQLAlchemy>=2.3',
                      'packaging>=14.1'],
    extras_require={'tests': ['pytest-postgresql<2.0', 'psycopg2-binary']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Pytest',
    ],

    # Make the package available to pytest
    entry_points={
        'pytest11': [
            'pytest-flask-sqlalchemy = pytest_flask_sqlalchemy.plugin',
        ]
    },

    # Sphinx 
    command_options={'build_sphinx': { # Pull this info from a PROJECT.__meta__ module
        'project': ('setup.py', project),
        'version': ('setup.py', version),
        'release': ('setup.py', release),
        'source_dir': ('setup.py', 'docs')}},
)
