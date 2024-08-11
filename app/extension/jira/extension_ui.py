import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:dashboard_page")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/bloompeak-jr-free/mainservlet/chart?dashboardId=10100&itemId=10100")
            page.wait_until_visible((By.ID, "bloompeak-jr-root"))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()

