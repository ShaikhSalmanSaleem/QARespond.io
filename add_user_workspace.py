import time
from behave import given, when, then
from selenium.webdriver.common.by import By

driver = None  # Define the driver variable as global

@given('the user is logged in and on the user management page')
def step_impl(context):
    # Implement login steps here
    context.execute_steps('''
        Given the user is on the login page
        When the user enters valid username "admin" and password "adminpass"
        And the user clicks the login button
    ''')
    context.driver.get("https://app.respond.io/space/241293/settings/users")

@when('the user clicks the add user button')
def step_impl(context):
    global driver  # Access the global driver variable
    adduser_button = driver.find_element(By.XPATH,"//div[@id='root']/div/div/div/nav/div/div/a[7]/div[2]/div/div/i")
    adduser_button.click()

@when('the user enters new username "{username}" and email "{email}"')
def step_impl(context, username, user_email):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys(user_email)
    #context.driver.find_element_by_id("new-email").send_keys(email)

@when('the user submits the new user form')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//button)[56]").click()

@then('the new user should be added successfully')
def step_impl(context):
    success_message = context.driver.find_element_by_id("user-added-success")
    assert success_message.is_displayed()