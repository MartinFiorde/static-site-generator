#!/bin/bash
python3 -m src.main "/" public
cd public && python3 -m http.server 8888