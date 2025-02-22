from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.pages.base_component import BaseComponent

PRICE = (By.XPATH, "./div[3]/div/p")


class OffersCardComponent(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._price = None

    def get_price(self) -> str:
        if not self._price:
            self._price = self.node.find_element(*PRICE)
        return self._price.text

    def get_price_without_currency(self):
        return self.get_price().replace("UAH", "")

