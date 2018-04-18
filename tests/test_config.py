from chatbot import config
import os


def test_load_config_from_file():
    if 'HANGOUTS_API_KEY' in os.environ:
        del os.environ['HANGOUTS_API_KEY']
    conf = config.Config()

    assert "secret-api-key" == conf.get_value("hangouts-api-key")


def test_load_config_from_environment_value():
    os.environ["HANGOUTS_API_KEY"] = "foobar"
    conf = config.Config()

    assert "foobar" == conf.get_value("hangouts-api-key")
    del os.environ['HANGOUTS_API_KEY']


def test_uppercase():
    assert 'FOO_BAR' == config.uppercase('foo-bar')
    assert 'FOO_BAR' == config.uppercase('FOO_BAR')
