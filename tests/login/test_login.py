import pytest


@pytest.mark.parametrize(
    "username,password,expected_result",
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            True,
            id="Correct username and password",
        ),
        pytest.param(
            "invalid_username",
            "qa_automation_password",
            False,
            id="Incorrect username",
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "invalid_password",
            False,
            id="Incorrect password",
        ),
        pytest.param(
            "",
            "",
            False,
            id="Empty fields",
        ),
    ],
)
def test_user_login(username, password, expected_result, user_login_fixture):
    lp = user_login_fixture
    result = lp.login(
        username=username,
        password=password
    )
    assert result is expected_result
