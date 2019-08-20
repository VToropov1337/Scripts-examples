from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_android_kassa:

    def setup_class(self):
        """
        Настройка уст-ва, пропуск промо экранов и отказ от геолокации.
        """
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Pixel_3_API_24",
            "app": "/Users/mac/Desktop/rambler/касса.apk",
            "automationName": "uiautomator2",
            "appPackage": "ru.rambler.kassa",
            "appWaitActivity": "ru.rambler.popcorn.sdk.presentation.screens.onboarding.OnBoardingActivity"
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("ru.rambler.kassa:id/button_next").click()
        self.driver.find_element_by_id("ru.rambler.kassa:id/button_next").click()
        self.driver.find_element_by_id("ru.rambler.kassa:id/button_next").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'ru.rambler.kassa:id/toolbar')))

    def teardown_class(self):
        self.driver.quit()

    def test_titles_for_every_featured_movies(self):
        """
        Считаю буллеты, проверяю длину тайтла и свайпаю на следующий муви
        """
        movies = self.driver.find_elements_by_xpath(
            "//android.widget.LinearLayout[@resource-id='ru.rambler.kassa:id/pagerBulletIndicator']/*")
        for _ in range(len(movies) - 1):
            el = self.driver.find_element_by_id('ru.rambler.kassa:id/movie_title')
            text = el.text
            assert len(text) != 0
            self.driver.swipe(972, 989, 160, 998)

    def test_check_visible_layout(self):
        """
            Возвращаюсь на раздел 'популярное', путем нажатия на раздел 'билеты',
            а после на раздел 'популярное'. И свайпаю на следующий фильм.
            Захожу в сеанс и проверяю отображение зала.
        """
        self.driver.find_element_by_id("ru.rambler.kassa:id/tab_tickets").click()
        self.driver.find_element_by_id("ru.rambler.kassa:id/tab_featured").click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located((By.ID, 'ru.rambler.kassa:id/toolbar')))
        self.driver.swipe(972, 989, 160, 998)
        self.driver.find_element_by_xpath(
            "//android.widget.Button[@resource-id='ru.rambler.kassa:id/button_time'][1]").click()
        r = self.driver.find_element_by_id('ru.rambler.kassa:id/level_map_view')
        assert (r.is_displayed() == True)
