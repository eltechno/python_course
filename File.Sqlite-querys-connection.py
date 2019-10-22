from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Chinook.sqlite")
con = engine.connect()
rs = con.execute("SELECT * FROM Employee")
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys() # to fix the columns names
con.close()

print(df.head())


with engine.connect() as con:
    rs = con.execute("SELECT * from Employee where 'EmployeeID' >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())


# Open engine in context manager
with engine.connect() as con:
    rs = con.execute("SELECT * from Employee order by BirthDate")
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
df.columns = rs.keys()

# Print head of DataFrame
print(df.head())
