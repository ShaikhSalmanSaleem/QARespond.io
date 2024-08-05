from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the login page')
def step_impl(context):
    context.driver.get("https://app.respond.io/user/login")

@when('the user enters valid username "{Email}" and password "{password}"')
def step_impl(context, Email, password):
    context.driver.find_element(By.NAME, "field_2").send_keys(Email)
    context.driver.find_element(By.NAME, "field_3").send_keys(password)

@when('the user clicks the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

@then('the user should be redirected to the dashboard')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "dashboard"))
    )
    assert context.driver.find_element(By.ID, "dashboard").is_displayed()

@then('the user should see an error message')
def step_impl(context):
    error_message = context.driver.find_element(By.ID, "error-message")
    assert error_message.is_displayed()