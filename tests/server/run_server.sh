#!/bin/bash

# 가상환경 생성 및 Flask 서버 실행
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
