import pytest


@pytest.mark.parametrize(
    "username,password,expected_result",
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            "qa.ajax.app.automation@gmail.com",
            id="Email equals to username",
        ),
    ],
)
def test_settings(username, password, expected_result, user_login_fixture):
    lp = user_login_fixture
    email = lp.sidebar_settings(username=username, password=password)
    assert email == expected_result
