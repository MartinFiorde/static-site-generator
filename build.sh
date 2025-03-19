#!/bin/bash
python3 -m src.main "/static-site-generator/" docs
cd public && python3 -m http.server 8888