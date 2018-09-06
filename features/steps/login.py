from behave import*
from selenium import webdriver

@given(u'go to arena homepage')
def step_impl(context):
    context.browser.get('https://arena.jog.ojodowo.com/')
    context.browser.implicitly_wait(10)
    context.browser.find_element_by_xpath("/html/body/div[1]/div/span/div/div[1]/div/div/div[1]")
    context.browser.find_element_by_xpath("/html/body/div[1]/div/span/div/div[2]")
    context.browser.find_element_by_xpath("/html/body/div[1]/div/span/div/div[1]/div/div/div[2]/button[1]").click()

@when(u'login with rizkimahaputra and rizkimahaputra')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/button[2]").click()
    context.browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/span[2]/form")
    context.browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/span[2]/form/div[2]/div[1]/input").send_keys("jogja")
    context.browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/span[2]/form/div[2]/div[2]/input").send_keys("12345678")
    context.browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/span[2]/form/div[4]/button").click()

@then(u'direct to homepage users')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element_by_xpath("/html/body/div[1]/div/header/div[3]/div/button[1]/div")
    context.browser.find_element_by_xpath("/html/body/div[1]/div/span/div/div[1]")

#Scenario: set vip and unset vip
@given(u'go to manage arena page')
def step_impl(context):
    context.browser.get('http://arena.jog.ojodowo.com/arena/manage/')
    context.browser.find_element_by_xpath("/html/body/div[1]/div/span/div/div[2]/div/div/div[1]")

@when(u'click button create vip')
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/div[1]/div/span/div/div[2]/div/div/div[1]/div[1]/div[2]/button").click()

@then(u'create vip popup is shown')
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/div[2]/div/div")

@when(u'user input passkey & clue and click save')
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/form/h3/input[1]").send_keys("12#$abZX")
    context.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/form/h3/input[2]").send_keys("12#$abZX")
    context.browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/form/div/div[2]/button").click()

@then(u'the arena become vip')
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/div[1]/div/span/div/div[2]/div/div/div[1]/div[1]/a/div/div")
