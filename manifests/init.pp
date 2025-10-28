class binary {
  file { '/root/sample_copy.bin':
    ensure => 'file',
    source => 'puppet:///modules/binary/sample_copy.bin',
    mode   => '0755',
  }
}
