import time

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.pages_locators import FormLocators


class PageForm(BasePage):

    locator = FormLocators()

    PAGE_FORM_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    @allure.step("Зайти на страницу регистрации")
    def click_customer_login(self):
        self.element_is_visible(self.locator.CUSTOMER_LOGIN_BUTTON).click()

    @allure.step("Выбрать пользователя Гарри Поттер")
    def choose_harry(self):
        self.element_is_visible(self.locator.USER_SELECT).click()
        self.element_is_visible(self.locator.LOGIN_HARRY).click()
        self.element_is_visible(self.locator.LOGIN_BUTTON).click()

    @allure.step("Выполнить пополнение счета")
    def top_up_balance(self, count: int):
        self.element_is_visible(self.locator.DEPOSIT_BUTTON).click()
        amount_field = self.element_is_visible(self.locator.AMOUNT_FIELD)
        amount_field.send_keys(count)
        self.element_is_visible(self.locator.SUBMIT_AMOUNT_BUTTON).click()
        time.sleep(0.5)  # Ожидание загрузки операции в транзакции(не выполняется без тайм-слип)

    @allure.step("Выполнить списание со счета")
    def debit_account(self, count: int):
        self.element_is_visible(self.locator.WITHDRAWL_BUTTON).click()
        withdrawl_field = self.element_is_visible(self.locator.WITHDRAWL_FIELD)
        withdrawl_field.send_keys(count)
        self.element_is_visible(self.locator.WITHDRAWL_SUBMIT_BUTTON).click()
        time.sleep(0.5)  # Ожидание загрузки операции в транзакции(не выполняется без тайм-слип)

    @allure.step("Проверить баланс")
    def check_balance(self, count: int):
        balance_txt = self.element_is_visible(self.locator.BALANCE).text
        assert int(balance_txt) == count, "Баланс счета не равен нулю"

    @allure.step("Перейти на страницу и проверить наличие транзакций")
    def check_num_transactions_in_form(self, count: int):
        self.element_is_visible(self.locator.TRANSACTION_BUTTON).click()
        transactions = self.read_transactions()
        assert len(transactions) == count, "Транзакций нет"

    @allure.step("Проверка количества суммы в транзакции")
    def check_amount_in_transaction(self, count: int):
        rows = self.browser.find_elements(By.CSS_SELECTOR, "tr[id^='anchor']")
        for row in rows:
            assert int(row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text) == count, \
                "Сумма транзакции не совпадает"

    def read_transactions(self) -> list:
        rows = self.browser.find_elements(By.CSS_SELECTOR, "tr[id^='anchor']")
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