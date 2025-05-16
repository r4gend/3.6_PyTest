import time

def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Для визуальной проверки языка
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_basket_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(add_to_basket_button) > 0, "Add to basket button is not present"