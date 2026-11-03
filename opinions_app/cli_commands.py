# type: ignore
import csv
import click

import os

from opinions_app import app, db, Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Функция загрузки мнений в базу данных."""
    # Определяем путь к файлу: родительская папка пакета opinions_app
    # + opinions.csv
    CSV_PATH = os.path.join(os.path.dirname
                            (os.path.dirname(__file__)), 'opinions.csv')
    with open(CSV_PATH, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            opinion = Opinion(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1

    click.echo(f'Загружено мнений: {counter}')
