Feature: Contact

  Background:
    Given I am on the contact page

  Scenario: Correct email
    Then I see the email "student.office@example.com"
