# Puppet manifests  that install puppet-lint
package { 'puppet-lint':
  ensure   => 'installed',
  provider => 'gem',
}
