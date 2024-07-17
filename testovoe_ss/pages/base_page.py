from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv

from data.data import TIME_WAIT


class BasePage:
    def __init__(self, browser, url=None, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=TIME_WAIT):
         return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=TIME_WAIT):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def check_transactions(self):
        rows = self.browser.find_elements(By.CSS_SELECTOR, "tr[id^='anchor']")
        global transactions
        transactions = []
        for row in rows:
            date = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
            amount = int(row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text)
            transaction_type = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
            transactions.append({
                "date": date,
                "amount": amount,
                "type": transaction_type
            })
        return transactions

    def write_csv(self):
        csv_file = "transactions.csv"
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Дата-времяТранзакции", "Сумма", "ТипТранзакции"])
            for transaction in transactions:
                writer.writerow([transaction["date"], transaction["amount"], transaction["type"]])
        return csv_file