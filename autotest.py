import os
import pytest
from selene import browser, be, have

url = "file://" + os.path.abspath("Login.html")

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.open(url)
    yield


def test_successful_login():
    browser.element('[name="username"]').type('admin')
    browser.element('[name="password"]').type('1234567890').press_enter()
    browser.element('[id="message"]').should(have.text('Login successful!'))


def test_successful_login_with_enter():
    browser.element('[name="username"]').type('admin')
    browser.element('[name="password"]').type('1234567890').press_enter()
    browser.element('[id="message"]').should(have.text('Login successful!'))


def test_unsuccessful_login():
    browser.element('[name="username"]').type('wronguser')
    browser.element('[name="password"]').type('wrongpass').press_enter()
    browser.element('[id="message"]').should(have.text('Invalid username or password'))


def test_successful_logout():
    browser.element('[name="username"]').type('admin')
    browser.element('[name="password"]').type('1234567890').press_enter()
    browser.element('[id="message"]').should(have.text('Login successful!'))
    browser.element('button[id="logout-btn"]').click()
    browser.element('[id="message"]').should(have.text('You have been logged out.'))

def test_negative_login_password():
    browser.element('[name="username"]').type('admins')
    browser.element('[name="password"]').type('12345').press_enter()
    browser.element('[id="message"]').should(have.text('Password must be at least 6 characters'))

def test_negative_logout_latin():
    browser.element('[name="username"]').type('Привет')
    browser.element('[name="password"]').type('<PASSWORD>').press_enter()
    browser.element('[id="message"]').should(have.text('Username must contain only Latin letters'))

def test_nothing_pressed():
    browser.element('button[type="submit"]').click()
    browser.element('[id="message"]').should(have.text('Please enter both username and password'))
