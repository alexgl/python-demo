Feature: Test Basic functions of Search

    Scenario Outline: Run Script no args
        Given I run search script with "<args>"
        Then I verify output has "<text>"

        Examples:
            | args                                                        | text                                                              |
            | -u -r lorem -l /Data/SampleInput.txt /Data/SampleInput2.txt | Pellentesque tincidunt accumsan eros, ut varius lorem gravida in. |
            | -u -r lorem -l /Data/SampleInput.txt /Data/SampleInput2.txt | ^^^^^                                                             |


