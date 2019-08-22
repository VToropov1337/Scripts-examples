from pages.locators import MainPageLocators, Swipe, MoviePageLocators, TicketPageLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def is_movies_title_valid(self):
        movies = self.driver.instance.find_elements_by_xpath(MainPageLocators.XPATH_BULLETS)
        arr = []
        for i in range(len(movies) - 1):
            el = self.driver.instance.find_element_by_id(MainPageLocators.TITLE)
            if len(el.text) == 0:
                arr.append(i)

            self.driver.instance.swipe(*Swipe.FORWARD)
        assert len(arr) == 0, 'title is empty at index {}'.format(arr)

    def click_footer_tickets(self):
        self.driver.instance.find_element_by_id(MainPageLocators.FOOTER_TICKETS).click()
        self.driver.instance.wait.until(EC.visibility_of_element_located((By.ID, TicketPageLocator.TICKET_MENU)))

    def click_footer_features(self):
        self.driver.instance.find_element_by_id(MainPageLocators.FOOTER_FEATURED).click()
        self.driver.instance.wait.until(EC.visibility_of_element_located((By.ID, MainPageLocators.TOOLBAR)))

    def swipe_some_screens(self, count):
        for _ in range(count):
            self.driver.instance.swipe(*Swipe.FORWARD)

    def choose_session_time(self, index):
        self.driver.instance.find_element_by_xpath(MoviePageLocators.MOVIE_SESSION_PATH + '[{}]'.format(index)).click()
        r = self.driver.instance.find_element_by_id(MoviePageLocators.MOVIE_LAYOUT_MAP)
        assert (r.is_displayed() == True)
