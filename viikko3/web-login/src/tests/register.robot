*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kimmo
    Set Password  kimmo123
    Set Password_confirmation  kimmo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ki
    Set Password  kimmo123
    Set Password_confirmation  kimmo123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long and contain only letters a-z

Register With Valid Username And Too Short Password
    Set Username  kimmo
    Set Password  kimmo12
    Set Password_confirmation  kimmo12
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kimmo
    Set Password  kimmokimmo
    Set Password_confirmation  kimmokimmo
    Submit Credentials
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  kimmo
    Set Password  kimmo123
    Set Password_confirmation  kimmo124
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password_confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is already taken

Login After Successful Registration
    Set Username  kalevi
    Set Password  kalevi123
    Set Password_confirmation  kalevi123
    Submit Credentials
    Logout After Successful Registration
    Go To Login Page
    Set Username  kalevi
    Set Password  kalevi123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ka
    Set Password  kalevi123
    Set Password_confirmation  kalevi123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long and contain only letters a-z
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Logout After Successful Registration   
    Welcome Page Should Be Open
    Click Link  Continue to main page
    Click Button  Logout

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page