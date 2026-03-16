from app import app
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = str(Path(__file__).resolve().parent / "chromedriver.exe")
import pytest

@pytest.fixture
def chrome_driver():
    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods Pink Morsel Sales Visualiser" in header.text


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None