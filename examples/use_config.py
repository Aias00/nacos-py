from nacos_py_client import NacosClient

client = NacosClient(
    server_addresses="http://172.16.21.45:11047",
    username="nacos",
    password="GFJ5l$*]B@+;jI'5"
)

# publish config
client.config.publish("test_config", "DEFAULT_GROUP", "test_value", "dcup")

# get config
assert client.config.get("test_config", "DEFAULT_GROUP") == "test_value"

# get config with default value
assert client.config.get(
    "test_config_miss", "DEFAULT_GROUP", default="default_value"
) == "default_value"


# subscribe config

def config_update(config):
    print(config)


client.config.subscribe(
    "test_config",
    "DEFAULT_GROUP",
    callback=config_update
)
