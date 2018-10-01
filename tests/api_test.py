from grapi.grapi import Grapi


def test_get():
    api = Grapi("http://echo.jsontest.com/one/two", "l3fkjh345ksdfjll345")
    result = api._get()
    expected = "{\"one\": \"two\"}\n"
    assert result.text == expected

# TODO: Write tests for all the things
