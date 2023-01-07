import os
import pandas as pd

from database.conections.sqlite import create_db_sqlite


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
  
