from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

LIST_ITEMS = (By.XPATH, '/html/body/div[1]/div/header/div/ul')
LOGO = (By.XPATH, "/html/body/div[1]/div/header/div/a")
NAVIGATE_ELEMENTS = (By.XPATH, "/html/body/div[1]/div/header/div/ul/li")


class HeaderComponent(BaseComponent):

    def __init__(self, node):
        super().__init__(node)
        self._navigate_elements = None

    def get_logo(self) -> WebElement:
        return self.node.find_element(*LOGO)

    def click_logo(self):
        self.get_logo().click()

    def get_navigate_links(self) -> tuple:
        from SpaceToStudy.ui.pages.header.navigate_component import NavigateComponent
        if self._navigate_elements is None:
            navigate_links = self.node.find_elements(*NAVIGATE_ELEMENTS)
            self._navigate_elements = []
            for element in navigate_links:
                self._navigate_elements.append(NavigateComponent(element))
        return self._navigate_elements
