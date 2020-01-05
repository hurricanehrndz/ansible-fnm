import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nodejs(host):
    f = host.file('/home/testuser/.local/share/fnm/aliases/default/bin/node')

    assert f.exists
    assert f.user == 'testuser'
    assert f.group == 'testuser'
    assert f.mode == 0o755


def test_npm_neovim_pkg(host):
    f = host.file(
      '/home/testuser/.local/share/fnm/aliases/default/bin/neovim-node-host'
    )

    assert f.exists
    assert f.user == 'testuser'
    assert f.group == 'testuser'
