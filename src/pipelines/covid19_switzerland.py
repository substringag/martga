import requests
import csv
from dagster import pipeline, solid


@solid
def covid19_switzerland(context):
    response = requests.get(
        "https://data.bs.ch/explore/dataset/100077/download/?format=csv&timezone=Europe/Zurich&lang=en&use_labels_for_header=true&csv_separator=%3B")
    lines = response.text.split("\n")
    rows = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(rows)} rows")

    return rows


@pipeline
def covid19_switzerland_pipeline():
    covid19_switzerland()
