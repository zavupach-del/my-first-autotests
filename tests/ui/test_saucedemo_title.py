import pytest
from playwright.sync_api import expect

@pytest.mark.ui
def test_saucedemo_title(page):
    page.goto("https://www.saucedemo.com/")
    # Обязательно используем expect, а не assert!
    expect(page).to_have_title("Swag Labs")