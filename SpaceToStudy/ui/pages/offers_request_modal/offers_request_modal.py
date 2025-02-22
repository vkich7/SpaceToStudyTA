from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SpaceToStudy.ui.elements.checkbox import Checkbox
from SpaceToStudy.ui.elements.chip import Chip
from SpaceToStudy.ui.elements.input import Input
from SpaceToStudy.ui.elements.input_with_drop_down_list import InputDropDownList
from SpaceToStudy.ui.elements.textarea import Textarea
from SpaceToStudy.ui.pages.base_component import BaseComponent

MODAL_NAME = (By.XPATH, "/html/body/div[2]/div[3]/form/p[1]")
MODAL_DESC = (By.XPATH, "/html/body/div[2]/div[3]/form/p[2]")
CLOSE_BTN = (By.XPATH, "/html/body/div[2]/div[3]/button")
CREATE_OFFER_BTN = (By.XPATH, "//button[contains(@type, 'submit')][1]")
ADD_TO_DRAFT_BTN = (By.XPATH, "//button[contains(@type, 'submit')][2]")

FIRST_BLOCK_OF_MODAL = (By.XPATH, "/html/body/div[2]/div[3]/form/div[1]")
NUMBER_OF_FIRST_BLOCK = (By.XPATH, "./div[1]/p/span/span")
NAME_OF_FIRST_BLOCK = (By.XPATH, "./div[1]/p/span")
DESC_BEFORE_CATEGORY = (By.XPATH, "./div[2]/div[1]/p")
CATEGORY_INPUT = (By.XPATH, "./div[2]/div[1]/div[1]/div")
SUBJECT_INPUT = (By.XPATH, "./div[2]/div[1]/div[2]/div")
DESC_BEFORE_CHECKBOX = (By.XPATH, "./div[2]/div[2]/p")
CHECKBOX_BEGINNER = (By.XPATH, "./div[2]/div[2]/div/label[1]")
CHECKBOX_INTERMEDIATE = (By.XPATH, "./div[2]/div[2]/div/label[2]")
CHECKBOX_ADVANCED = (By.XPATH, "./div[2]/div[2]/div/label[3]")
CHECKBOX_TEST_PREPARATION = (By.XPATH, "./div[2]/div[2]/div/label[4]")
CHECKBOX_PROFESSIONAL = (By.XPATH, "./div[2]/div[2]/div/label[5]")
CHECKBOX_SPECIALIZED = (By.XPATH, "./div[2]/div[2]/div/label[6]")

SECOND_BLOCK_OF_MODAL = (By.XPATH, "/html/body/div[2]/div[3]/form/div[2]")
NAME_OF_SECOND_BLOCK = (By.XPATH, "./div[1]/p/span")
NUMBER_OF_SECOND_BLOCK = (By.XPATH, "./div[1]/p/span/span")
TITLE_INPUT = (By.XPATH, "./div[2]/div[1]")
DESCRIBE_INPUT = (By.XPATH, "./div[2]/div[2]")
DESC_BEFORE_LANGUAGE = (By.XPATH, "./div[2]/div[3]/p")
LANGUAGE_INPUT = (By.XPATH, "./div[2]/div[3]/div[1]/div")
LANGUAGE_CHIPS = (By.XPATH, ".//div[contains(@data-testid, 'chip')]")
DESC_BEFORE_PRICE = (By.XPATH, "./div[2]/div[4]/p")
PRICE_INPUT = (By.XPATH, "./div[2]/div[4]/div")
PRICE_IMG = (By.XPATH, ".//img")

THIRD_BLOCK_OF_MODAL = (By.XPATH, "/html/body/div[2]/div[3]/form/div[3]")
NAME_OF_THIRD_BLOCK = (By.XPATH, "./div[1]/p/span")
NUMBER_OF_THIRD_BLOCK = (By.XPATH, "./div[1]/p/span/span")
DESC_BEFORE_QUESTION = (By.XPATH, "./div[2]/p[1]")
QUESTION_INPUT = (By.XPATH, "./div[2]/div[1]/div/div[1]")
ANSWER_INPUT = (By.XPATH, "./div[2]/div[1]/div/div[2]/div/div/textarea[1]")
ADD_QUESTION_BTN = (By.XPATH, ".//button[contains(@type, 'button')]")
ADDITION_QUESTION_INPUT = (By.XPATH, "./div[2]/div[2]/div/div[1]")
ADDITION_ANSWER_INPUT = (By.XPATH, "./div[2]/div[2]/div/div[2]/div")
QUESTION_CLOSE_BTN = (By.XPATH, "./div[2]/div[1]/button")
ADDITION_CLOSE_BTN = (By.XPATH, "./div[2]/div[2]/button")


class OffersRequestModal(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._modal_name = None
        self._modal_desc = None
        self._close_btn = None
        self._create_offer_btn = None
        self._add_to_draft_btn = None

    def get_modal_name(self) -> str:
        if not self._modal_name:
            self._modal_name = self.node.find_element(*MODAL_NAME)
        return self._modal_name.text

    def get_modal_desc(self) -> str:
        if not self._modal_desc:
            self._modal_desc = self.node.find_element(*MODAL_DESC)
        return self._modal_desc.text

    def get_close_btn(self) -> WebElement:
        if not self._close_btn:
            self._close_btn = self.node.find_element(*CLOSE_BTN)
        return self._close_btn

    def get_add_to_draft_btn(self) -> WebElement:
        if not self._add_to_draft_btn:
            self._add_to_draft_btn = self.node.find_element(*ADD_TO_DRAFT_BTN)
        return self._add_to_draft_btn

    def get_create_offer_btn(self) -> WebElement:
        if not self._create_offer_btn:
            self._create_offer_btn = self.node.find_element(*CREATE_OFFER_BTN)
        return self._create_offer_btn

    def click_close_btn(self):
        self.get_close_btn().click()

    def click_add_to_draft_btn(self):
        self.get_add_to_draft_btn().click()
        sleep(2)

    def click_create_offer_btn(self):
        self.get_create_offer_btn().click()

    def is_btn_displayed(self: WebElement) -> bool:
        if self.is_displayed():
            return True
        return False

    def get_btn_name(self, btn: WebElement) -> str:
        return btn.text


class FirstBlock(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name_of_first_block = None
        self._number_of_first_block = None
        self._desc_before_category = None
        self._category_input = None
        self._subject_input = None
        self._desc_before_checkbox = None
        self._checkbox_beginner = None
        self._checkbox_intermediate = None
        self._checkbox_advanced = None
        self._checkbox_test_preparation = None
        self._checkbox_professional = None
        self._checkbox_specialized = None

    def get_name_of_first_block(self) -> str:
        if not self._name_of_first_block:
            self._name_of_first_block = self.node.find_element(*NAME_OF_FIRST_BLOCK)
        return self._name_of_first_block.text

    def get_number_of_first_block(self) -> str:
        if not self._number_of_first_block:
            self._number_of_first_block = self.node.find_element(*NUMBER_OF_FIRST_BLOCK)
        return self._number_of_first_block.text

    def get_desc_before_category(self) -> str:
        if not self._desc_before_category:
            self._desc_before_category = self.node.find_element(*DESC_BEFORE_CATEGORY)
        return self._desc_before_category.text

    def get_category_input(self) -> InputDropDownList:
        if not self._category_input:
            node = self.node.find_element(*CATEGORY_INPUT)
            self._category_input = InputDropDownList(node)
        return self._category_input

    def get_subject_input(self) -> InputDropDownList:
        if not self._subject_input:
            node = self.node.find_element(*SUBJECT_INPUT)
            self._subject_input = InputDropDownList(node)
        return self._subject_input

    def get_desc_before_checkbox(self) -> str:
        if not self._desc_before_checkbox:
            self._desc_before_checkbox = self.node.find_element(*DESC_BEFORE_CHECKBOX)
        return self._desc_before_checkbox.text

    def get_checkbox_beginner(self) -> Checkbox:
        if not self._checkbox_beginner:
            node = self.node.find_element(*CHECKBOX_BEGINNER)
            self._checkbox_beginner = Checkbox(node)
        return self._checkbox_beginner

    def get_checkbox_intermediate(self) -> Checkbox:
        if not self._checkbox_intermediate:
            node = self.node.find_element(*CHECKBOX_INTERMEDIATE)
            self._checkbox_intermediate = Checkbox(node)
        return self._checkbox_intermediate

    def get_checkbox_advanced(self) -> Checkbox:
        if not self._checkbox_advanced:
            node = self.node.find_element(*CHECKBOX_ADVANCED)
            self._checkbox_advanced = Checkbox(node)
        return self._checkbox_advanced

    def get_checkbox_test_preparation(self) -> Checkbox:
        if not self._checkbox_test_preparation:
            node = self.node.find_element(*CHECKBOX_TEST_PREPARATION)
            self._checkbox_test_preparation = Checkbox(node)
        return self._checkbox_test_preparation

    def get_checkbox_professional(self) -> Checkbox:
        if not self._checkbox_professional:
            node = self.node.find_element(*CHECKBOX_PROFESSIONAL)
            self._checkbox_professional = Checkbox(node)
        return self._checkbox_professional

    def get_checkbox_specialized(self) -> Checkbox:
        if not self._checkbox_specialized:
            node = self.node.find_element(*CHECKBOX_SPECIALIZED)
            self._checkbox_specialized = Checkbox(node)
        return self._checkbox_specialized


class SecondBlock(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name_of_second_block = None
        self._number_of_second_block = None
        self._title_input = None
        self._describe_input = None
        self._desc_before_language = None
        self._language_input = None
        self._language_chips = None
        self._desc_before_price = None
        self._price_img = None
        self._price_input = None

    def get_name_of_second_block(self) -> str:
        if not self._name_of_second_block:
            self._name_of_second_block = self.node.find_element(*NAME_OF_SECOND_BLOCK)
        return self._name_of_second_block.text

    def get_number_of_second_block(self) -> str:
        if not self._number_of_second_block:
            self._number_of_second_block = self.node.find_element(*NUMBER_OF_SECOND_BLOCK)
        return self._number_of_second_block.text

    def get_title_input(self) -> Textarea:
        if not self._title_input:
            node = self.node.find_element(*TITLE_INPUT)
            self._title_input = Textarea(node)
        return self._title_input

    def get_describe_input(self) -> Textarea:
        if not self._describe_input:
            node = self.node.find_element(*DESCRIBE_INPUT)
            self._describe_input = Textarea(node)
        return self._describe_input

    def get_desc_before_language(self) -> str:
        if not self._desc_before_language:
            self._desc_before_language = self.node.find_element(*DESC_BEFORE_LANGUAGE)
        return self._desc_before_language.text

    def get_language_input(self) -> InputDropDownList:
        if not self._language_input:
            node = self.node.find_element(*LANGUAGE_INPUT)
            self._language_input = InputDropDownList(node)
        return self._language_input

    def get_language_chips(self) -> tuple[Chip]:
        if not self._language_chips:
            set_of_chips = self.node.find_elements(*LANGUAGE_CHIPS)
            self._language_chips = [Chip(chip) for chip in set_of_chips]
        return self._language_chips

    def is_language_dropdown_list_open(self) -> bool:
        if self.get_language_input().get_input().get_attribute("aria-expanded") == "true":
            return True
        return False

    def get_desc_before_price(self) -> str:
        if not self._desc_before_price:
            self._desc_before_price = self.node.find_element(*DESC_BEFORE_PRICE)
        return self._desc_before_price.text

    def get_price_img(self) -> WebElement:
        if not self.get_price_img():
            self._price_img = self.node.find_element(*PRICE_IMG)
        return self._price_img

    def get_price_input(self) -> Input:
        if not self._price_input:
            node = self.node.find_element(*PRICE_INPUT)
            self._price_input = Input(node)
        return self._price_input


class ThirdBlock(BaseComponent):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._name_of_third_block = None
        self._number_of_third_block = None
        self._desc_before_question = None
        self._question_input = None
        self._answer_input = None
        self._add_question_btn = None
        self._addition_question_input = None
        self._addition_answer_input = None
        self._question_close_btn = None
        self._addition_close_btn = None

    def get_name_of_third_block(self) -> str:
        if not self._name_of_third_block:
            self._name_of_third_block = self.node.find_element(*NAME_OF_THIRD_BLOCK)
        return self._name_of_third_block.text

    def get_number_of_third_block(self) -> str:
        if not self._number_of_third_block:
            self._number_of_third_block = self.node.find_element(*NUMBER_OF_THIRD_BLOCK)
        return self._number_of_third_block.text

    def get_desc_before_question(self) -> str:
        if not self._desc_before_question:
            self._desc_before_question = self.node.find_element(*DESC_BEFORE_QUESTION)
        return self._desc_before_question.text

    def get_question_input(self) -> Input:
        if not self._question_input:
            node = self.node.find_element(*QUESTION_INPUT)
            self._question_input = Input(node)
        return self._question_input

    def get_answer_input(self) -> WebElement:
        if not self._answer_input:
            self._answer_input = self.node.find_element(*ANSWER_INPUT)
        return self._answer_input

    def get_answer_input_text(self) -> str:
        return self.get_answer_input().text

    def set_answer_input_text(self, text: str):
        self.get_answer_input().send_keys(text)

    def get_add_question_btn(self) -> WebElement:
        if not self._add_question_btn:
            self._add_question_btn = self.node.find_element(*ADD_QUESTION_BTN)
        return self._add_question_btn

    def click_add_question_btn(self):
        return self.get_add_question_btn().click()

    def get_add_question_name(self) -> str:
        return self.get_add_question_btn().text

    def get_addition_question_input(self) -> Input:
        if not self._addition_question_input:
            node = self.node.find_element(*ADDITION_QUESTION_INPUT)
            self._addition_question_input = Input(node)
        return self._addition_question_input

    def get_addition_answer_input(self) -> WebElement:
        if not self._addition_answer_input:
            self._addition_answer_input = self.node.find_element(*ADDITION_ANSWER_INPUT)
        return self._addition_answer_input

    def get_additional_answer_input_text(self) -> str:
        return self.get_addition_answer_input().text

    def set_additional_answer_input_text(self, text: str):
        self.get_addition_answer_input().send_keys(text)

    def get_question_close_btn(self) -> WebElement:
        if not self._question_close_btn:
            self._question_close_btn = self.node.find_element(*QUESTION_CLOSE_BTN)
        return self._question_close_btn

    def click_question_close_btn(self):
        self.get_question_close_btn().click()

    def get_addition_close_btn(self) -> WebElement:
        if not self._addition_close_btn:
            self._addition_close_btn = self.node.find_element(*ADDITION_CLOSE_BTN)
        return self._addition_close_btn

    def click_addition_close_btn(self):
        self.get_addition_close_btn().click()

    def is_btn_displayed(self:WebElement) -> bool:
        if self.is_displayed():
            return True
        return False
