import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)

    @allure.step('Подождать видимости элемента')
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельности элемента')
    def wait_for_click_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Кликнуть элемент страницы')
    def click_page_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step('Найти элемент страницы')
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Найти все элементы')
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Проверка URL')
    def check_to_url(self):
        return self.driver.current_url

    @allure.step('Подождать пока элемент станет невидимым')
    def wait_for_element_hide(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверить видимость элемента')
    def is_element_visible(self, locator):
        element = self.wait_for_element(locator)
        return element.is_displayed()

    @allure.step('Перетащить элемент из ... в ...')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Подождать загрузку страницы')
    def waiting_for_page_load(self, locator):
        self.wait.until(EC.url_to_be(locator))

    @allure.step('Переход на страницу')
    def go_to_page(self, locator):
        self.driver.get(locator)

    @allure.step('Написать текст')
    def write_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Вывод текста элемента')
    def element_text_output(self, locator):
        panel = self.wait.until(EC.visibility_of_element_located(locator))
        return panel.text
