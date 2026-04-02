import allure
from pages.base_page import BasePage
from locators import MainPageLocators
from urls import MAIN_URL, SHOP_URL, MOVIES_URL, SERIES_URL, TV_CHANNELS_URL, SPORT_URL, SUBSCRIBE_URL, MOVIE_TICKETS_URL, MEDIA_URL


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дождаться кликабельности кнопки "Магазин"')
    def wait_for_click_shop(self):
        self.wait_for_click_element(MainPageLocators.SHOP)

    @allure.step('Кликнуть кнопку "Магазин"')
    def click_button_shop(self):
        self.click_page_element(MainPageLocators.SHOP)

    @allure.step('Проверка перехода на страницу "Магазин"')
    def checking_the_transition_to_the_shop_page(self):
        return self.check_to_url() in SHOP_URL
