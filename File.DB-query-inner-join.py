from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Northwind.sqlite")
df = pd.read_sql_query("Select OrderID, CustomerID from Orders INNER JOIN Customer on Orders.CustomerID = Customers.CustomerID", engine)
print(df.head())



engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())