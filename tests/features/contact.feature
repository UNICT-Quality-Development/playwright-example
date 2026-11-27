Feature: Contact information

  Background:
    Given I'm on the contact page

  Scenario: View the student office email
    Then the student office email is visible
    And the email is "student.office@example.com"