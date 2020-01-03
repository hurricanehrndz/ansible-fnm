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
    f = host.file('/home/hurricanehrndz/.fnm/aliases/default/bin/node')

    assert f.exists
    assert f.user == 'hurricanehrndz'
    assert f.group == 'hurricanehrndz'
    assert f.mode == 0o755


def test_npm_neovim_pkg(host):
    f = host.file(
      '/home/hurricanehrndz/.fnm/aliases/default/bin/neovim_node_host'
    )

    assert f.exists
    assert f.user == 'hurricanehrndz'
    assert f.group == 'hurricanehrndz'
