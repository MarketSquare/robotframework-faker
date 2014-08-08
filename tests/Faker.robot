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
    FakerLibrary.Seed    5

Can call Words with integer argument
    [Tags]    implemented
    ${WordsList}=    Words    nb=10
    Log    ${WordsList}
