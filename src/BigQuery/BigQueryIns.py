from google.cloud import bigquery # bigQuery config

def BigQueryIns_rows(dataset, rows_json) :
    client = bigquery.Client()
    errors = client.insert_rows_json(
        dataset, rows_json, row_ids=[None] * len(rows_json))
    print(errors)
    return errors
