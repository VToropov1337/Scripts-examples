*** Settings ***
Documentation  Simple example using SeleniumLibrary
Library  SeleniumLibrary


*** Variables ***
${url}  https://www.avito.ru/moskva#login?s=h
${browser}  Chrome


*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Email  ***
    Input Password  ***
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]  Close Browser



*** Keywords ***
Open Browser To Login Page
    Open Browser    ${url}    ${browser}
    Title Should Be    Авито — объявления в Москве


Input Email
    [Arguments]  ${email}
    Input Text  login   ${email}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    login

Welcome Page Should Be Open
    Title Should Be    Авито — объявления в Москве