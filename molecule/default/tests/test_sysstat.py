import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_sysstat_installed(host):
    sysstat_package_name = "sysstat"
    assert host.package(sysstat_package_name).is_installed


def test_lm_sensors_installed(host):
    lm_sensor_package_name = _get_lm_sensor_package_name(
        host.system_info.distribution)
    assert host.package(lm_sensor_package_name).is_installed


def test_sysstat_service(host):
    sysstat_service_name = "sysstat"
    service = host.service(sysstat_service_name)
    assert service.is_running
    assert service.is_enabled


def _get_lm_sensor_package_name(host_distro):
    return {
        "debian": "lm-sensors",
        "centos": "lm_sensors"
    }.get(host_distro, "lm-sensors")
