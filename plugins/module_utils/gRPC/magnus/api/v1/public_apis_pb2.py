# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magnus/api/v1/public_apis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magnus.api.v1 import public_vmware_data_pb2 as magnus_dot_api_dot_v1_dot_public__vmware__data__pb2
from magnus.api.google.api import annotations_pb2 as magnus_dot_api_dot_google_dot_api_dot_annotations__pb2
from magnus.api.protoc_gen_openapiv2.options import annotations_pb2 as magnus_dot_api_dot_protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmagnus/api/v1/public_apis.proto\x12\x16\x63ohesity.magnus.api.v1\x1a&magnus/api/v1/public_vmware_data.proto\x1a\'magnus/api/google/api/annotations.proto\x1a\x39magnus/api/protoc-gen-openapiv2/options/annotations.proto2\xa1\x0b\n\x17MagnusPublicGRPCService\x12\xa0\x02\n\x15VMwareDatastoreAction\x12\x30.cohesity.magnus.api.v1.VMwareDatastoreActionArg\x1a\x33.cohesity.magnus.api.v1.VMwareDatastoreActionResult\"\x9f\x01\x92\x41r\n\x10VMware Datastore\x12\x18VMware datastore actions\x1a\x44RPC to perform various actions on VMware datastore e.g create/delete\x82\xd3\xe4\x93\x02$\"\x1f/magnus/api/v1/vmware/datastore:\x01*\x12\xcd\x02\n\x1fVMwareDatastoreActionTaskStatus\x12:.cohesity.magnus.api.v1.VMwareDatastoreActionTaskStatusArg\x1a=.cohesity.magnus.api.v1.VMwareDatastoreActionTaskStatusResult\"\xae\x01\x92\x41z\n\x10VMware Datastore\x12#VMware datastore action task status\x1a\x41RPC to get task status of action requested on a VMware datastore.\x82\xd3\xe4\x93\x02+\x12)/magnus/api/v1/vmware/datastore/{task_id}\x12\x8a\x02\n\x0eVMwareVMAction\x12).cohesity.magnus.api.v1.VMwareVMActionArg\x1a,.cohesity.magnus.api.v1.VMwareVMActionResult\"\x9e\x01\x92\x41x\n\tVMware VM\x12\x11VMware VM actions\x1aXRPC to perform various actions on VMware VMs e.g create/delete/reconfigure/relocate etc.\x82\xd3\xe4\x93\x02\x1d\"\x18/magnus/api/v1/vmware/vm:\x01*\x12\x9f\x02\n\x18VMwareVMActionTaskStatus\x12\x33.cohesity.magnus.api.v1.VMwareVMActionTaskStatusArg\x1a\x36.cohesity.magnus.api.v1.VMwareVMActionTaskStatusResult\"\x95\x01\x92\x41h\n\tVMware VM\x12\x1cVMware VM action task status\x1a=RPC to get task status of an action requested on a VMware VM.\x82\xd3\xe4\x93\x02$\x12\"/magnus/api/v1/vmware/vm/{task_id}\x1a\xe3\x01\x92\x41\xdf\x01\x12\x98\x01Magnus service is used to interact with primary environments such as vCenter to create and fetch resources. It exposes various public APIs listed below.\x1a\x42\n\"Find out more about Magnus service\x12\x1chttps://support.cohesity.comB\xa0\x02Z\x1d\x63ohesity/magnus/api/v1;magnus\x92\x41\xfd\x01\x12\x87\x01\n\x12Magnus public APIs\x12(APIs exposed by Magnus for DR operations\"B\n\x10\x43ohesity Support\x12\x18https://www.cohesity.com\x1a\x14support@cohesity.com2\x03\x31.0*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonrJ\n-More about Cohesity disaster recovery service\x12\x19https://docs.cohesity.comb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magnus.api.v1.public_apis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\035cohesity/magnus/api/v1;magnus\222A\375\001\022\207\001\n\022Magnus public APIs\022(APIs exposed by Magnus for DR operations\"B\n\020Cohesity Support\022\030https://www.cohesity.com\032\024support@cohesity.com2\0031.0*\001\0022\020application/json:\020application/jsonrJ\n-More about Cohesity disaster recovery service\022\031https://docs.cohesity.com'
  _globals['_MAGNUSPUBLICGRPCSERVICE']._loaded_options = None
  _globals['_MAGNUSPUBLICGRPCSERVICE']._serialized_options = b'\222A\337\001\022\230\001Magnus service is used to interact with primary environments such as vCenter to create and fetch resources. It exposes various public APIs listed below.\032B\n\"Find out more about Magnus service\022\034https://support.cohesity.com'
  _globals['_MAGNUSPUBLICGRPCSERVICE'].methods_by_name['VMwareDatastoreAction']._loaded_options = None
  _globals['_MAGNUSPUBLICGRPCSERVICE'].methods_by_name['VMwareDatastoreAction']._serialized_options = b'\222Ar\n\020VMware Datastore\022\030VMware datastore actions\032DRPC to perform various actions on VMware datastore e.g create/delete\202\323\344\223\002$\"\037/magnus/api/v1/vmware/datastore:\001*'
  _globals['_MAGNUSPUBLICGRPCSERVICE'].methods_by_name['VMwareDatastoreActionTaskStatus']._loaded_options = None
  _globals['_MAGNUSPUBLICGRPCSERVICE'].methods_by_name['VMwareDatastoreActionTaskStatus']._serialized_options = b'\222Az\n\020VMware Datastore\022#VMware datastore action task status\032ARPC to get task status of action requested on a VMware datastore.\202\323\344\223\002+\022)/magnus/api/v1/vmware/datastore/{task_id}'
  _globals['_MAGNUSPUBLICGRPCSERVICE'].methods_by_name['VMwareVMAction']._loaded_options = None
  _globals['_MAGNUSPUBLICGRPCSERVICE'].methods_by_name['VMwareVMAction']._serialized_options = b'\222Ax\n\tVMware VM\022\021VMware VM actions\032XRPC to perform various actions on VMware VMs e.g create/delete/reconfigure/relocate etc.\202\323\344\223\002\035\"\030/magnus/api/v1/vmware/vm:\001*'
  _globals['_MAGNUSPUBLICGRPCSERVICE'].methods_by_name['VMwareVMActionTaskStatus']._loaded_options = None
  _globals['_MAGNUSPUBLICGRPCSERVICE'].methods_by_name['VMwareVMActionTaskStatus']._serialized_options = b'\222Ah\n\tVMware VM\022\034VMware VM action task status\032=RPC to get task status of an action requested on a VMware VM.\202\323\344\223\002$\022\"/magnus/api/v1/vmware/vm/{task_id}'
  _globals['_MAGNUSPUBLICGRPCSERVICE']._serialized_start=200
  _globals['_MAGNUSPUBLICGRPCSERVICE']._serialized_end=1641
# @@protoc_insertion_point(module_scope)
