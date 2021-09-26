import requests
import csv
from dagster import pipeline, solid


@solid
def covid19_switzerland(context):
    response = requests.get(
        "https://data.bs.ch/explore/dataset/100077/download/?format=csv&timezone=Europe/Zurich&lang=en&use_labels_for_header=true&csv_separator=,")
    lines = response.text.split("\n")
    rows = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(rows)} rows")

    file = open('../transformation/data/covid19_switzerland.csv', 'w')
    file.write(response.text)
    file.close()

    return rows


@pipeline
def covid19_switzerland_pipeline():
    covid19_switzerland()
