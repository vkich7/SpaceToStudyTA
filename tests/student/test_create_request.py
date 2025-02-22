import unittest

from selenium.webdriver.common.by import By

from SpaceToStudy.ui.pages.header.header_component import HeaderComponent
from SpaceToStudy.ui.pages.header.header_unauthorized_component import HeaderUnauthorizedComponent
from SpaceToStudy.ui.pages.offer_details.offer_details import OfferDetailsPage
from SpaceToStudy.ui.pages.offers_request_modal.offers_request_modal import OffersRequestModal, FirstBlock, SecondBlock, \
    ThirdBlock
from tests.test_runners import BaseTestRunner
from tests.value_provider import ValueProvider


class CreateRequestTestCase(BaseTestRunner):

    def test_offer_details(self):
        category = "Music"
        subject = "Guitar"
        title = "I'd like to become a guitar coach"
        desc = "Prefer focus on standard"
        language = "Ukrainian"
        price = "700"
        question = "What staff do I need?"
        answer = "You need a guitar"
        (HeaderUnauthorizedComponent(self.driver).click_login_btn()
         .set_email(ValueProvider.get_student_email())
         .set_password(ValueProvider.get_student_password())
         .click_login_button())
        (HeaderComponent(self.driver)
         .get_navigate_links()[0]
         .click())
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create request')]").click()
        first_block = FirstBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[1]"))
        first_block.get_category_input().set_text(category)
        first_block.get_category_input().press_down_button(1).press_enter_button()
        first_block.get_subject_input().set_text(subject)
        first_block.get_subject_input().press_down_button(1).press_enter_button()
        first_block.get_checkbox_beginner().set_check()

        second_block = SecondBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[2]"))
        second_block.get_title_input().set_text(title)
        second_block.get_describe_input().set_text(desc)
        second_block.get_language_input().set_text(language)
        second_block.get_language_input().press_down_button(1).press_enter_button()
        second_block.get_price_input().set_text(price)

        third_block = ThirdBlock(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[3]"))
        third_block.get_question_input().set_text(question)
        third_block.set_answer_input_text(answer)
        (OffersRequestModal(self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form"))
         .click_add_to_draft_btn())

        inline_card = OfferDetailsPage(self.driver).get_inline_card_component()
        student_name_expected = (f"{ValueProvider.get_student_first_name()} "
                                 f"{ValueProvider.get_student_last_name()[0]}.")
        student_name_actual = inline_card.get_person_name()
        card_title_actual = inline_card.get_offer_title()
        card_subject_actual = inline_card.get_subject_label()
        card_level_actual = inline_card.get_level_label()
        card_language_actual = inline_card.get_languages()
        card_price_actual = inline_card.get_price_value()
        self.assertEqual(student_name_expected, student_name_actual)
        self.assertEqual(title, card_title_actual)
        self.assertEqual(str.upper(subject), card_subject_actual)
        self.assertEqual(str.upper("Beginner"), card_level_actual)
        self.assertEqual(language, card_language_actual)
        self.assertEqual(f"{price} UAH", card_price_actual)

        general_info_component = OfferDetailsPage(self.driver).get_general_info_component()
        offer_desc_actual = OfferDetailsPage(self.driver).get_about_offer_desc()
        subject_actual = (general_info_component
                          .get_tutoring_subject_component()
                          .get_value())
        level_actual = (general_info_component
                         .get_preparation_levels_component()
                         .get_values()[0]
                         .get_text())
        language_actual = (general_info_component
                         .get_tutoring_languages_component()
                         .get_values()[0]
                         .get_text())
        price_actual = (general_info_component
                         .get_pricing_component()
                         .get_value())
        self.assertEqual(desc, offer_desc_actual)
        self.assertEqual(subject, subject_actual)
        self.assertEqual("Beginner", level_actual)
        self.assertEqual(language, language_actual)
        self.assertEqual(f"{price} UAH/hour", price_actual)

        question_actual = (OfferDetailsPage(self.driver)
                         .get_frequently_asked_questions_component()
                         .get_questions()[0].get_question_text())
        answer_actual = (OfferDetailsPage(self.driver)
                         .get_frequently_asked_questions_component()
                         .get_questions()[0]
                         .click_question_btn()
                         .get_answer())
        self.assertEqual(question, question_actual)
        self.assertEqual(answer, answer_actual)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
