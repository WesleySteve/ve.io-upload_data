import os
import pandas as pd

from database.conections.sqlite import create_db_sqlite, connect_db_sqlite


# project path
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DATA_DIR = os.path.join(BASE_DIR, "data")

def check_db_exists(data_dir):
  """
    Check database file '.db'
    
    Returns:
      True: if exists
      False: if not exists
  """
  
  base_db = [i for i in os.listdir(data_dir) if i.endswith(".db")]
  
  if len(base_db) > 0:
    return True
  else:
    return False
  

def create_db_files_xlsx_and_xls(data_dir, file_name=None):
  """
    Create Sqlite database with '.xls' and '.xlsx' files
    
    Returns:
      Connection
  """
  
  if not check_db_exists(data_dir=data_dir):
  
    # files = [i for i in os.listdir(data_dir) if i.endswith(".xls") or i.endswith(".xlsx")]
    if file_name != None:
    
      if len(file_name) > 0:
        # open connection
      
        con = create_db_sqlite(data_dir, "banco")
      
        for i in file_name:
          df_tmp = pd.read_excel(os.path.join(data_dir, i))
        
          if i.endswith(".xlsx"):
            name_table = i.strip(".xlsx")
            df_tmp.to_sql(name_table, con, index=False)
          
          elif i.endswith(".xls"):
            name_table = i.strip(".xls")
            df_tmp.to_sql(name_table, con, index=False)
          
        print("Sqlite database sucessfully created")
      
      return True
    
  else:  
    print("The data file was not load")
    
    return False

  
def connect_db_sqlite(data_dir):
  """
    Connection with database sqlite
    
    Returns:
      Connection
  """  
  
  if check_db_exists(data_dir=data_dir):
  
    con = connect_db_sqlite(data_dir)
  
    if con:
      print("Database connection sucessfully")
    
      return True
  
  else:
    print("Failure connection with database")
    
    return False
    
    
  