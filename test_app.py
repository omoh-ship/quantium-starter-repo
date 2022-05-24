from app import app
# from dash.testing.application_runners import import_app
# from selenium import webdriver

# driver = webdriver.Chrome('C:/DevTools/chromedriver.exe')


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#header', timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#graph', timeout=10)


def test_region_selecter_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#radio_options', timeout=10)

