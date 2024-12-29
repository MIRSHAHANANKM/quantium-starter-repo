import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def app_runner():
    return import_app('task4')

def test_visualization_present(dash_duo, app_runner):
    dash_duo.start_server(app_runner)

    # Check if the line chart is present
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None

def test_region_picker_present(dash_duo, app_runner):
    dash_duo.start_server(app_runner)

    # Check if the radio button group is present
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None
