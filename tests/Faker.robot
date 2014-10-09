*** Settings ***
Force Tags        faker
Default Tags      not started
Test Timeout      1 minute
Library           FakerLibrary

*** Test Cases ***
Can Get Fake Name
    [Tags]    implemented
    ${name}=    FakerLibrary.Name
    Should Not Be Empty    ${name}

Two Calls To Faker Should Give Different Results
    [Tags]    implemented
    ${name}=    FakerLibrary.Name
    Should Not Be Empty    ${name}
    ${name2}=    FakerLibrary.Name
    Should Not Be Empty    ${name2}
    Should Not Be Equal As Strings    ${name}    ${name2}

Can Seed Faker
    [Tags]    implemented
    FakerLibrary.Seed    ${5}

Can call Words with integer argument
    [Tags]    implemented
    ${WordsList}=    Words    nb=${10}
    Log    ${WordsList}

Can call SHA-1
    [Tags]    implemented
    SHA1
    SHA1    ${True}
    SHA1    ${False}

Can call Password
    [Tags]    implemented
    Password
    Password    ${5}
    Password    special_chars=${False}
    Password    special_chars=${True}
    Password    digits=${True}
    Password    digits=${False}
    Password    upper_case=${True}
    Password    lower_case=${True}
    Password    digits=${False}
    Password    ${5823}    ${True}    ${False}    ${True}    ${True}
