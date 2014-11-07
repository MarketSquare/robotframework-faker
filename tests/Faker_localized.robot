*** Settings ***
Force Tags        faker
Test Timeout      1 minute

*** Test Cases ***
Import With Locale
    Import Library    FakerLibrary    de_DE
    Import Library    FakerLibrary    en_US
    Import Library    FakerLibrary    ko_KR
    Import Library    FakerLibrary    es_MX

Import With Explicit Locale
    Import Library    FakerLibrary    locale=de_DE

Import With Explicit Seed
    Import Library    FakerLibrary    seed=124

Import With Explicit Locale And Seed
    Import Library    FakerLibrary    locale=de_DE    seed=124

Import With Explicit Locale And Seed And No Providers
    Import Library    FakerLibrary    locale=de_DE    providers=${None}    seed=124
