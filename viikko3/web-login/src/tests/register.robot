*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Fail With Message  Length of username must be at least 3

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  ville12
    Set Password Confirmation  ville12
    Submit Credentials
    Register Should Fail With Message  Length of password must be at least 8

Register With Valid Username And Invalid Password
    # salasana ei sisällä halutunlaisia merkkejä
    Set Username  ville
    Set Password  villeville
    Set Password Confirmation  villeville
    Submit Credentials
    Register Should Fail With Message  Password can't consist of only regular characters a-z or A-Z

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville1234
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation don't match

Register With Username That Is Already In Use
    Set Username  heppu
    Set Password  heppu123
    Set Password Confirmation  heppu123
    Submit Credentials
    Register Should Fail With Message  Username already exists

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  heppu  heppu123
    Go To Register Page
