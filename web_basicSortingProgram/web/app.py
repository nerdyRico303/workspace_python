from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

# flask env. initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dts207tc@localhost:5432/dts207cw2'  # Replace with your DB URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# defining ORM ---
# PART OF TASK 2
# table name can be random
class Info(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    symbol = db.Column(db.VARCHAR, nullable=False)
    fullname = db.Column(db.VARCHAR, nullable=False)
    industry = db.Column(db.VARCHAR, nullable=False)

class Time(db.Model):
    __tablename__ = 'times'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    date = db.Column(db.DATE, nullable=False)
    weeknum = db.Column(db.INTEGER, nullable=False)
    weekday = db.Column(db.INTEGER, nullable=False)

class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    date = db.Column(db.DATE, nullable=False)
    open = db.Column(db.FLOAT, nullable=True)
    high = db.Column(db.FLOAT, nullable=True)
    low = db.Column(db.FLOAT, nullable=True)
    close = db.Column(db.FLOAT, nullable=True)
    volume = db.Column(db.INTEGER, nullable=True)
    symbol = db.Column(db.VARCHAR, nullable=False)
# ---

# function to export csv content to postgres database
def csv_to_db(csv_file, model, column_mapping):
    """Function to import CSV data into the database."""
    data = pd.read_csv(csv_file)
    for _, row in data.iterrows():
        record = model(**{db_col: row[csv_col] for csv_col, db_col in column_mapping.items()})
        db.session.add(record)
    db.session.commit()

# routing to display the table: structure home -> link to tables ---
# PART OF TASK 3
@app.route('/', defaults={'page': 1})
@app.route('/<int:page>')
def unified_table(page):
    # Get filters from the query parameters
    symbol = request.args.get('symbol', type=str)
    start_date = request.args.get('start_date', type=str)
    end_date = request.args.get('end_date', type=str)

    # Number of records per page
    records_per_page = 30
    offset = (page - 1) * records_per_page

    # Base query with joins
    base_query = db.session.query(
        Info.symbol,
        Info.fullname,
        Info.industry,
        Price.date,
        Price.close,
        Price.volume,
        Time.weeknum,
        Time.weekday
    ).join(Price, Info.symbol == Price.symbol).join(Time, Price.date == Time.date)

    # Apply filters to the query
    #ADDED IN TASK 4
    if symbol:
        base_query = base_query.filter(Info.symbol.ilike(f'%{symbol}%'))
    if start_date:
        base_query = base_query.filter(Price.date >= start_date)
    if end_date:
        base_query = base_query.filter(Price.date <= end_date)

    # Get total records after applying filters
    total_records = base_query.count()

    # Apply pagination
    paginated_query = base_query.limit(records_per_page).offset(offset).all()

    # Calculate total pages
    total_pages = (total_records + records_per_page - 1) // records_per_page

    # Pass data and pagination info to the template
    return render_template('table.html', data=paginated_query, page=page, total_pages=total_pages)

@app.context_processor
def utility_processor():
    return dict(getattr=getattr)
#---

# main function
if __name__ == '__main__':
    with app.app_context():
        # Creating the table frameworks
        db.create_all()

        # Import data from info.csv
        csv_to_db(
            csv_file='info.csv',
            model=Info,
            column_mapping={
                'symbol': 'symbol',
                'fullname': 'fullname',
                'industry': 'industry'
            }
        )
        # Import data from price.csv
        csv_to_db(
            csv_file='price.csv',
            model=Price,
            column_mapping={
                'date': 'date',
                'open': 'open',
                'high': 'high',
                'low': 'low',
                'close': 'close',
                'volume': 'volume',
                'symbol': 'symbol'
            }
        )
        # Import data from time.csv
        csv_to_db(
            csv_file='time.csv',
            model=Time,
            column_mapping={
                'date': 'date',
                'weeknum': 'weeknum',
                'weekday': 'weekday'
            }
        )
        
    # running the website database
    # after running, check 127.0.0.1
    app.run(debug=True)