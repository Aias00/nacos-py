# nacos-py-client

<a href="https://github.com/Aias00/nacos-py/actions/workflows/test.yml?query=event%3Apush+branch%3Amain" target="_blank">
    <img src="https://github.com/Aias00/nacos-py/actions/workflows/test.yml/badge.svg?branch=main&event=push" alt="Test">
</a>
<a href="https://pypi.org/project/nacos-py-client" target="_blank">
    <img src="https://img.shields.io/pypi/v/nacos-py-client.svg" alt="Package version">
</a>

<a href="https://pypi.org/project/nacos-py-client" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/nacos-py-client.svg" alt="Supported Python versions">
</a>

A python nacos client based on the official [open-api](https://nacos.io/zh-cn/docs/open-api.html).

## install

```shell
pip install nacos-py-client
```

## usage

### config

```python
from nacos_py_client import NacosClient

client = NacosClient(...)

# publish config
client.config.publish("test_config", "DEFAULT_GROUP", "test_value")
# get config
assert client.config.get("test_config", "DEFAULT_GROUP", "namespaceId") == "test_value"


# subscribe config

def config_update(config):
    print(config)


client.config.subscribe(
    "test_config",
    "DEFAULT_GROUP",
    "namespaceId",
    callback=config_update
)
```

### instance

```python
from nacos_py_client import NacosClient

nacos = NacosClient()

nacos.instance.register(
    service_name="test",
    ip="10.10.10.10",
    port=8000,
    weight=10.0
)

nacos.instance.heartbeat(
    service_name="test",
    ip="10.10.10.10",
    port=8000,
)
```

### 😘support `async` mode

```python
# example: fastapi

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from nacos_py_client import NacosAsyncClient


def config_update(config):
    print(config)


@asynccontextmanager
async def lifespan(app: FastAPI):
    nacos = NacosAsyncClient()

    config_subscriber = await nacos.config.subscribe(
        data_id="test-config",
        group="DEFAULT_GROUP",
        callback=config_update,
    )
    yield
    config_subscriber.cancel()


app = FastAPI(lifespan=lifespan)

if __name__ == '__main__':
    uvicorn.run("in_fastapi:app", host="0.0.0.0", port=1081)
```

## Developing

```text
make install  # Run `poetry install`
make lint  # Runs bandit and black in check mode
make format  # Formats you code with Black
make test  # run pytest with coverage
make publish  # run `poetry publish --build` to build source and wheel package and publish to pypi
```