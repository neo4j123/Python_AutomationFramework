class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_linkText = "Logout"

    def do_logout(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
        self.driver.find_element_by_link_text(self.logout_linkText).click()