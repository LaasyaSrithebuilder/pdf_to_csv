from extractors.pdf_extractor import PdfPlumberExtractor
from parsers.transaction_parser import RblTransactionParser
from parsers.customer_parser import RblCustomerParser
from writers.csv_writer import CsvWriter


def process_pdf(pdf_path):
    base = pdf_path.replace(".pdf", "")

    extractor = PdfPlumberExtractor()
    txn_parser = RblTransactionParser()
    cust_parser = RblCustomerParser()
    writer = CsvWriter()

    text = extractor.extract(pdf_path)

    transactions = txn_parser.parse(text)
    customer = cust_parser.parse(text)

    writer.write_transactions(transactions, f"{base}_transactions.csv")
    writer.write_customer(customer, f"{base}_customer.csv")


if __name__ == "__main__":
    for pdf in ["pdf1.pdf", "pdf2.pdf"]:
        process_pdf(pdf)
