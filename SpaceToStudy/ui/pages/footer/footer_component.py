from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

PRIVACY_POLICY = (By.XPATH, "./div/a[1]")
TERM_OF_USE = (By.XPATH, "./div/a[2]")
ALL_RIGHTS = (By.XPATH, "./span")


class Footer(BaseComponent):

    def __init__(self, node: WebElement):
        super().__init__(node)
        self._privacy_policy = None
        self._term_of_use = None
        self._all_rights = None

    def get_privacy_policy_text(self) -> str:
        if not self._privacy_policy:
            self._privacy_policy = self.node.find_element(*PRIVACY_POLICY)
        return self._privacy_policy.text

    def click_privacy_policy(self):
        if not self._privacy_policy:
            self._privacy_policy = self.node.find_element(*PRIVACY_POLICY)
            self._privacy_policy.click()

    def get_term_of_use_text(self) -> str:
        if not self._term_of_use:
            self._term_of_use = self.node.find_element(*TERM_OF_USE)
        return self._term_of_use.text

    def click_term_of_use(self):
        if not self._term_of_use:
            self._term_of_use = self.node.find_element(*TERM_OF_USE)
            self._term_of_use.click()

    def get_all_rights_text(self) -> str:
        if not self._all_rights:
            self._all_rights = self.node.find_element(*ALL_RIGHTS)
        return self._all_rights.text
