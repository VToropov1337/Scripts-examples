class PromoPageLocators:
    NEXT_BUTTON = "ru.rambler.kassa:id/button_next"


class PermissionPageLocators:
    DENY = "com.android.packageinstaller:id/permission_deny_button"


class MainPageLocators:
    TITLE = "ru.rambler.kassa:id/movie_title"
    XPATH_BULLETS = "//android.widget.LinearLayout[@resource-id='ru.rambler.kassa:id/pagerBulletIndicator']/*"
    FOOTER_TICKETS = "ru.rambler.kassa:id/tab_tickets"
    FOOTER_FEATURED = "ru.rambler.kassa:id/tab_featured"
    TOOLBAR = "ru.rambler.kassa:id/toolbar"


class MoviePageLocators:
    MOVIE_SESSION_PATH = "//android.widget.Button[@resource-id='ru.rambler.kassa:id/button_time']"
    MOVIE_LAYOUT_MAP = "ru.rambler.kassa:id/level_map_view"


class TicketPageLocator:
    TICKET_MENU = "ru.rambler.kassa:id/placeholder_image"


class Swipe:
    FORWARD = (972, 989, 160, 998)
    BACK = (65, 755, 946, 750)
