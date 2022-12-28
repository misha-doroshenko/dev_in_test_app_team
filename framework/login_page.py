import time

from .page import Page
from selenium.webdriver.common.by import By
import logging


LOGGER = logging.getLogger(__name__)


class LoginPage(Page):

    def login(self, username: str, password: str) -> bool:
        LOGGER.info("Click login button")
        self.click_element(By.ID, "com.ajaxsystems:id/login")
        LOGGER.info("Insert username")
        self.insert_value_to_field(
            By.XPATH,
            "/hierarchy/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
            ".RelativeLayout/android.widget.EditText[1]",
            username
        )
        LOGGER.info("Insert password")
        self.insert_value_to_field(
            By.XPATH,
            "/hierarchy/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
            ".RelativeLayout/android.widget.EditText[2]",
            password
        )
        LOGGER.info("Click submit button")
        self.click_element(By.ID, "com.ajaxsystems:id/next")

        wrong_credentials_message = self.find_element(By.ID, "com.ajaxsystems:id/snackbar_text")
        return False if wrong_credentials_message else True

    def sidebar_settings(self, username, password):
        self.login(username, password)
        LOGGER.info("Click cancel button in the popup window")
        self.click_pop_up_cancel_button()
        LOGGER.info("Click sidebar button")
        self.click_element(By.ID, "com.ajaxsystems:id/menuDrawer")
        LOGGER.info("Click settings button")
        self.click_element(By.ID, "com.ajaxsystems:id/settings")
        return self.find_element(By.ID, "com.ajaxsystems:id/mail").text

    def click_pop_up_cancel_button(self):
        popup_btn = self.find_element(By.ID, "com.ajaxsystems:id/cancel_button")
        if popup_btn:
            time.sleep(3)
            popup_btn1 = self.find_element(By.ID, "com.ajaxsystems:id/cancel_button")
            popup_btn1.click()
