#! /usr/bin/bash

./process.py && tail -n +2 ../data/price_place.csv  >> ../data/clean_price.csv

psql -a -f load.sql -d gasStations -U luis
