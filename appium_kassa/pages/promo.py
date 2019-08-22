from selenium.webdriver.common.by import By
from pages.locators import PromoPageLocators, PermissionPageLocators, Swipe, TicketPageLocator, MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class PromoPage:
    def __init__(self, driver, count):
        self.driver = driver
        self.count = count

    def skip_promo(self):
        for _ in range(self.count):
            self.driver.instance.find_element_by_id(PromoPageLocators.NEXT_BUTTON).click()

    def skip_geo(self):
        self.driver.instance.find_element_by_id(PermissionPageLocators.DENY).click()

    def waiting_main(self):
        self.driver.instance.wait.until(EC.visibility_of_element_located((By.ID, MainPageLocators.TOOLBAR)))
