# hurricanehrndz.fastnodemanager

[![Build Status](https://img.shields.io/travis/hurricanehrndz/ansible-fastnodemanager/master.svg?style=for-the-badge&logo=travis)](https://travis-ci.org/hurricanehrndz/ansible-fastnodemanager)
[![Ansible Role](https://img.shields.io/ansible/role/d/45604?style=for-the-badge)](https://galaxy.ansible.com/hurricanehrndz/fastnodemanager)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](https://raw.githubusercontent.com/hurricanehrndz/ansible-fastnodemanager/master/LICENSE)

Ansible role to install Fast Node Manager (fnm) and nodejs within userspace.

## Role Variables

A description of the settable variables for this role are listed below,
including any variables that are in [defaults/main.yml](defaults/main.yml),
[vars/main.yml](vars/main.yml), and any variables that can/should be set via
parameters to the role.

```yaml
fnm_user: "{{ ansible_user | default(lookup('env', 'USER')) }}"
```

The user for whom fnm, node, npm, and node modules will be installed. Default is
`ansible_user`.

```yaml
fnm_root: "{{ lookup('env', 'HOME') }}/{{ fnm_root_suffix }}"
```

Installation directory for `fnm`, this directory should be writeable by
`fnm_user`. Default is `fnm_user`'s home directory (`$HOME`),
plus `fnm_root_suffix` (`.fnm`). For example,
`/home/hurricanehrndz/.fnm`.

```yaml
fnm_root_suffix: ".fnm"
```

Suffix for installation directory, used only when `fnm_root` is not set.
Defaults, to `.fnm`.

```yaml
fnm_skip_shell: false
```

Set to `true`, to suppress modifications to `fnm_user`'s runtime
shell configuration.

```yaml
fnm_nodejs_versions: []
```

List of nodejs versions to install. Defaults, to `[ "latest-v12.x" ]`. First
entry in list is later defined as `fnm_default_nodejs_version`.

```yaml
fnm_npm_global_packages: []
```

A list of npm packages with `name`, (optional) `nodejs_version`, and (optional)
package `version` to be installed globally. For example:

```yaml
fnm_npm_global_packages:
  - name: gulp
  - name: neovim
    version: '4.7.0'
    nodejs_version: '12.14.0'

```

## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  tasks:
    - name: Run role
      include_role:
        name: hurricanehrndz.fastnodemanager
```

## License

[MIT](LICENSE)

## Author Information

