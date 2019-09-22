import click
from . import manage

@click.group()
def main():
    """Flask CLI entrypoint for installed package"""

@main.command(help ="Create a database")
@click.argument("target")
@click.argument("database")
def create(target, database, *args, **kvps):
    """
    ::

        flask_test create "DATABASE+PROTOCOL://USERNAME:PASSWORD@HOSTNAME:HOSTPORT" "DATASTORE"

    :param args:
    :param kvps:
    :return:
    """
    manage.create(target, database, *args, **kvps)

@main.command(help ="Create a schema for the database")
@click.argument("target")
def schema(target, *args, **kvps):
    """
    ::

        flask_test schema "DATABASE+PROTOCOL://USERNAME:PASSWORD@HOSTNAME:HOSTPORT/DATASTORE"

    :param args:
    :param kvps:
    :return:
    """
    manage.schema(target, *args, **kvps)


@main.command(help ="Delete a database")
@click.argument("target")
@click.argument("database")
def delete(*args, **kvps):
    """
    ::

        flask_test create "DATABASE+PROTOCOL://USERNAME:PASSWORD@HOSTNAME:HOSTPORT" "DATASTORE"

    :param args:
    :param kvps:
    :return:
    """
    manage.delete(*args, **kvps)


main()
