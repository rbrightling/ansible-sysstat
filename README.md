SYSSTAT
=======

![Test Ansible Role](https://github.com/rbrightling/ansible-sysstat/workflows/Test%20Ansible%20Role/badge.svg?branch=main) [![Ansible Galaxy](http://img.shields.io/badge/galaxy-rbrightling.sysstat-660198.svg?style=flat)](https://galaxy.ansible.com/rbrightling/sysstat)

Install and configure sysstat - System performance tools for linux.

Requirements
------------

Supported OS's:
  - Debian 10
  - RedHat 8

**NOTE**: Debian 10 requires cron to be installed and running to generate system activity log files.

Role Variables
--------------

```yaml
# Number of days to keep daily data files or reports.
sysstat_history: 28

# Number of days after which to compress files with the given zip program
sysstat_compressafter: 31

# Options to pass to sadc
sysstat_sadc_options: "-S DISK"

# Directory where the standard system activity daily data and report files are saved
sysstat_sa_dir: "{{ sysstat__sa_dir }}"
# Debian: /var/log/sysstat
# RedHat: /var/log/sa

# Program to use to compress data and report files
sysstat_zip: xz

# Set to generate reports based on yesterdays data
sysstat_yesterday: null

# Set to prevent reports being generated
sysstat_reports: null

# The interval of when collect data in minutes
sysstat_activity_interval: 10
# Debian cron: */{{ sysstat_activity_interval }}
# Redhat timer: *:00/{{ sysstat_activity_interval }}
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: include sysstat role
      include_role:
        name: sysstat
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
