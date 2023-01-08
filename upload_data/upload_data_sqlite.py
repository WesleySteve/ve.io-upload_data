import os
import pandas as pd

from database.conections.sqlite import create_db_sqlite, connect_db_sqlite


# project path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

def check_db_exists():
  """
    Check database file '.db'
    
    Returns:
      False: if not exists
      True: if exists
  """
  
  base_db = [i for i in os.listdir(DATA_DIR) if i.endswith(".db")]
  
  if len(base_db) == 0:
    return False
  else:
    return True
  

def create_db_files_xlsx_and_xls():
  """
    Create Sqlite database with '.xls' and '.xlsx' files
    
    Returns:
      Connection
  """
  
  if not check_db_exists():
  
    files = [i for i in os.listdir(DATA_DIR) if i.endswith(".xls") or i.endswith(".xlsx")]
    
    if len(files) > 0:
      # open connection
      
      con = create_db_sqlite(DATA_DIR, "banco")
      
      for i in files:
        df_tmp = pd.read_excel(os.path.join(DATA_DIR, i))
        
        if i.endswith(".xlsx"):
          name_table = i.strip(".xlsx")
          df_tmp.to_sql(name_table, con, index=False)
          
        elif i.endswith(".xls"):
          name_table = i.strip(".xls")
          df_tmp.to_sql(name_table, con, index=False)
          
      print("Sqlite database sucessfully created")
      
      return True
    
  else:  
    print("The data file was not loadd")
    
    return False

  
def connect_db_sqlite():
  """
    Connection with database sqlite
    
    Returns:
      Connection
  """  
  
  if check_db_exists():
  
    con = connect_db_sqlite(DATA_DIR)
  
    if con:
      print("Database connection sucessfully")
    
      return True
  
  else:
    print("Failure connection with database")
    
    return False
    
    
  