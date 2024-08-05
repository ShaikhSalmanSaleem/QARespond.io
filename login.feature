Feature: Login Functionality

  Scenario: Failed login with invalid credentials
    Given the user is on the login page
    When the user enters invalid username "wronguser" and password "wrongpass"
    And the user clicks the login button
    Then the user should see an error message  
  
  
  
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid username "qaks724@gmail.com" and password "Audio@1234"
    And the user clicks the login button
    Then the user should be redirected to the dashboard

  