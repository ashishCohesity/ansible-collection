# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/base/packages.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19nexus/base/packages.proto\x12\x13\x63ohesity.nexus.base\"`\n\rPackagesProto\x12&\n\x1e\x63ohesity_software_packages_vec\x18\x01 \x03(\t\x12\'\n\x0cpackages_key\x18\x02 \x01(\t:\x11\x63ohesity_packages\"\xb0\x04\n\x13PackagesConfigProto\x12X\n\x15repository_config_vec\x18\x01 \x03(\x0b\x32\x39.cohesity.nexus.base.PackagesConfigProto.RepositoryConfig\x12&\n\x1e\x63ustomer_software_packages_vec\x18\x02 \x03(\t\x12$\n\x1cupdate_software_packages_vec\x18\x03 \x03(\t\x12\x1b\n\x13update_all_packages\x18\x04 \x01(\x08\x12\x1b\n\x13\x63ustom_baseos_setup\x18\x05 \x01(\x08\x12+\n#custom_baseos_linux_release_rpm_url\x18\x06 \x01(\t\x12%\n\x1d\x63ustomer_managed_baseos_setup\x18\x07 \x01(\x08\x1a\x31\n\x10RepositoryOption\x12\x0e\n\x06option\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x1a\xaf\x01\n\x10RepositoryConfig\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x10\n\x08url_path\x18\x03 \x02(\t\x12\x0e\n\x06gpgkey\x18\x04 \x02(\t\x12\x0f\n\x07\x65nabled\x18\x05 \x01(\x08\x12N\n\x0boptions_vec\x18\x06 \x03(\x0b\x32\x39.cohesity.nexus.base.PackagesConfigProto.RepositoryOption\"\x8a\x02\n\x13PackagesStatusProto\x12\x18\n\x10software_version\x18\x01 \x01(\t\x12N\n\x10package_info_vec\x18\x02 \x03(\x0b\x32\x34.cohesity.nexus.base.PackagesStatusProto.PackageInfo\x1a\x88\x01\n\x0bPackageInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0f\n\x07release\x18\x03 \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\t\x12\x10\n\x08packager\x18\x06 \x01(\t\x12\x0e\n\x06vendor\x18\x07 \x01(\tB\x18Z\x16nexus/base/packages.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.base.packages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\026nexus/base/packages.pb'
  _globals['_PACKAGESPROTO']._serialized_start=50
  _globals['_PACKAGESPROTO']._serialized_end=146
  _globals['_PACKAGESCONFIGPROTO']._serialized_start=149
  _globals['_PACKAGESCONFIGPROTO']._serialized_end=709
  _globals['_PACKAGESCONFIGPROTO_REPOSITORYOPTION']._serialized_start=482
  _globals['_PACKAGESCONFIGPROTO_REPOSITORYOPTION']._serialized_end=531
  _globals['_PACKAGESCONFIGPROTO_REPOSITORYCONFIG']._serialized_start=534
  _globals['_PACKAGESCONFIGPROTO_REPOSITORYCONFIG']._serialized_end=709
  _globals['_PACKAGESSTATUSPROTO']._serialized_start=712
  _globals['_PACKAGESSTATUSPROTO']._serialized_end=978
  _globals['_PACKAGESSTATUSPROTO_PACKAGEINFO']._serialized_start=842
  _globals['_PACKAGESSTATUSPROTO_PACKAGEINFO']._serialized_end=978
# @@protoc_insertion_point(module_scope)
