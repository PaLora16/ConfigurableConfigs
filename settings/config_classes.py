from .config_mixing import config_mixing


class ConfigPostgreSQL:
    def __init__(self, stage: str = None):
        # update class dict thus exposing class attributes referencig to YAML keys
        self.__dict__.update(config_mixing(
            stage, "settings/postgreSQL_settings.yaml"))


class ConfigPushiOS:
    def __init__(self, stage: str = None):
        # update class dict thus exposing class attributes referencig to YAML keys
        self.__dict__.update(
            config_mixing(stage, "settings/push_notification_settings.yaml")
        )


class Config(ConfigPostgreSQL, ConfigPushiOS):
    def __init__(self, stage: str = None):
        ConfigPushiOS.__init__(self, stage)
        ConfigPostgreSQL.__init__(self, stage)
