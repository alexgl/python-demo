Feature: Test Basic functions of Search

    Scenario Outline: Run Script no args
        Given I run search script with "<args>"
        Then I verify output has "<text>"

        Examples:
            | args                                                        | text                                                              |
            | -u -r lorem -l /Data/SampleInput.txt /Data/SampleInput2.txt | Pellentesque tincidunt accumsan eros, ut varius lorem gravida in. |
            | -u -r lorem -l /Data/SampleInput.txt /Data/SampleInput2.txt | ^^^^^                                                             |
            | -c -r lorem -l /Data/SampleInput.txt /Data/SampleInput2.txt | \x1b[6;30;42mlorem\x1b[0m                                         |
            | -m -r lorem -l /Data/SampleInput.txt /Data/SampleInput2.txt | /Data/SampleInput2.txt:15:48:Pellentesque                         |


         





