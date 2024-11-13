*** Settings ***
Resource  resource.robot
Resource    login.robot
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

# Register With Too Short Username And Valid Password
# # ...

# Register With Valid Username And Too Short Password
# # ...

# Register With Valid Username And Invalid Password
# # salasana ei sisällä halutunlaisia merkkejä
# # ...

# Register With Nonmatching Password And Password Confirmation
# # ...

# Register With Username That Is Already In Use
# #

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

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  heppu  heppu123
    Go To Register Page
