*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Suite Setup    Open a localhost page


*** Test Cases ***
Create a new member
	Click to sign up
	Waiting time
	Enter email
	Enter password
	Enter confirmation password
	Accept
	[Teardown]  Close Browser


Login like admin
	Open a localhost page
	Click to sign in
	Waiting time
	Input Text    //*[@id="user_email"]    admin2222@mail.ru
	Enter password
	Accept
	Page Should Contain Element    //*[@class="alert"]    "Invalid Email or password."
	[Teardown]  Close Browser

Forgot password
	Open a localhost page
	Click to sign in
	Waiting time
	Forgot password
	[Teardown]  Close Browser


Posting a message
	Open a localhost page
	Click to sign in
	Waiting time
	Input Text    //*[@id="user_email"]   vladimir@mail.ru
	Input Text    //*[@id="user_password"]   123456
	Accept
	Page Should Contain Element    //*[@class="notice"]    Signed in successfully.
	[Teardown]  Close Browser


*** Keywords ***
Open a localhost page
	Open Browser    ${url}    ${browser}


Click to sign up
	Click Link    //*[contains(text(),"Sign Up")]

Waiting time
	Wait Until Element Is Visible    //*[contains(text(),"Log in")]


Enter email
	Input Text    //*[@id="user_email"]   vladimir@mail.ru

Enter password
	Input Text    //*[@id="user_password"]   123456

Forgot password
	Click Link    //*[@href="/users/password/new"]

Enter confirmation password
	Input Text    //*[@id="user_password_confirmation"]   123456

Accept
	Click Button    //*[@class="actions"]/*

Click to sign in
    Click Link    //*[@id="buttons"]/a[2]


*** Variables ***
${url}  http://localhost:3000/
${browser}  Chrome