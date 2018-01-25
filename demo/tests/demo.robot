*** Settings ***
Suite Setup       Start webapp and open browser
Suite Teardown    Stop webapp and close all browsers
Variables         ../resources/config.py    # this is the only place where we have to hard-code a path;    # when config.py is loaded it will alter the path to include    # the resources folder.
Library           SeleniumLibraryExtension
Library           Process
Library           PageObjectLibrary

*** Variables ***
${BROWSER}        chrome

*** Test Cases ***
Login smoke test
    [Setup]    Go to page    LoginPage
    sleep    1
    Login as a normal user
    The current page should be    HomePage

Login with valid credentials
    [Setup]    Go to page    LoginPage
    Enter username    Demo User
    Enter password    password
    Click the submit button
    The current page should be    HomePage

Login with invalid credentials
    [Setup]    Go to page    LoginPage
    Enter username    Demo User
    Enter password    bogus password
    Click the submit button
    The current page should be    LoginPage

*** Keywords ***
Stop webapp and close all browsers
    Terminate all processes
    Close all browsers

Start webapp and open browser
    start process    python    ${CONFIG.demo_root}/webapp/demoserver.py
    open browser    ${CONFIG.root_url}    ${BROWSER}
