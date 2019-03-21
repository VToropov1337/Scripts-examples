*** Settings ***
Documentation  This is test case
Library  SeleniumLibrary  run_on_failure=Nothing
Library  String
Library  BuiltIn
Library  Collections
Suite Setup  Open Browser    ${mainProject}    ${browser}
Suite Teardown  Close All Browsers

*** Variables ***
${email}  vova@mail.ru
${name}  admin
${password}  123123
${browser}  Chrome
${mainProject}  localhost:3000
${title}  test1
${link}  yandex.ru
${description}  lorem ipsum


*** Keywords ***
Open a login page
	Maximize Browser Window
	Title Should be  Muse

Click to sign up
	Click Link    //*[contains(text(),"Sign Up")]
	Wait Until Element Is Visible    //*[contains(text(),"Log in")]
	Input Text    //*[@id="user_email"]  ${email}
	Input Text    //*[@id="user_name"]  ${name}
	Input Text    //*[@id="user_password"]  ${password}
	Input Text    //*[@id="user_password_confirmation"]  ${password}
	Click Button  //*[@value="Sign up"]
	Page Should Contain Element  //div[contains(@class,"error")]
	Click Link  //*[@href="/users/sign_in"]

Logging in
	Input Text    //*[@id="user_email"]  ${email}
	Input Text    //*[@id="user_password"]  ${password}
	Click Button  //*[@name="commit"]



*** Test Cases ***
Open a page
	Open a login page

Create a dublicate user
	Click to sign up
#
#Logging
##	Click Link  //*[@href="/users/sign_in"]
#	Logging in

Log like unique user
	Logging in
	Wait Until Element Is Visible  //*[contains(text(),"Signed in successfully.")]
	Page Should Contain Element  //*[@id="posts"]
	Click Link  //*[@href="/posts/new"]
	Wait Until Page Contains  Add new inspiration


Create a post
	Click Link  //*[@href="/posts/new"]
	Input Text  //*[@id="post_title"]  ${title}
	Input Text  //*[@id="post_link"]  ${link}
	Input Text  //*[@id="post_description"]  ${description}
	Click Button  //*[@value="Create Post"]
	Click Link  //*[@href="/"]
	Log To Console      Display to console while Robot is running



##For-Loop-In-Range
#    : FOR    ${INDEX}    IN RANGE 1  10
#    \    Log To Console  '===='
#    \    Log To Console    ${INDEX}
#    \    ${RANDOM_STRING}=    Generate Random String    ${INDEX}
#    \    Log To Console    ${RANDOM_STRING}


Like post
	Page Should Contain Element  //*[@id="posts"]
	${count}=  Get Element Count  //*[@id="posts"]/*
    :FOR    ${i}  IN RANGE  1  ${count}+1
	\  Click Link  //*[@href="/posts/${i}"]
	\  Wait Until Element Is Visible  //*[@href="/posts/${i}/like"]
	\  Click Link  //*[@href="/posts/${i}/like"]
	\  Click Link  //*[@href="/"]
    \  Log To Console    ${i}
    \  Log To Console   ====