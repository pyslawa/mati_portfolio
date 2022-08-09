*** Settings ***
Library  SeleniumLibrary
Documentation    Suite description #automated tests for scout website


*** Variables ***
${LOGIN URL}      https://scouts-test.futbolkolektyw.pl/en
${BROWSER}        Chrome
${SIGNINBUTTON}   xpath=//*[(text()= 'Sign in')]
${EMAILINPUT}   xpath=//*[@id='login']
${PASSWORDINPUT}    xpath=//*[@id='password']
${PAGELOGO}    xpath=//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[1]

*** Test Cases ***
Login to the system
    Open login page
    Type in email
    Type in password
    Click on the Submit button
    Assert dashboard
    [Teardown]  Close Browser

Log out of the system
    Open login page
    Type in email
    Type in password
    Click on the Submit button
    Assert dashboard
    Test step 1
    Test step 2
    [Teardown]  Close Browser

*** Keywords ***
Open login page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be     Scouts panel - sign in
Type in email
#    wait until element is visible   ${EMAILINPUT}
    Input Text   ${EMAILINPUT}   user07@getnada.com
Type in password
#    wait until element is visible   id=password
    Input Text  id=password  Test-1234
Click on the Submit button
    Click Element   xpath=//*[(text()= 'Sign in')]
Assert dashboard
    wait until element is visible   ${PAGELOGO}
    title should be     Scouts panel
    Capture Page Screenshot  alert.png
