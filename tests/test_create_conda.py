from unittest.mock import call, patch

from conda.python_api import Commands

from create_conda.plugin import create_conda


class TestCreateConda(unittest.TestCase):
    @patch("create_conda.plugin.run_command")
    def test_create_conda_default(self, mock_run_command):
        config = {"general": {"experiment_src_dir": "/path/to/experiment"}}
        result = create_conda(config)
        self.assertEqual(result, config)
        mock_run_command.assert_called_once_with(
            Commands.CREATE,
            "-n",
            "plugin-test",
            "-p",
            "/path/to/experiment/conda/plugin-test",
            "-c",
            "conda-forge",
            "python=3.7",
        )

    @patch("create_conda.plugin.run_command")
    def test_create_conda_custom(self, mock_run_command):
        config = {
            "general": {"experiment_src_dir": "/path/to/experiment"},
            "conda": {
                "name": "custom-env",
                "channels": ["custom-channel"],
                "packages": ["custom-package"],
                "prefix": "/custom/prefix",
            },
        }
        result = create_conda(config)
        self.assertEqual(result, config)
        mock_run_command.assert_called_once_with(
            Commands.CREATE,
            "-n",
            "custom-env",
            "-p",
            "/custom/prefix",
            "-c",
            "custom-channel",
            "custom-package",
        )


if __name__ == "__main__":
    unittest.main()
