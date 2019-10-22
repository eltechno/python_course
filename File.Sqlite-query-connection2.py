
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///Chinook.sqlite")

with engine.connect() as con:
    rs = con.execute("SELECT EmployeeId, LastName, Email  FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()  # to fix the columns names

# with this code we can forget to close the connection
#or avoid any problem forgetting to close the connection

print(df)