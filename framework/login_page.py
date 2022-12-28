from .page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    def login(self, username: str, password: str) -> bool:
        self.click_element(By.ID, "com.ajaxsystems:id/login")
        self.insert_value_to_field(
            By.XPATH,
            "/hierarchy/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
            ".RelativeLayout/android.widget.EditText[1]",
            username
        )
        self.insert_value_to_field(
            By.XPATH,
            "/hierarchy/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
            ".RelativeLayout/android.widget.EditText[2]",
            password
        )
        self.click_element(By.ID, "com.ajaxsystems:id/next")

        wrong_credentials_message = self.find_element(By.ID, "com.ajaxsystems:id/snackbar_text")
        return False if wrong_credentials_message else True
