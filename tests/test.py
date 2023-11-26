from connection import Connector
from boto3.dynamodb.conditions import Key


def test_connection():
    con = Connector('dynamodb', '../notebooks/config.json')
    res = con.connect()
    tables = []
    for table in res.tables.all():
        print(table.name)
        tables.append(table)
    assert tables != []
def test_connection_2():
    con = Connector('dynamodb', '../notebooks/config.json')
    res = con.connect()
    movies = res.Table('doc-example-table-movies')
    t = movies.get_item(Key={'year': 2013, 'title': '2 Guns'})
    assert t['Item']['info']['actors'] == ['Denzel Washington', 'Mark Wahlberg', 'Paula Patton']
def test_connection_3():
    con = Connector('dynamodb', '../notebooks/config.json')
    res = con.connect()
    movies = res.Table('doc-example-table-movies')
    t = movies.query(
        KeyConditionExpression=Key('year').eq(2013)
    )
    assert t is not None

