from selenium.webdriver.common.by import By


class FormLocators:

    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-lg")
    USER_SELECT = (By.ID, "userSelect")
    LOGIN_HARRY = (By.XPATH, "//option[text()='Harry Potter']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default")
    DEPOSIT_BUTTON = (By.XPATH, "//button[@class='btn btn-lg tab'][2]")
    AMOUNT_FIELD = (By.CSS_SELECTOR, "input[ng-model='amount']")
    SUBMIT_AMOUNT_BUTTON = (By.XPATH, "//button[@type='submit']")
    BALANCE = (By.XPATH, "//strong[2]")
    WITHDRAWL_BUTTON = (By.XPATH, "//div[3]/button[3]")
    WITHDRAWL_FIELD = (
    By.XPATH, "//label[text()='Amount to be Withdrawn :']/following-sibling::input[@placeholder='amount']")
    WITHDRAWL_SUBMIT_BUTTON = (By.XPATH, "//form/button")
    TRANSACTION_BUTTON = (By.CSS_SELECTOR, "button[ng-click='transactions()']")
    ROWS = (By.CSS_SELECTOR, "tr[id^='anchor']")
    DATE = (By.CSS_SELECTOR, "td:nth-child(1)")
    AMOUNT = (By.CSS_SELECTOR, "td:nth-child(2)")
    TRANSACTION_TYPE = (By.CSS_SELECTOR, "td:nth-child(3)")
