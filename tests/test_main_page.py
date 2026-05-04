import allure
import pytest

@allure.feature("Главная страница")
class TestMainPage:

    @allure.title("Проверка работы кнопки 'Магазин'")
    @allure.description('Дождаться кликабельности кнопки "Закрыть рекламу" и кликнуть её, если она не появится, идём дальше, Дождаться кликабельности кнопки "Магазин", '
                        'Кликнуть кнопку "Магазин", Дождаться загрузки страницы "Магазин", Проверка перехода на страницу "Магазин"')
    def test_work_button_shop(self, driver, main_page):
        main_page.wait_for_click_exit_advertising_may_be()
        main_page.wait_for_click_shop()
        main_page.click_button_shop()
        main_page.wait_for_the_page_to_load_shop()
        assert main_page.checking_the_transition_to_the_shop_page()

    @allure.title("Проверка работы кнопки 'Фильмы'")
    @allure.description('Дождаться кликабельности кнопки "Закрыть рекламу" и кликнуть её, если она не появится, идём дальше, Дождаться кликабельности кнопки "Фильмы", '
        'Кликнуть кнопку "Фильмы", Дождаться загрузки страницы "Фильмы", Проверка перехода на страницу "Фильмы"')
    def test_work_button_movies(self, driver, main_page):
        main_page.wait_for_click_exit_advertising_may_be()
        main_page.wait_for_click_movies()
        main_page.click_button_movies()
        main_page.wait_for_the_page_to_load_movies()
        assert main_page.checking_the_transition_to_the_movies_page()

    @allure.title("Проверка работы кнопки 'Сериалы'")
    @allure.description('Дождаться кликабельности кнопки "Закрыть рекламу" и кликнуть её, если она не появится, идём дальше, Дождаться кликабельности кнопки "Сериалы", '
        'Кликнуть кнопку "Сериалы", Дождаться загрузки страницы "Сериалы", Проверка перехода на страницу "Сериалы"')
    def test_work_button_series(self, driver, main_page):
        main_page.wait_for_click_exit_advertising_may_be()
        main_page.wait_for_click_series()
        main_page.click_button_series()
        main_page.wait_for_the_page_to_load_series()
        assert main_page.checking_the_transition_to_the_series_page()

    @allure.title("Проверка работы кнопки 'Телеканалы'")
    @allure.description('Дождаться кликабельности кнопки "Закрыть рекламу" и кликнуть её, если она не появится, идём дальше, Дождаться кликабельности кнопки "Телеканалы", '
        'Кликнуть кнопку "Телеканалы", Дождаться загрузки страницы "Телеканалы", Проверка перехода на страницу "Телеканалы"')
    def test_work_button_tv_channels(self, driver, main_page):
        main_page.wait_for_click_exit_advertising_may_be()
        main_page.wait_for_click_tv_channels()
        main_page.click_button_tv_channels()
        main_page.wait_for_the_page_to_load_tv_channels()
        assert main_page.checking_the_transition_to_the_tv_channels_page()

    @allure.title("Проверка работы кнопки 'Спорт'")
    @allure.description('Дождаться кликабельности кнопки "Закрыть рекламу" и кликнуть её, если она не появится, идём дальше, Дождаться кликабельности кнопки "Спорт", '
        'Кликнуть кнопку "Спорт", Дождаться загрузки страницы "Спорт", Проверка перехода на страницу "Спорт"')
    def test_work_button_sport(self, driver, main_page):
        main_page.wait_for_click_exit_advertising_may_be()
        main_page.wait_for_click_sport()
        main_page.click_button_sport()
        main_page.wait_for_the_page_to_load_sport()
        assert main_page.checking_the_transition_to_the_sport_page()

    @allure.title("Проверка работы поисковой строки")
    @allure.description('Дождаться кликабельности кнопки "Закрыть рекламу" и кликнуть её, если она не появится, идём дальше, Дождаться кликабельности кнопки "Спорт", '
        'Кликнуть кнопку "Спорт", Проверка перехода на страницу "Спорт"')
    def test_work_search_field(self, driver, main_page):
        main_page.wait_for_click_exit_advertising_may_be()