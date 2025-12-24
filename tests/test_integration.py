import sys
import os
import pandas as pd

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import process_pdf


def test_pdf_to_csv_integration():
    pdf_path = "pdf1.pdf"

    process_pdf(pdf_path)

    txn_csv = "pdf1_transactions.csv"
    cust_csv = "pdf1_customer.csv"

    assert os.path.exists(txn_csv)
    assert os.path.exists(cust_csv)

    txn_df = pd.read_csv(txn_csv)
    cust_df = pd.read_csv(cust_csv)

    assert not txn_df.empty
    assert not cust_df.empty

    assert "Date" in txn_df.columns
    assert "Amount" in txn_df.columns
    assert "Name" in cust_df.columns
