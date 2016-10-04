from testinfra.utils.ansible_runner import AnsibleRunner

runner = AnsibleRunner('.molecule/ansible_inventory')
runner.options.connection = 'docker'

testinfra_hosts = runner.get_hosts('apt_madison')


def test_apt_madison(TestinfraBackend, Command):

    target = TestinfraBackend.get_hostname()
    expected_version = Command("dpkg -l | grep apt | head -n 1 | awk '{ print $3}'")

    p = runner.run(target, 'apt_madison', 'name=apt', check=False)

    assert p['versions'][0]['name'] == 'apt'
    assert p['versions'][0]['version'] == expected_version.stdout.strip()
