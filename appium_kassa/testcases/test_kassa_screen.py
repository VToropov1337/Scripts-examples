from webdriver.webdriver import Driver
from pages.main import MainPage
from pages.promo import PromoPage


class Test_kassa_screen:

    def setup_class(self):
        self.driver = Driver('/Users/mac/Desktop/desired_android.json', 'http://localhost:4723/wd/hub')
        self.main_page = MainPage(self.driver)
        self.promo_page = PromoPage(self.driver, 3)

    def test_check_titles(self):
        self.promo_page.skip_promo()
        self.promo_page.skip_geo()
        self.promo_page.waiting_main()
        self.main_page.is_movies_title_valid()

    def test_layout_views(self):
        self.main_page.click_footer_tickets()
        self.main_page.click_footer_features()
        self.main_page.swipe_some_screens(1)
        self.main_page.choose_session_time(1)

    def teardown_class(self):
        self.driver.instance.quit()
