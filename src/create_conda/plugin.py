from conda.python_api import Commands, run_command


def create_conda_env(config):
    """Create a conda environment with the given configuration."""
    conda_config = config.get("conda", {})
    env_name = conda_config.get("name", "plugin-test")
    channels = [
        f"-c {channel_name}"
        for channel_name in conda_config.get("channels", ["conda-forge"])
    ]
    packages = conda_config.get("packages", ["python=3.7"])
    prefix = conda_config.get(
        "prefix", f"{config['general']['experiment_src_dir']}/conda/{env_name}"
    )
    run_command(Commands.CREATE, "-n", env_name, "-p", prefix, *channels, *packages)
    return config
