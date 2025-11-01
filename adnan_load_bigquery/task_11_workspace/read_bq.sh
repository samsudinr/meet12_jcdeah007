#!/bin/bash
echo "Autentikasi ke BigQuery..."


export GOOGLE_APPLICATION_CREDENTIALS="/workspace/bigquery.json"
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
PROJECT_ID=$(cat $GOOGLE_APPLICATION_CREDENTIALS | jq -r '.project_id')
gcloud config set project $PROJECT_ID

DATASET="adnan"
TABLE="meet_9_house_prices"

# Query
QUERY="SELECT count(*) FROM \`${PROJECT_ID}.${DATASET}.${TABLE}\` WHERE Price_in_rupees>5000;"

echo "Menjalankan query:"
echo "$QUERY"

# Simpan hasil query ke .csv
bq query --nouse_legacy_sql --format=csv "$QUERY" > filtered_data.csv

echo "Data terfilter disimpan ke filtered_data.csv"
