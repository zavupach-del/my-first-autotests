import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

@pytest.mark.ui
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    # Проверяем, что URL изменился на /inventory.html
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.ui
def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    
    # Проверяем, что виден текст ошибки о блокировке
    expect(login_page.error_message).to_contain_text("Epic sadface: Sorry, this user has been locked out.")