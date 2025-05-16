import time
from selenium.webdriver.common.by import By  # Добавьте импорт

def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)

    # Новый синтаксис Selenium 4
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_basket_button) > 0, "Кнопка добавления в корзину не найдена!"
