import os
import pytest
from playwright.sync_api import expect
from dotenv import load_dotenv
from pages.login_page import LoginPage

# Загружаем переменные из .env файла
load_dotenv()


@pytest.mark.ui
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.open()
    
    # Используем os.getenv с дефолтным значением (для страховки)
    username = os.getenv("SAUCE_USER", "standard_user")
    password = os.getenv("SAUCE_PASS", "secret_sauce")
    
    login_page.login(username, password)

    # Проверяем, что URL изменился на /inventory.html
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.ui
def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.open()
    
    password = os.getenv("SAUCE_PASS", "secret_sauce")
    login_page.login("locked_out_user", password)

    # Проверяем, что виден текст ошибки о блокировке
    expect(login_page.error_message).to_contain_text(
        "Epic sadface: Sorry, this user has been locked out."
    )