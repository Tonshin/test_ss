import csv

import allure

from data.data import CSV_NAME


def write_csv(transactions: list) -> str:
    csv_file = CSV_NAME
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Дата-времяТранзакции", "Сумма", "ТипТранзакции"])
        for transaction in transactions:
            writer.writerow([transaction["date"], transaction["amount"], transaction["type"]])
    return csv_file


@allure.step("CSV-файл")
def attach_csv_file(file_path):
    with open(file_path, "rb") as file_csv:
        allure.attach(file_csv.read(), name="transactions.csv", attachment_type=allure.attachment_type.CSV)