# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/onprem_deploy.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import vmware_common_pb2 as magneto_dot_base_dot_vmware__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n magneto/base/onprem_deploy.proto\x12\x10\x63ohesity.magneto\x1a magneto/base/vmware_common.proto\"g\n\x17\x44\x65ployVMsToOnPremParams\x12L\n\x1b\x64\x65ploy_vms_to_vmware_params\x18\x01 \x01(\x0b\x32\'.cohesity.magneto.RestoreVMwareVMParams')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.onprem_deploy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DEPLOYVMSTOONPREMPARAMS']._serialized_start=88
  _globals['_DEPLOYVMSTOONPREMPARAMS']._serialized_end=191
# @@protoc_insertion_point(module_scope)
