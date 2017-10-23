import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory.yml').get_hosts('apt_madison')


def test_apt_madison(host):

    expected_version = host.run("dpkg -l | grep apt | head -n 1 | awk '{ print $3}'")

    p = host.ansible('apt_madison', 'name=apt', check=False)
    assert p['versions'][0]['name'] == 'apt'
    assert p['versions'][0]['version'] == expected_version.stdout.strip()
