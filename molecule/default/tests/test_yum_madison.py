import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory.yml').get_hosts('yum_madison')


def test_yum_madison(host):

    expected_version = host.run("yum list | grep sudo | head -n 1 | awk '{ print $2'}")

    p = host.ansible('yum_madison', 'name=sudo', check=False)
    assert p['versions'][0]['name'] == 'sudo'
    assert p['versions'][0]['version'] == expected_version.stdout.strip()
