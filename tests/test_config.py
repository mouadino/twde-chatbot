from chatbot import config
import os


def test_load_config_from_file():
    del os.environ['HANGOUTS_API_KEY']
    conf = config.Config()

    assert "secret-api-key" == conf.get_value("HANGOUTS_API_KEY")


def test_load_config_from_environment_value():
    os.environ["HANGOUTS_API_KEY"] = "foobar"
    conf = config.Config()

    assert "foobar" == conf.get_value("HANGOUTS_API_KEY")
