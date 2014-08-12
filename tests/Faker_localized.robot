*** Settings ***
Force Tags        faker
Default Tags      not started
Test Timeout      1 minute

*** Test Cases ***
Import With Locale
    [Tags]    implemented
    Import Library    FakerLibrary    de_DE
    Import Library    FakerLibrary    en_US
    Import Library    FakerLibrary    ko_KR
    Import Library    FakerLibrary    es_MX

Import With Explicit Locale
    [Tags]    implemented
    Import Library    FakerLibrary    locale=de_DE

Import With Explicit Seed
    [Tags]    implemented
    Import Library    FakerLibrary    seed=124

Import With Explicit Locale And Seed
    [Tags]    implemented
    Import Library    FakerLibrary    locale=de_DE    seed=124

Import With Explicit Locale And Seed And No Providers
    [Tags]    implemented
    Import Library    FakerLibrary    locale=de_DE    providers=${None}    seed=124

