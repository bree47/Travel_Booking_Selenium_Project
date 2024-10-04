import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class TravelBookingAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://travel.agileway.net/login"

    def launch_browser(self):
        """Launch the browser and navigate to the travel booking site."""
        self.driver.get(self.url)

    def login(self, username, password):
        """Login with provided credentials."""
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "commit").click()

    def select_flight_details(self, from_index, to_index, depart_day, depart_month, return_day, return_month):
        """Select flight details including origin, destination, and travel dates."""
        originDropDown = self.driver.find_element(By.NAME, "fromPort")
        Select(originDropDown).select_by_index(from_index)

        destinationDropDown = self.driver.find_element(By.NAME, "toPort")
        Select(destinationDropDown).select_by_index(to_index)

        self.driver.find_element(By.NAME, "departDay").send_keys(depart_day)
        self.driver.find_element(By.NAME, "departMonth").send_keys(depart_month)
        self.driver.find_element(By.NAME, "returnDay").send_keys(return_day)
        self.driver.find_element(By.NAME, "returnMonth").send_keys(return_month)

    def select_flight(self):
        """Select the flight."""
        self.driver.find_elements(By.XPATH, "//*[@id='flights']/tbody/tr[2]/th/input")[0].click()
        self.driver.find_element(By.XPATH, "//*[@id='container']/form/input").click()

    def enter_passenger_details(self, first_name, last_name):
        """Enter passenger details."""
        self.driver.find_element(By.NAME, "passengerFirstName").send_keys(first_name)
        self.driver.find_element(By.NAME, "passengerLastName").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//*[@id='container']/form/input[3]").click()

    def enter_payment_details(self, card_type_index, card_number, expiry_month, expiry_year):
        """Enter payment details."""
        self.driver.find_elements(By.XPATH, "//input[@name='card_type']")[card_type_index].click()
        self.driver.find_element(By.NAME, "card_number").send_keys(card_number)
        self.driver.find_element(By.NAME, "expiry_month").send_keys(expiry_month)
        self.driver.find_element(By.NAME, "expiry_year").send_keys(expiry_year)
        self.driver.find_elements(By.XPATH, "//*[@id='payment-form']/p/input")[0].click()

    def complete_booking(self):
        """Wait for the booking to complete."""
        time.sleep(7)


@pytest.mark.usefixtures("init_driver")
class TestTravelBookingAutomation:
    def setup_method(self):
        """Set up the test."""
        self.travel_booking = TravelBookingAutomation(self.driver)

    def test_travel_booking(self):
        """Test case for booking a flight."""
        # Step 1: Launch browser and navigate to the site
        self.travel_booking.launch_browser()

        # Step 2: Login
        self.travel_booking.login("agileway", "testwise")

        # Step 3: Select flight details
        self.travel_booking.select_flight_details(2, 1, "12", "May 2025", "28", "May 2025")

        # Step 4: Select a flight
        self.travel_booking.select_flight()

        # Step 5: Enter passenger details
        self.travel_booking.enter_passenger_details("Fake", "Person")

        # Step 6: Enter payment details
        self.travel_booking.enter_payment_details(1, "12345", "08", "2026")

        # Step 7: Complete the booking
        self.travel_booking.complete_booking()
