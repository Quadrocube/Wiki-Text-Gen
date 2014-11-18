#!/bin/bash

LINK_COUNT=300
DOMAIN="en.wikipedia.com"

echo "Usage: $0 LINK_COUNT DOMAIN"
if [ $# -gt 0 ]; then
    LINK_COUNT=$1
fi
if [ $# -gt 1 ]; then
    DOMAIN=$2
fi

echo "Crawling for link list from $DOMAIN"
python3 src/get_links.py $LINK_COUNT $DOMAIN
echo "Downloading articles"
python3 src/download_data.py $DOMAIN
echo "Analyzing articles"
python3 src/analyze_data.py $DOMAIN
echo "Generating text"
python3 src/generate_text.py $DOMAIN
