import time

import allure

from pages.base_page import BasePage
from locators.pages_locators import FormLocators
from data.data import result_fibbonaci


class PageForm(BasePage):

    locator = FormLocators()

    @allure.step("Зайти на страницу регистрации")
    def click_customer_login(self):
        self.element_is_visible(self.locator.CUSTOMER_LOGIN_BUTTON).click()

    @allure.step("Выбрать пользователя Гарри Поттер")
    def choose_harry(self):
        self.element_is_visible(self.locator.USER_SELECT).click()
        self.element_is_visible(self.locator.LOGIN_HARRY).click()
        self.element_is_visible(self.locator.LOGIN_BUTTON).click()

    @allure.step("Выполнить пополнение счета")
    def top_up_balance(self):
        self.element_is_visible(self.locator.DEPOSIT_BUTTON).click()
        amount_field = self.element_is_visible(self.locator.AMOUNT_FIELD)
        amount_field.send_keys(result_fibbonaci())
        self.element_is_visible(self.locator.SUBMIT_AMOUNT_BUTTON).click()
        time.sleep(0.5) #ожидание загрузки операции в транзакции(не выполняется без тайм-слип)

    @allure.step("Выполнить списание со счета")
    def debit_account(self):
        self.element_is_visible(self.locator.WITHDRAWL_BUTTON).click()
        withdrawl_field = self.element_is_visible(self.locator.WITHDRAWL_FIELD)
        withdrawl_field.send_keys(result_fibbonaci())
        self.element_is_visible(self.locator.WITHDRAWL_SUBMIT_BUTTON).click()
        time.sleep(0.5) #ожидание загрузки операции в транзакции(не выполняется без тайм-слип)

    @allure.step("Проверить баланс")
    def check_balance(self):
        balance_txt = self.element_is_visible(self.locator.BALANCE).text
        assert balance_txt == "0", "Баланс счета не равен нулю"

    @allure.step("Перейти на страницу и проверить наличие транзакций")
    def check_transactions_in_form(self):
        self.element_is_visible(self.locator.TRANSACTION_BUTTON).click()
        transaction_check = self.check_transactions()
        assert len(transaction_check) == 2, "Транзакций нет"

    @allure.step("Записать данные в CSV")
    def write_csv_step(self):
        return self.write_csv()

    @allure.step("CSV-файл")
    def attach_csv_file(self, file_path):
        with open(file_path, "rb") as file_csv:
            allure.attach(file_csv.read(), name="transactions.csv", attachment_type=allure.attachment_type.CSV)


