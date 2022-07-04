import yaml


def config_mixing(current_stage: str, config_file: str) -> dict:
    """Mix base config in DEV stage with current stage
    If no current_stage supplied, looks for value in current_stage section
    yaml structure:
            yaml file must be flatten - just one level inside stage
    Minimal configuration of yaml:
            yaml must have at least DEV section
            "DEV" must be declared in current_stage section of yaml

    Returns:
        dictionary: mixed dictionary from DEV section and current_stage section
    """

    with open(config_file, "r") as settings:
        # YAML struct mirrors to dict
        _dict_temp = yaml.load(settings, Loader=yaml.FullLoader)
    current_stage = current_stage or _dict_temp["current_stage"]
    # DEV as base stage, where  all configuration must be defined
    _base_stage: dict = _dict_temp["DEV"]
    # config of current stage
    _current_stage: dict = _dict_temp[current_stage]
    # dict mixing - DEV stage is updated by current stage
    _base_stage |= _current_stage
    return _base_stage
