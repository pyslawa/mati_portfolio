*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${LOGIN URL}          "https://scouts-test.futbolkolektyw.pl/en"
${BROWSER}      Chrome
${signInButton} =  xpath=//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[1]
${login} =  id=login
${password} =  id=password
${alert} =  xpath=//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[1]