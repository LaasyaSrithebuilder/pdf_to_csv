# PDF to CSV Bank Statement Parser

This project extracts transaction and customer details from bank statement PDFs
and converts them into structured CSV files.

## Features
- Extracts raw text from PDFs using pdfplumber
- Parses transaction and customer data separately
- Outputs clean, readable CSV files
- Designed using SOLID principles for extensibility

## Project Structure
- extractors/ : PDF text extraction
- parsers/    : Transaction and customer parsing logic
- writers/    : CSV output formatting

## Requirements
- Python 3.9+
- pdfplumber

## Setup
pip install -r requirements.txt

## Run
python main.py

## Notes
- The system is designed to handle inconsistent PDF formatting
- New bank formats or output types can be added without changing core logic
