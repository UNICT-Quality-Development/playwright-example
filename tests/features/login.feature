Feature: Login

  Scenario: Successful login
    Given I am on the login page
    When I log in as "mario" with password "password123"
    Then I see the greeting "Welcome, Mario"
