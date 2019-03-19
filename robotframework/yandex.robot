*** Settings ***
Library  SeleniumLibrary
Suite Setup    Open a yandex page
Suite Teardown  Close All Browsers

*** Variables ***
${url}  https://yandex.ru
${browser}  Chrome


*** Test Cases ***
blablabla
    Open a yandex page
    Search and check    Russia  Москва
    Search and check    Spain   Барселона
    Search and check    France  Париж



*** Keywords ***
Open a yandex page
    Open Browser    ${url}    ${browser}

Search and check
    [Arguments]  ${query}   ${expected result}
    Input text  //span[class="input__ahead"]/*   ${query}
    Click button    type="submit"    ${query}
    Wait until page contains    ${expected result}





