from testinfra.utils.ansible_runner import AnsibleRunner

runner = AnsibleRunner('.molecule/ansible_inventory')
runner.options.connection = 'docker'

testinfra_hosts = runner.get_hosts('yum_madison')


def test_yum_madison(TestinfraBackend, Command):

    target = TestinfraBackend.get_hostname()
    expected_version = Command("yum list | grep sudo | head -n 1 | awk '{ print $2'}")

    p = runner.run(target, 'yum_madison', 'name=sudo', check=False)

    assert p['versions'][0]['name'] == 'sudo'
    assert p['versions'][0]['version'] == expected_version.stdout.strip()
