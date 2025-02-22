from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.base_element import BaseElement

INPUT = (By.XPATH, "./div/input")
LABEL = (By.XPATH, "./label")
ERROR_MESSAGE = (By.XPATH, "./p/span")




class Input(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._input = None
        self._label = None
        self._input_css_class = None
        self._label_location = None

    def get_input(self):
        if not self._input:
            self._input = self.node.find_element(*INPUT)
        return self._input
    
    def set_text(self, text):
        self.get_input().send_keys(text)

    def get_text(self):
        return self.get_input().get_attribute("value")
    
    def get_label(self) -> str:
        if not self._label:
            self._label = self.node.find_element(*LABEL)
        return self._label.text

    def get_label_location(self):
        if self._input:
            self._label_location = self._input.location
        return self._label_location   

    def get_input_css_class(self):
        if self._input:
            self._input_css_class = self._input.get_attribute("class")
        return self._input_css_class  
    
    def get_error_message(self) -> str:
        return self.node.find_element(*ERROR_MESSAGE).text
    
    
class PasswordInput(Input):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._hidden_button = None

    def get_hidden_icon(self):
        if not self._hidden_button:
            self._hidden_button = self.node.find_elements(By.XPATH, "./span")
        return self._hidden_button

    def click_hidden_icon(self):
        self.get_hidden_icon().click()
