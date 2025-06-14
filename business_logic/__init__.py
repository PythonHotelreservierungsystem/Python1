
from datetime import date, datetime
import sqlite3



def date_to_db(d: date) -> str:
    return d.isoformat()

def db_to_date(s: str) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()
#
## Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, date_to_db)
## Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", db_to_date)