import allure
from pages.base_page import BasePage
from locators import MainPageLocators
from urls import MAIN_URL, SHOP_URL, MOVIES_URL, SERIES_URL, TV_CHANNELS_URL, SPORT_URL, SUBSCRIBE_URL, MOVIE_TICKETS_URL, MEDIA_URL, BLADE_URL
from data import BLADE
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Дождаться кликабельности кнопки "Закрыть рекламу" и кликнуть её, если она не появится, идём дальше')
    def wait_for_click_exit_advertising_may_be(self, timeout=2):
        try:
            self.wait_for_click_element(MainPageLocators.EXIT_ADVERTISING)
            self.click_page_element(MainPageLocators.EXIT_ADVERTISING)
        except TimeoutException:
            print("Реклама не появилась, идём дальше.")

    @allure.step('Дождаться кликабельности кнопки "Закрыть рекламу"')
    def wait_for_click_exit_advertising(self):
        self.wait_for_click_element(MainPageLocators.EXIT_ADVERTISING)

    @allure.step('Кликнуть кнопку "Закрыть рекламу"')
    def click_button_exit_advertising(self):
        self.click_page_element(MainPageLocators.EXIT_ADVERTISING)


    @allure.step('Дождаться кликабельности кнопки "Магазин"')
    def wait_for_click_shop(self):
        self.wait_for_click_element(MainPageLocators.SHOP)

    @allure.step('Кликнуть кнопку "Магазин"')
    def click_button_shop(self):
        self.click_page_element(MainPageLocators.SHOP)

    @allure.step('Дождаться загрузки страницы "Магазин"')
    def wait_for_the_page_to_load_shop(self):
        self.waiting_for_page_load(SHOP_URL)

    @allure.step('Проверка перехода на страницу "Магазин"')
    def checking_the_transition_to_the_shop_page(self):
        return self.check_to_url() in SHOP_URL


    @allure.step('Дождаться кликабельности кнопки "Фильмы"')
    def wait_for_click_movies(self):
        self.wait_for_click_element(MainPageLocators.MOVIES)

    @allure.step('Кликнуть кнопку "Фильмы"')
    def click_button_movies(self):
        self.click_page_element(MainPageLocators.MOVIES)

    @allure.step('Дождаться загрузки страницы "Фильмы"')
    def wait_for_the_page_to_load_movies(self):
        self.waiting_for_page_load(MOVIES_URL)

    @allure.step('Проверка перехода на страницу "Фильмы"')
    def checking_the_transition_to_the_movies_page(self):
        return self.check_to_url() in MOVIES_URL


    @allure.step('Дождаться кликабельности кнопки "Сериалы"')
    def wait_for_click_series(self):
        self.wait_for_click_element(MainPageLocators.SERIES)

    @allure.step('Кликнуть кнопку "Сериалы"')
    def click_button_series(self):
        self.click_page_element(MainPageLocators.SERIES)

    @allure.step('Дождаться загрузки страницы "Сериалы"')
    def wait_for_the_page_to_load_series(self):
        self.waiting_for_page_load(SERIES_URL)

    @allure.step('Проверка перехода на страницу "Сериалы"')
    def checking_the_transition_to_the_series_page(self):
        return self.check_to_url() in SERIES_URL


    @allure.step('Дождаться кликабельности кнопки "Телеканалы"')
    def wait_for_click_tv_channels(self):
        self.wait_for_click_element(MainPageLocators.TV_CHANNELS)

    @allure.step('Кликнуть кнопку "Телеканалы"')
    def click_button_tv_channels(self):
        self.click_page_element(MainPageLocators.TV_CHANNELS)

    @allure.step('Дождаться загрузки страницы "Телеканалы"')
    def wait_for_the_page_to_load_tv_channels(self):
        self.waiting_for_page_load(TV_CHANNELS_URL)

    @allure.step('Проверка перехода на страницу "Телеканалы"')
    def checking_the_transition_to_the_tv_channels_page(self):
        return self.check_to_url() in TV_CHANNELS_URL


    @allure.step('Дождаться кликабельности кнопки "Спорт"')
    def wait_for_click_sport(self):
        self.wait_for_click_element(MainPageLocators.SPORT)

    @allure.step('Кликнуть кнопку "Спорт"')
    def click_button_sport(self):
        self.click_page_element(MainPageLocators.SPORT)

    @allure.step('Дождаться загрузки страницы "Спорт"')
    def wait_for_the_page_to_load_sport(self):
        self.waiting_for_page_load(SPORT_URL)

    @allure.step('Проверка перехода на страницу "Спорт"')
    def checking_the_transition_to_the_sport_page(self):
        return self.check_to_url() in SPORT_URL


    @allure.step('Дождаться кликабельности поисковой строки')
    def wait_for_click_search_field(self):
        self.wait_for_click_element(MainPageLocators.SEARCH_FIELD)

    @allure.step('Кликнуть поисковую строку')
    def click_search_field(self):
        self.click_page_element(MainPageLocators.SEARCH_FIELD)

    @allure.step('Ввести текст "Блэйд"')
    def input_text_blade(self):
        self.write_text(MainPageLocators.SEARCH_FIELD, BLADE)

    @allure.step('Дождаться кликабельности всплывшего поискового запроса "Блэйд"')
    def wait_for_click_search_query_blade(self):
        self.wait_for_click_element(MainPageLocators.BLADE_IN_SEARCH_FIELD)

    @allure.step('Кликнуть всплывшый поисковый запрос "Блэйд"')
    def click_search_query_blade(self):
        self.click_page_element(MainPageLocators.BLADE_IN_SEARCH_FIELD)

    @allure.step('Дождаться загрузки страницы "Блэйд"')
    def wait_for_the_page_to_load_blade(self):
        self.waiting_for_page_load(BLADE_URL)

    @allure.step('Проверка перехода на страницу "Блэйд"')
    def checking_the_transition_to_the_blade_page(self):
        return self.check_to_url() in BLADE_URL