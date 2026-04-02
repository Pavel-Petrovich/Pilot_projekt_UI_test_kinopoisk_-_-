import allure
import pytest

@allure.feature("Главная страница")
class TestMainPage:

    @allure.title("Проверка работы кнопки 'Магазин'")
    @allure.description('Дождаться кликабельности кнопки "Магазин", Кликнуть кнопку "Магазин", '
                        'Проверка перехода на страницу "Магазин"')
    def test_work_button_shop(self, driver, main_page):
        main_page.wait_for_click_shop()
        main_page.click_button_shop()
        assert main_page.checking_the_transition_to_the_shop_page()
