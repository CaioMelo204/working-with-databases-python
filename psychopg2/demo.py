import psycopg2
import psycopg2.extras
from dataclasses import dataclass

@dataclass
class Investment:
    id: int
    coin: str
    currency: str
    amount: float

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

# cursor = connection.cursor()

cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

create_investment_table = """ 
    create table investment (
        id serial primary key,
        coin varchar(255),
        currency varchar(3),
        amount real
    )
"""

add_bitcoin = """
    insert into investment (
        coin,
        currency,
        amount)
        values ('bitcoin', 'usd', 1000)

"""

add_inverstiment_template = """
    insert into investment (
        coin,
        currency,
        amount)
        values %s

"""

data = [
    ("ethereum", "GBP", 10.0),
    ("dogecoin", "EUR", 100.0)
]


select_bitcoin_investiment = "SELECT * FROM investment WHERE coin='bitcoin'"

select_all_investments = "SELECT * FROM investment"

# cursor.execute(add_bitcoin)

# psycopg2.extras.execute_values(cursor, add_inverstiment_template, data)

# cursor.execute(select_bitcoin_investiment)

# data = cursor.fetchone()

cursor.execute(select_all_investments)

data = [Investment(**dict(row)) for row in cursor.fetchall()]

print(data)

for inv in data:
    print(inv.coin)

connection.commit()

cursor.close()
connection.close()