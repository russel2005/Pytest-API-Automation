import json
import requests
from requests_ntlm import HttpNtlmAuth
import pytest


def get_api_response(api_boomi_url, boomi_payload, auth_credentials):
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    url = api_boomi_url
    NTUSERNAME, NTPASSWORD = auth_credentials
    auth = HttpNtlmAuth(NTUSERNAME, NTPASSWORD)
    headers = {'x-api-key': '86676553-af00-4c80-a0f0-da3c21ad6347', "Content-Type": "application/json"}

    # Convert pr_payload to JSON format
    pr_payload_json = json.dumps(boomi_payload)
    response = requests.post(url, data=pr_payload_json, auth=auth, headers=headers, verify=False)
    return response


@pytest.mark.smoke
def test_verify_success_response_status_code(api_boomi_url, boomi_payload, auth_credentials):
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    response = get_api_response(api_boomi_url, boomi_payload, auth_credentials)
    assert response.status_code == 200
    print("Response status code is 200")


@pytest.mark.smoke
def test_panel_roster_records_not_empty(api_boomi_url, boomi_payload, auth_credentials):
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    response = get_api_response(api_boomi_url, boomi_payload, auth_credentials)
    records = response.json().get("panelRosterRecords", [])
    assert records, "Panel Roster Records is an empty list"
    print("Panel Roster Records is not an empty list")


@pytest.mark.regression
def test_ng_panel_roster_post_request(api_boomi_url, boomi_payload, auth_credentials):
    response = get_api_response(api_boomi_url, boomi_payload, auth_credentials)

    print(f"payload type: {type(boomi_payload)}")
    print(f"Response -Type: {type(response)}" )
    print(f"Response: {response}")
    print(f"Response Status Code: {response.status_code}")

    content_type = response.headers.get('Content-Type', '')
    print("Response Content-Type:", content_type)

    try:
        providers = [record["providerGuid"] for record in response.json()["panelRosterRecords"]]
        unique_providers = set(provider for provider in providers)
        print("Unique provider Values:", unique_providers)

        provider_counts = {}
        for l in providers:
            provider_counts[l] = provider_counts.get(l, 0) + 1

        print(provider_counts)

    except json.JSONDecodeError:
        print("Unable to decode JSON response.")
        assert False, "JSON decoding error"


def test_verify_response_Content_Type_is_correct(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_response_time_is_less_than_10s(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_response_time_is_less_than_10s(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_response_returns_empty_panelRosterRecords_list_when_providerGuid_missing_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Internal_server_error_when_providerGuid_invalid_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_response_returns_empty_panelRosterRecords_list_when_providerGuid_is_empty_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_panelRosterRecords_list_has_all_required_keys_in_response(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_panelRosterRecords_list_have_correct_data_type(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_NGPanelRosterResult_Schema_is_correct(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Bad_request_when_BusinessGuid_missing_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_response_returns_empty_panelRosterRecords_list_when_BusinessGuid_empty_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Bad_request_when_BusinessGuid_invalid_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Unauthorized_when_bearer_token_missing(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Unauthorized_when_traceability_id_missing_in_header(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Unauthorized_when_TIN_missing_in_header(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Forbidden_response_when_invalid_bearer_token_use(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Internal_server_error_when_missing_ROUTEID_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Internal_server_error_when_invalid_ROUTEID_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass


def test_verify_Internal_server_error_when_empty_ROUTEID_in_payload(api_boomi_url, boomi_payload, auth_credentials):
    pass
