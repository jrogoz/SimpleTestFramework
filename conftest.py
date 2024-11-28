import pytest
import webbrowser
from pathlib import Path


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """
    Automatic opening of the generated report configuration
    """

    report_path = Path("reports/report.html")
    if report_path.exists():
        webbrowser.open_new_tab(report_path.absolute().as_uri())


