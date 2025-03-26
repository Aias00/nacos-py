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
