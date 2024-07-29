class binary {
  file { '/root/sample.bin':
    ensure => 'file',
    source => 'puppet:///modules/binary/sample.bin',
    mode   => '0755',
  }
}
