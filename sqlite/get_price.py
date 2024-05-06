from api_data import data
import sqlite3
import click
from datetime import datetime

def get_price(coin_id, currency):
    return data[coin_id][currency]

@click.group()
def cli():
    pass

@cli.command()
@click.option('--coin_id', default='bitcoin')
@click.option('--currency', default='USD')
def show_price(coin_id, currency):
    price = get_price(coin_id, currency)
    return print(f'The price of {coin_id} is {price:.2f} {currency.upper()}')

@cli.command()
@click.option('--coin_id', default='bitcoin')
@click.option('--currency', default='USD')
@click.option('--amount', type=float, default=1000)
def add_investiment(coin_id, currency, amount):
    sql = "INSERT INTO investiments VALUES (?, ?, ?);"
    values = (coin_id, currency, amount)
    cursor.execute(sql, values)
    database.commit()
    
    return print(f'You invested {amount:.2f} {currency.upper()} in {coin_id}')

@cli.command()
def get_investiments():
    sql = "SELECT * FROM investiments;"
    cursor.execute(sql)
    investiments = cursor.fetchall()
    for investiment in investiments:
        print(f'You invested {investiment[2]} {investiment[1].upper()} in {investiment[0]}')
        
@cli.command()
def import_investiments(csv_file)
    with open(csv_file, 'r') as f:
        rdr = csv.reader(f, delimiter=",")
        rows = list(rdr)
        sql = "INSERT INTO investiments VALUES (?, ?, ?)"
        cursor.executemany(sql, rows)
        database.commit()
        
        print(f"Imported {len(rows) investiments from {csv_file}}")
    
cli.add_command('show-price', show_price)
cli.add_command('add-investiment', add_investiment)
cli.add_command('get-investiments', get_investiments)
cli.add_command('import-investiments', import_investiments)
    
if __name__ == "__main__":
    database = sqlite3.connect('test.db')
    cursor = database.cursor()
    cli()