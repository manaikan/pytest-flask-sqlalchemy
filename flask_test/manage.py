"""Management

This module provides the means for creating a database, populating with witha given schema and then dropping the database after the fact.
This is largely done to assist in testing PyTest-Flask-SQLAlchemy against multiple databases.
"""
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy.engine.url import make_url

#: The SQL commands used to create the schema in different databases
SCHEMA = {"mssql":"""
CREATE TABLE [dbo].[table](
	[id] [int] NOT NULL,
	[name] [nchar](80) NULL,
 CONSTRAINT [PK_table] PRIMARY KEY CLUSTERED 
(
	[id] ASC
) WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
""",}


def create(target, database, *args, **kvps):
    """Create a new database for this test suite

    :param trgt: The database url, `DATABASE+PROTOCOL://USERNAME:PASSWORD@HOSTNAME:HOSTPORT`, without the `DATASTORE`
    :param args: reserved
    :param database: The datastore name
    :param kvps: reserved
    :return: None

    .. note::

        SQL-Alchemy creates a session upon first connecting to the database.
        This session has to be exited before creatting the database; SQL-Alchemy may complain that no work was done e.g.::

            Cannot commit transaction: (3902, b'The COMMIT TRANSACTION request has no corresponding BEGIN TRANSACTION.DB-Lib error message 20018, severity 16:\nGeneral SQL Server error: Check messages from the SQL Server\n')

        For the most part this message can be ignored but one might verify that the database has indeed been created.
    """
    # This could be improved by using the sqlalchemy-utils package [1]
    #
    # [1] https://stackoverflow.com/a/30971098
    trgt = make_url(target)
    ngin = create_engine(trgt)
    try :
        cnxn = ngin.connect()  # autocommit=True does ot work ?
        cnxn.execute("commit") # Terminate existing transaction
        cnxn.execute("create database {}".format(database))
    except Exception as error:
        print(error)
    finally :
        cnxn.close()

def schema(target, *args, **kvps):
    """Given an empty database populate this with the schema necessary for this test suit

    :param target: The database url, `DATABASE+PROTOCOL://USERNAME:PASSWORD@HOSTNAME:HOSTPORT/DATASTORE`
    :param args: reserved
    :param kvps: reserved
    :return:

    The net effect is to provide a database with a single table called `table`; having the columns :

        `id`
            The primary key and index for the table,
        `name`
            A string value, NCHAR(80).
    """
    trgt = make_url(target)
    ngin = create_engine(trgt)
    meta = MetaData(ngin)
    table = Table("table", meta,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(80), ))
    meta.create_all()


def delete(target, database, *args, **kvps):
    """Delete the database given the the service URL

    :param trgt: The `DATABASE_URL` with or without the `DATASTORE`
    :param args: reserved
    :param database: The datastore name, when `DATABASE_URL` excludes it
    :param kvps: reserved
    :return: None

    .. note::

        SQL-Alchemy creates a session upon first connecting to the database.
        This session has to be exited before deleting the database; SQL-Alchemy may complain that no work was done e.g.::

            Cannot commit transaction: (3902, b'The COMMIT TRANSACTION request has no corresponding BEGIN TRANSACTION.DB-Lib error message 20018, severity 16:\nGeneral SQL Server error: Check messages from the SQL Server\n')

        For the most part this message can be ignored but one might verify that the database has indeed been dropped.
    """
    # This could be improved by using the sqlalchemy-utils package [1]
    #
    # [1] https://stackoverflow.com/a/30971098
    trgt = make_url(target)
    ngin = create_engine(trgt)
    try :
        cnxn = ngin.connect()  # autocommit=True does ot work ?
        cnxn.execute("commit") # Terminate existing transaction
        cnxn.execute("drop database {}".format(database))
    except Exception as error:
        print(error)
    finally :
        cnxn.close()
