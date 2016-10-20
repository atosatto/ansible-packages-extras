Ansible Library: Packages Extras
================================

[![Build Status](https://travis-ci.org/atosatto/ansible-packages-extras.svg?branch=master)](https://travis-ci.org/atosatto/ansible-packages-extras)

Library modules to extract additional package informations from YUM and APT.

Requirements
------------

The `apt_madison` module requires `python-apt` to be installed on target hosts.

Dependencies
------------

None.

Usage Example
-------------

    - hosts: all
      roles:
        - { role: atosatto.packages-extras }
      tasks:
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
