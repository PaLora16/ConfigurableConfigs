## Configurable configs

********************************

I coined a little bit strange term that expresses fundamentals: In one config file, define separate sections - stages, which can be digested on demand by the app.

In the app development cycle, it is common to have a different configuration for different stages of development.
Understandably, developers seldom use production DB and production infra.
Testers have their environments, too. So it is desirable to have a simple way to hook the actual development stage against a particular config section without heavy reconfiguration.
I figured out a solution for multiple stages in one config file.
Business logic then exposes Config class attributes with constant names but values corresponding given stage.
This way, you can prepare yaml files for all stages in advance and easily let flow project from DEV -> QA -> EDU -> PROD without significant modifications.
For example, testers just modify their stage to "QA" in a yamls current_stage key, and that's all. They can even test apps in combinations of modules for different stages, as the stages are free to comprehend - for example, different environments can be perceived as stages too.
For a real example, I prepared in push_notification_settings.yaml skeleton for iOS push notification service(URL is real - check https://www.mynotifier.app/). For all developers and testers, define their push api key. Changing iOS device belongig to particular guy is peace of cake - just put their name in yaml current_stage.
You can check config usage config usage with stages defined at the app level or simplified use dependent on stages defined in yaml files

Remarks:
- In-app, you can use separate config per module (ConfigPostgreSQL class, ConfigPushIos class ...) or compose config classes into one master config (Config class).
- DEV stage is mandatory in all yamls.
- In DEV stage, define all required keys. In other stages, define just differences against DEV
- Initialization config classes in an application you can define stage ("DEV" "QA"..)
- If no stage is defined, stages are taken from "curent_stage" key of yamls.
- Warning - compose particular module configs, supply module (psg_, push_..)prefixes in yaml keys, keys not to be rewritten in a master config class.




## Instalation

********************************

1. Save downloaded scripts into any folder
2. Cd to script folder

## Run demos

********************************

`py usage.py`  
`py usage_simplified.py`
