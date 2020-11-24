from pymongo import MongoClient
from pymongo.cursor import CursorType
from DB.DBHandler import DBHandler
from BigQuery.BigQueryIns import BigQueryIns_rows

def main() :
    cursor_list = DBHandler().find_item(None, "gsn", "gsn")
    cursor_l = []
    for list in cursor_list :
        cursor_l.append(list)
    errors = BigQueryIns_rows('hig-bigqueryproject.hig.fhig', cursor_l)
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

if __name__ == "__main__" :
    main()
