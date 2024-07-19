import allure

from data.data import result_fibbonaci
from helpers.others import attach_csv_file, write_csv
from pages.page_forms import PageForm

COUNT_FIBBONACI = result_fibbonaci()


@allure.title("Проверить отправку валидно заполненной формы")
@allure.description("""
    Цель: Проверить работу личного кабинета
    Шаги:
    1. Авторизоваться пользователем «Harry Potter»
    2. Выполнить пополнение счета (Deposit) и списание (Withdrawl)
    3. Записать данные в CSV
    """)
def test_form_submit_success(browser):
    page_form = PageForm(browser, PageForm.PAGE_FORM_URL)
    page_form.open()
    page_form.click_customer_login()
    page_form.choose_harry()
    page_form.top_up_balance(COUNT_FIBBONACI)
    page_form.debit_account(COUNT_FIBBONACI)
    page_form.check_balance(0)
    page_form.check_num_transactions_in_form(2)
    page_form.check_amount_in_transaction(COUNT_FIBBONACI)
    csv_file = write_csv(page_form.read_transactions())
    attach_csv_file(csv_file)