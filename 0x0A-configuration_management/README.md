![Holberton](https://user-images.githubusercontent.com/85451781/140782830-f3f4a341-3d98-4a6e-89d2-76d684c80e9e.png)

# 0x0A. Configuration management

## Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install puppet

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

You do **not** need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](https://puppet.com/docs/puppet/5.5/puppet_index.html)

### Install puppet-lint

```bash
$ gem install puppet-lint
```

## Tasks

### 0. Create a file

Using Puppet, create a file in /tmp.

Requirements:

- File path is /tmp/school
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains I love Puppet

```bash
Example:

root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~#
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x0A-configuration_management
- File: 0-create_a_file.pp

### 1. Install a package

Using Puppet, install puppet-lint.

Requirements:

- Install puppet-lint
- Version must be 2.5.0

Example:

```bash
root@d391259bf577:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for d391259bf577 in environment production in 0.14 seconds
Notice: Applied catalog in 0.20 seconds
root@d391259bf577:/# gem list

*** LOCAL GEMS ***

puppet-lint (2.5.0)
root@d391259bf577:/#
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x0A-configuration_management
- File: 1-install_a_package.pp

### 2. Execute a command

Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

- Must use the exec Puppet resource
- Must use pkill

Example:

Terminal #0 - starting my process

```bash
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
```

Terminal #1 - executing my manifest

```bash
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/#
```

Terminal #0 - process has been terminated

```bash
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x0A-configuration_management
- File: 2-execute_a_command.pp
