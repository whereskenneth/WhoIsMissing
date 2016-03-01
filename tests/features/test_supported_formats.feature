Feature: Test support for various instrument formats

  Scenario Outline: I have data with different vendor formats with 1 file per injection
    Given an Ascent csv file with minimum required columns
    And it has a full row with {"filename": "1"}
    When I add all injections in the sequence file with a <extension> extension
    Then I should not have any missing injections

  Examples:
  | format      | extension   |
  | dot d       | .D          |
  | dot d       | .d          |
  | mzData      | .mzData.xml |
  | lcd         | .lcd        |
  | wiff        | .wiff       |
  | wiff scan   | .wiff.scan  |
  | raw         | .RAW        |
  | raw         | .raw        |

  Scenario Outline: I am missing a file from my list of injections
    Given an Ascent csv file with minimum required columns
    And it has a full row with {"filename": "1"}
    And it has a full row with {"filename": "2"}
    And it has a full row with {"filename": "3"}
    When I add all injections in the sequence file with a .mzData extension
    And I remove injections <removed injections>
    Then I should have missing injections: <removed injections>

    Examples:
    | removed injections |
    | ['1']              |
    | ['2']              |
    | ['3']              |
    | ['1', '2']         |
    | ['1', '3']         |
    | ['2', '3']         |
    | ['1', '2', '3']    |


  Scenario: Ensure case sensitivity
     Given an Ascent csv file with minimum required columns
    And it has a full row with {"filename": "HECKEL_and_jekyl"}
    When I add all injections in the sequence file with a .mzData extension
    And I remove injections ['HECKEL_and_jekyl']
    Then I should have missing injections: ['HECKEL_and_jekyl']

