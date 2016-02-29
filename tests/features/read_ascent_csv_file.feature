Feature: I can read an Ascent csv and check it for validity

  Scenario: I can create and read an Ascent csv file
    Given an Ascent csv file with columns ['name', 'filename', 'dilution_factor', 'type', 'assay', 'instrument', 'ascentid']
    Then I should be able to instantiate my class

  Scenario: I get an exception when the sequence file does not contain all the required columns
    Given an Ascent csv file with columns ['name']
    Then I should get an InvalidAscentCsvException
