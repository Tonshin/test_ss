import allure

from pages.page_forms import PageForm

@allure.title("Проверить отправку валидно заполненной формы")
@allure.description("""
    Цель: Проверить работу личного кабинета
    Шаги:
    1. Авторизоваться пользователем «Harry Potter»
    2. Выполнить пополнение счета (Deposit) и списание (Withdrawl)
    3. Записать данные в CSV
    """)
def test_form_submit_success(browser):
    page_form = PageForm(browser, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page_form.open()
    page_form.click_customer_login()
    page_form.choose_harry()
    page_form.top_up_balance()
    page_form.debit_account()
    page_form.check_balance()
    page_form.check_transactions_in_form()
    csv_path = page_form.write_csv_step()
    page_form.attach_csv_file(csv_path)