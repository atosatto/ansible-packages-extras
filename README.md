Ansible Library: Package Extras
===============================

[![Build Status](https://travis-ci.org/atosatto/ansible-package-extras.svg?branch=master)](https://travis-ci.org/atosatto/ansible-package-extras)

Library modules to get additional package informations from RPM and APT.

Requirements
------------

None.

Dependencies
------------

The `apt_madison` module depends on `python-apt`.

Example Playbook
----------------

    - name: Extract the sudo package version
      yum_madison:
        name: "sudo"
        update_cache: yes
      changed_when: False
      register: sudo_version_result

    - debug: msg="{{ sudo_version_result.versions | map(attribute='version') | first }}"

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
