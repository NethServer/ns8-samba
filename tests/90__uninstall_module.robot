*** Settings ***
Resource    keywords.resource

*** Test Cases ***
Remove the modules from the cluster
    [Tags]    remove    instance
    Remove a module instance    ${MID1}
