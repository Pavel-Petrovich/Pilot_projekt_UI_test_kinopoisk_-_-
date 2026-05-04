from selenium.webdriver.common.by import By


class MainPageLocators:
    HOME = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Главная']"  # Главная
    SHOP = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Магазин']"  # Магазин
    MOVIES = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Фильмы']"  # Фильмы
    SERIES = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Сериалы']"  # Сериалы
    TV_CHANNELS = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Телеканалы']"  # Телеканалы
    SPORT = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Спорт']"  # Спорт
    SUBSCRIBE = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Подписки']"  # Подписки
    MOVIE_TICKETS = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Билеты в кино']"  # Билеты в кино
    MEDIA = By.XPATH, "//span[@class='styles_title__Jmj_H' and text()='Медиа']"  # Медиа
    ADVERTISING = By.XPATH, "//div[@aria-label='Коммуникация']"  # Стартовое окно рекламы
    EXIT_ADVERTISING = By.XPATH, "//button[@aria-label='Закрыть коммуникацию']"  # Закрыть стартовое окно рекламы
    CHECKBOX = By.XPATH, "//div[@class='CheckboxCaptcha-Checkbox']"
    SEARCH_FIELD = By.XPATH, "//input[@name='kp_query']"  # Поле ввода поиска
    BLADE_IN_SEARCH_FIELD = By.XPATH, "//a[@id='suggest-item-film-4554']"  # Всплывающий поисковый запрос "Блэйд"


    # $x("//span[@class='styles_title__Jmj_H' and text()='Сериалы']")
