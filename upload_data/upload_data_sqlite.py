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
  
  if len(base_db) == 1:
    return True
  
  else:
    return False
  


def create_db_files_xlsx_or_xls(data_dir, file_name=None):
  """
    Create Sqlite database with '.xls' and '.xlsx' files
    
    Returns:
      Connection
  """
  
  if check_db_exists(data_dir=data_dir):
    
    # open connection
    
    con = connect_db_sqlite(db_path=data_dir)
    
    df_tmp = pd.read_excel(os.path.join(data_dir, file_name))
      
    if file_name.endswith(".xlsx"):
          name_table = file_name.strip(".xlsx")
          df_tmp.to_sql(name_table, con, index=False)
        
    elif file_name.endswith(".xls"):
          name_table = file_name.strip(".xls")
          df_tmp.to_sql(name_table, con, index=False)
        
    print("Sqlite database sucessfully updated")
      
    return True 
    
      
  else:
    
    # open connection
      
      con = create_db_sqlite(data_dir, "banco")
      
      # if file_name == 'DADOS.xlsx' or file_name == 'DADOS.xls':
      df_tmp = pd.read_excel(os.path.join(data_dir, file_name))
      
      if file_name.endswith(".xlsx"):
          name_table = file_name.strip(".xlsx")
          df_tmp.to_sql(name_table, con, index=False)
        
      elif file_name.endswith(".xls"):
          name_table = file_name.strip(".xls")
          df_tmp.to_sql(name_table, con, index=False)
        
      print("Sqlite database sucessfully created")
      
      return True
     

    
def create_db_user(data_dir):
  """
    Create Sqlite database with 'tabele user'
    
    Returns:
      Connection
  """
  
  if check_db_exists(data_dir=data_dir):
    
    # open connection
    
    con = connect_db_sqlite(db_path=data_dir)
        
    print("Sqlite database sucessfully connected")
      
    return True 
    
      
  else:
    
    # open connection
      
      con = create_db_sqlite(data_dir, "banco")
      
      # if file_name == 'DADOS.xlsx' or file_name == 'DADOS.xls':
      # df_tmp = pd.read_excel(os.path.join(data_dir, file_name))
      
      query = pd.read_sql_query = '''
                                CREATE TABLE IF NOT EXISTS USERS 
                                  (
                                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    NAME VARCHAR(100) NOT NULL,
                                    USER_NAME VARCHAR(50) NOT NULL,
                                    PASSWORD VARCHAR(64) NOT NULL
                                  )
                                ''', con, False
                                
      
      print("Sqlite database sucessfully created")
      
      return True
     
        
    

