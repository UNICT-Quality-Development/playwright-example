Feature: Login

  Background:
    Given I am on the login page

  Scenario: Successful login
    When I log in as "mario" with password "password123"
    Then I see the greeting "Welcome, Mario"

  Scenario: Wrong password
    When I log in as "mario" with password "wrong"
    Then I see the error "Invalid username or password"

  Scenario: Unknown user
    When I log in as "luigi" with password "password123"
    Then I see the error "Invalid username or password"
