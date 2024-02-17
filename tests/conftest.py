import pytest
from decouple import config
from pytest_metadata.plugin import metadata_key


@pytest.fixture
def api_url():
    return "https://10.93.110.118/dev/ws/rest/ds11/datahub/v4/NGPanelRosters"


@pytest.fixture
def api_boomi_url():
    return "https://boomi-gateway-dev.dentaquest.com/dev/ws/rest/ds11/datahub/v4/NGPanelRosters"


@pytest.fixture
def pr_payload():
    return {
            "BusinessGUID": "CA0B3A18-97EF-4A76-B4E4-0026FB301BE1",
            "ProviderGuid": "21166ED6-CB94-4325-A1D8-C89EC514741D",
            "ROUTEID": "GOV"
    }


@pytest.fixture
def boomi_payload():
    # "BusinessGUID": "2D3DCEE4-2C31-4CC3-0D6A-E221CF7CAAE6",
    return {

        "ServiceOfficeGuids": "d6de0a12-5ab3-46c9-a450-8037ea29fcdb",
        "ROUTEID": "gov"
    }

@pytest.fixture
def auth_credentials():
    '''
    reading .env file for NT user and password, please create .env file and update with your NT user and password.
    file can be created at project level or test_*.py folder level.
    :return: username : type str
    :return: password : type str
    '''
    # Update with your NTLM credentials
    username = config("NTUSERNAME", default="")
    password = config("NTPASSWORD", default="")
    return username, password


# @pytest.fixture
def pytest_html_report_title(report):
    report.title = "BFF Panel Roster Report"


def pytest_configure(config):
    config.stash[metadata_key]["JAVA_HOME"] = ""


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["<p>BFF API Records</p>"])
