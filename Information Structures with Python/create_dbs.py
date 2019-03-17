# The main goals of this part of the project are to save data to database and read data from a database.

# create 'baseball.db' database using sqlite3

# create table named 'baseball_stats' with columns: player_name, games_played, average, salary


# create 'stocks.db' database

# 'stocks.db should have columns: company_name, ticker, exchange_country, price, exchange_rate, shares_outstanding,
# net_income, market_value_usd, pe_ratio.


class AbstractDAO:

    def __init__(self, db_name):
        self.db_name = db_name

    pass

    def insert_records(self, records):
        raise NotImplementedError

    def select_all(self):
        raise NotImplementedError

    # class used to connect to database identified by db_name
    def connect(self):

        # connect to self.db_name

        # return the created connection
        pass


class BaseballStatsDAO(AbstractDAO):

    # takes list of records as a parameter
    def insert_records(self, records):

        # call the method connect()

        # using the returned connection, create a cursor

        # execute an INSERT INTO statement to save record to correct table

        # commit the connection

        # close the connection
        pass

    def select_all(self):

        # call the method connect()

        # using the returned connection, create a cursor

        # create an empty decque to hold the records in memory

        # write and execute SELECT statement to get all records of table for DAO

        # for each row, iterate with a for loop to: create new record, and add record to the decque

        # close the connection

        # return the decque

        pass


class StockStatsDAO(AbstractDAO):

    # takes list of records as a parameter
    def insert_records(self, record):

        # call the method connect()

        # using the returned connection, create a cursor

        # execute an INSERT INTO statement to save record to correct table

        # commit the connection

        # close the connection
        pass

    def select_all(self):

        # call the method connect()

        # using the returned connection, create a cursor

        # create an empty decque to hold the records in memory

        # write and execute SELECT statement to get all records of table for DAO

        # for each row, iterate with a for loop to: create new record, and add record to the decque

        # close the connection

        # return the decque

        pass

# load MLB2008.csv using BaseballCSVReader

# load StockValuations.csv using StocksCSVReader

# Instantiate a new DAO instance for BaseballStats

# Instantiate a new DAO instance for StockStats

# Insert the loaded records into baseball database using Baseball DAO's insert_records

# Insert the loaded records into stocks database using Stocks DAO's insert_records


# Using the Instance of StocksStatDAO, select_all records

