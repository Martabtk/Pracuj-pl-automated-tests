import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

value = "qwerty"
email = "testcom"

class Pracuj_plTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.pracuj.pl")
        cookie_accept = self.driver.find_element(By.CSS_SELECTOR, 'button[data-test="button-submitCookie"]')
        cookie_accept.click()
        sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_demo_first_page(self):
        title = self.driver.title
        print(title)
        assert "Praca - Pracuj.pl" == title

    def test_button_click(self):
        button = self.driver.find_element(By.CSS_SELECTOR, 'button.size-large.variant-primary.core_b1fqykql')
        assert button.is_displayed()
        button.click()
        # Tutaj możesz dodać dalsze asercje lub akcje po kliknięciu przycisku

    def test_job_search(self):
        label_element = self.driver.find_element(By.XPATH, '//label[text()="Stanowisko, firma, słowo kluczowe"]')
        input_element = label_element.find_element(By.XPATH, './../input')
        input_element.send_keys("Tester")
        sleep(5)

        category_button = self.driver.find_element(By.XPATH, '//label[text()="Kategoria"]/following-sibling::span')
        self.driver.execute_script("arguments[0].click();", category_button)

        category_it = self.driver.find_element(By.CSS_SELECTOR, 'div[data-test="select-option-5016"]')
        category_it.click()
        search_button = self.driver.find_element(By.XPATH,
                                                 '//button[@class="size-large variant-primary core_b1fqykql"]')
        if search_button.is_displayed() and search_button.is_enabled():
            self.driver.execute_script("arguments[0].click();", search_button)
            sleep(5)

        internship_option = self.driver.find_element(By.XPATH, '//div[@data-test="select-option-1"]')
        internship_option.click()

        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button.size-large.variant-primary.core_b1fqykql')
        search_button.click()

        results_element = self.driver.find_element(By.CLASS_NAME, 'listing_juh9ikv')
        jobs_count_text = results_element.text
        jobs_count = int(jobs_count_text.split()[0])
        print(f"Liczba znalezionych ofert pracy: {jobs_count}")


def test_aregister_account(self, NoSuchElementException=None):

        button = self.driver.find_element(By.CSS_SELECTOR,
                                          'div[data-test="section-my-account-desktop-button"].header_b1uyf0zv')
        button.click()

        register_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="button-sign-up"].header_b1fqykql')
        register_link.click()
        sleep(2)
        # Wyszukaj pole adresu e-mail i wpisz niepoprawny adres
        email_input = self.driver.find_element(By.CSS_SELECTOR, 'input[data-test="input-email"]')
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[data-test="input-password"]')
        password_input.send_keys("qwerty")
        sleep(3)

        # Sprawdź wyświetlanie komunikatu pod polem adresu e-mail
        try:
            error_message = self.driver.find_element(By.CSS_SELECTOR, '.form-control__error')

            if error_message.is_displayed():
                error_text = error_message.text
                expected_error_text = 'Uwzględnij znak "@" w adresie e-mail. W adresie "{email}" brakuje znaku "@"'
                if error_text == expected_error_text:
                    print("Wiadomość o błędzie jest wyświetlona i zgadza się z oczekiwanym tekstem.")
                else:
                    print("Wiadomość o błędzie jest wyświetlona, ale nie zgadza się z oczekiwanym tekstem.")
                    print(f"Aktualny tekst wiadomości o błędzie: {error_text}")
            else:
                print("Wiadomość o błędzie nie jest wyświetlona.")
        except NoSuchElementException:
            print("Wiadomość o błędzie nie jest wyświetlona.")


if __name__ == '__main__':
    unittest.main()

