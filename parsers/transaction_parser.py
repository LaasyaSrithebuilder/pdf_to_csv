from interfaces import TransactionParser
from utils.date_parser import parse_date
import re

class RblTransactionParser(TransactionParser):

    AMOUNT_REGEX = r"(?P<amount>[\d,]+\.\d{2}\s*(Cr|Dr)?)"

    def parse(self, text: str) -> list:
        transactions = []

        for line in text.split("\n"):
            line = line.strip()
            parts = line.split()  # simple split to get first token as date candidate

            if not parts:
                continue

            date_candidate = parts[0]
            try:
                date = parse_date(date_candidate)
            except ValueError:
                continue  # skip lines where the first token is not a date

            # Amount detection as before
            amount_match = re.search(self.AMOUNT_REGEX, line)
            if amount_match:
                raw_amount = amount_match.group("amount").replace(",", "").strip()
                if raw_amount.endswith("Cr") or raw_amount.endswith("Dr"):
                    amount = raw_amount[:-2] + " " + raw_amount[-2:]
                else:
                    amount = raw_amount

                # Description = everything between date and amount
                start = line.find(date_candidate) + len(date_candidate)
                end = amount_match.start()
                description = line[start:end].strip()

                transactions.append([date, description, "", amount])

        return transactions
