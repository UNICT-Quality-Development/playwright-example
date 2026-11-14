Feature: StudentId

  # Background:

  Scenario: Correct student id
    Given I log in as "mario" with password "password123"
    When I goto profile page
    Then I see the student ID "1000012345"

  Scenario: Wrong student id
    Given I log in as "luigi" with password "password123"
    When I goto profile page
		Then I cannot enter profile page
    And I do not see any student ID
