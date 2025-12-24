# from interfaces import CustomerParser

# class RblCustomerParser(CustomerParser):

#     def parse(self, text: str) -> dict:
#         lines = text.split("\n")

#         name = ""
#         address = []
#         account = ""

#         for line in lines:
#             if "Sameer" in line and not name:
#                 name = line.strip()

#             if "XXXX XXXX" in line:
#                 account = line.strip()

#             if any(keyword in line for keyword in ["PALACE", "ROAD", "SURAT", "GJ"]):
#                 address.append(line.strip())

#         return {
#             "Name": name,
#             "AccountDetails": account,
#             "Address": " ".join(address)
#         }


from interfaces import CustomerParser
import re

class RblCustomerParser(CustomerParser):

    def parse(self, text: str) -> dict:
        lines = [line.strip() for line in text.split("\n") if line.strip()]

        name = ""
        account = ""
        address_lines = []

        for line in lines:

            # 1. Name detection (structure-based, not content-based)
            if not name and re.match(r"^[A-Z][a-z]+(\s[A-Z][a-z]+)+$", line):
                name = line

            # 2. Account number detection (masked format)
            if not account and "XXXX" in line:
                account = line

            # 3. Address detection (multi-line heuristic)
            if any(keyword in line.upper() for keyword in ["ROAD", "STREET", "NAGAR", "PALACE", "SURAT", "GJ"]):
                address_lines.append(line)

        if not name or not account:
            raise ValueError("Failed to parse customer details from statement")

        return {
            "Name": name,
            "AccountDetails": account,
            "Address": " ".join(address_lines)
<<<<<<< HEAD
        }

=======
        }
>>>>>>> 3928b68 (Updated previous code and added new folders)
