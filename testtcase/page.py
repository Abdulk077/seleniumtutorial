from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"
    
class BasePage(object):
    def __int__(self,driver):
        self.driver = driver


class Mainpage(BasePage):
    search_text_element = SearchTextElement()
    
    def is_title_matches(self):
        """

        :rtype: object
        """
        return "Python" in self.driver.title
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocator.G0_BUTTON)
        element.click()

class SearchResultPage(BasePage):
    def is_results_found(self):
        return " No result found ." not in self.driver.page_source
    
