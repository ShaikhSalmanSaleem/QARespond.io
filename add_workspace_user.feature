Feature: Add Workspace User Functionality

  Scenario: Successfully add a new workspace user
    Given the user is logged in and on the user management page
    When the user clicks the add user button
    And the user enters new username "SQA USER" and email "abc123@yopmail.com"
    And the user submits the new user form
    Then the new user should be added successfully  
      