# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/java/compatibility_tests/v2.5.0/more_protos/src/proto/google/protobuf/descriptor.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n}experimental/smurugesan/protobuf-3.6.0/java/compatibility_tests/v2.5.0/more_protos/src/proto/google/protobuf/descriptor.proto\x12\x0fgoogle.protobuf\"G\n\x11\x46ileDescriptorSet\x12\x32\n\x04\x66ile\x18\x01 \x03(\x0b\x32$.google.protobuf.FileDescriptorProto\"\xcb\x03\n\x13\x46ileDescriptorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07package\x18\x02 \x01(\t\x12\x12\n\ndependency\x18\x03 \x03(\t\x12\x19\n\x11public_dependency\x18\n \x03(\x05\x12\x17\n\x0fweak_dependency\x18\x0b \x03(\x05\x12\x36\n\x0cmessage_type\x18\x04 \x03(\x0b\x32 .google.protobuf.DescriptorProto\x12\x37\n\tenum_type\x18\x05 \x03(\x0b\x32$.google.protobuf.EnumDescriptorProto\x12\x38\n\x07service\x18\x06 \x03(\x0b\x32\'.google.protobuf.ServiceDescriptorProto\x12\x38\n\textension\x18\x07 \x03(\x0b\x32%.google.protobuf.FieldDescriptorProto\x12-\n\x07options\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.FileOptions\x12\x39\n\x10source_code_info\x18\t \x01(\x0b\x32\x1f.google.protobuf.SourceCodeInfo\"\xa9\x03\n\x0f\x44\x65scriptorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x05\x66ield\x18\x02 \x03(\x0b\x32%.google.protobuf.FieldDescriptorProto\x12\x38\n\textension\x18\x06 \x03(\x0b\x32%.google.protobuf.FieldDescriptorProto\x12\x35\n\x0bnested_type\x18\x03 \x03(\x0b\x32 .google.protobuf.DescriptorProto\x12\x37\n\tenum_type\x18\x04 \x03(\x0b\x32$.google.protobuf.EnumDescriptorProto\x12H\n\x0f\x65xtension_range\x18\x05 \x03(\x0b\x32/.google.protobuf.DescriptorProto.ExtensionRange\x12\x30\n\x07options\x18\x07 \x01(\x0b\x32\x1f.google.protobuf.MessageOptions\x1a,\n\x0e\x45xtensionRange\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\"\x94\x05\n\x14\x46ieldDescriptorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\x05\x12:\n\x05label\x18\x04 \x01(\x0e\x32+.google.protobuf.FieldDescriptorProto.Label\x12\x38\n\x04type\x18\x05 \x01(\x0e\x32*.google.protobuf.FieldDescriptorProto.Type\x12\x11\n\ttype_name\x18\x06 \x01(\t\x12\x10\n\x08\x65xtendee\x18\x02 \x01(\t\x12\x15\n\rdefault_value\x18\x07 \x01(\t\x12.\n\x07options\x18\x08 \x01(\x0b\x32\x1d.google.protobuf.FieldOptions\"\xb6\x02\n\x04Type\x12\x0f\n\x0bTYPE_DOUBLE\x10\x01\x12\x0e\n\nTYPE_FLOAT\x10\x02\x12\x0e\n\nTYPE_INT64\x10\x03\x12\x0f\n\x0bTYPE_UINT64\x10\x04\x12\x0e\n\nTYPE_INT32\x10\x05\x12\x10\n\x0cTYPE_FIXED64\x10\x06\x12\x10\n\x0cTYPE_FIXED32\x10\x07\x12\r\n\tTYPE_BOOL\x10\x08\x12\x0f\n\x0bTYPE_STRING\x10\t\x12\x0e\n\nTYPE_GROUP\x10\n\x12\x10\n\x0cTYPE_MESSAGE\x10\x0b\x12\x0e\n\nTYPE_BYTES\x10\x0c\x12\x0f\n\x0bTYPE_UINT32\x10\r\x12\r\n\tTYPE_ENUM\x10\x0e\x12\x11\n\rTYPE_SFIXED32\x10\x0f\x12\x11\n\rTYPE_SFIXED64\x10\x10\x12\x0f\n\x0bTYPE_SINT32\x10\x11\x12\x0f\n\x0bTYPE_SINT64\x10\x12\"C\n\x05Label\x12\x12\n\x0eLABEL_OPTIONAL\x10\x01\x12\x12\n\x0eLABEL_REQUIRED\x10\x02\x12\x12\n\x0eLABEL_REPEATED\x10\x03\"\x8c\x01\n\x13\x45numDescriptorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x03(\x0b\x32).google.protobuf.EnumValueDescriptorProto\x12-\n\x07options\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.EnumOptions\"l\n\x18\x45numValueDescriptorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x05\x12\x32\n\x07options\x18\x03 \x01(\x0b\x32!.google.protobuf.EnumValueOptions\"\x90\x01\n\x16ServiceDescriptorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x06method\x18\x02 \x03(\x0b\x32&.google.protobuf.MethodDescriptorProto\x12\x30\n\x07options\x18\x03 \x01(\x0b\x32\x1f.google.protobuf.ServiceOptions\"\x7f\n\x15MethodDescriptorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ninput_type\x18\x02 \x01(\t\x12\x13\n\x0boutput_type\x18\x03 \x01(\t\x12/\n\x07options\x18\x04 \x01(\x0b\x32\x1e.google.protobuf.MethodOptions\"\xe9\x03\n\x0b\x46ileOptions\x12\x14\n\x0cjava_package\x18\x01 \x01(\t\x12\x1c\n\x14java_outer_classname\x18\x08 \x01(\t\x12\"\n\x13java_multiple_files\x18\n \x01(\x08:\x05\x66\x61lse\x12,\n\x1djava_generate_equals_and_hash\x18\x14 \x01(\x08:\x05\x66\x61lse\x12\x46\n\x0coptimize_for\x18\t \x01(\x0e\x32).google.protobuf.FileOptions.OptimizeMode:\x05SPEED\x12\x12\n\ngo_package\x18\x0b \x01(\t\x12\"\n\x13\x63\x63_generic_services\x18\x10 \x01(\x08:\x05\x66\x61lse\x12$\n\x15java_generic_services\x18\x11 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13py_generic_services\x18\x12 \x01(\x08:\x05\x66\x61lse\x12\x43\n\x14uninterpreted_option\x18\xe7\x07 \x03(\x0b\x32$.google.protobuf.UninterpretedOption\":\n\x0cOptimizeMode\x12\t\n\x05SPEED\x10\x01\x12\r\n\tCODE_SIZE\x10\x02\x12\x10\n\x0cLITE_RUNTIME\x10\x03*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"\xb8\x01\n\x0eMessageOptions\x12&\n\x17message_set_wire_format\x18\x01 \x01(\x08:\x05\x66\x61lse\x12.\n\x1fno_standard_descriptor_accessor\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x43\n\x14uninterpreted_option\x18\xe7\x07 \x03(\x0b\x32$.google.protobuf.UninterpretedOption*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"\xbe\x02\n\x0c\x46ieldOptions\x12:\n\x05\x63type\x18\x01 \x01(\x0e\x32#.google.protobuf.FieldOptions.CType:\x06STRING\x12\x0e\n\x06packed\x18\x02 \x01(\x08\x12\x13\n\x04lazy\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x19\n\ndeprecated\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x14\x65xperimental_map_key\x18\t \x01(\t\x12\x13\n\x04weak\x18\n \x01(\x08:\x05\x66\x61lse\x12\x43\n\x14uninterpreted_option\x18\xe7\x07 \x03(\x0b\x32$.google.protobuf.UninterpretedOption\"/\n\x05\x43Type\x12\n\n\x06STRING\x10\x00\x12\x08\n\x04\x43ORD\x10\x01\x12\x10\n\x0cSTRING_PIECE\x10\x02*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"x\n\x0b\x45numOptions\x12\x19\n\x0b\x61llow_alias\x18\x02 \x01(\x08:\x04true\x12\x43\n\x14uninterpreted_option\x18\xe7\x07 \x03(\x0b\x32$.google.protobuf.UninterpretedOption*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"b\n\x10\x45numValueOptions\x12\x43\n\x14uninterpreted_option\x18\xe7\x07 \x03(\x0b\x32$.google.protobuf.UninterpretedOption*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"`\n\x0eServiceOptions\x12\x43\n\x14uninterpreted_option\x18\xe7\x07 \x03(\x0b\x32$.google.protobuf.UninterpretedOption*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"_\n\rMethodOptions\x12\x43\n\x14uninterpreted_option\x18\xe7\x07 \x03(\x0b\x32$.google.protobuf.UninterpretedOption*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"\x9e\x02\n\x13UninterpretedOption\x12;\n\x04name\x18\x02 \x03(\x0b\x32-.google.protobuf.UninterpretedOption.NamePart\x12\x18\n\x10identifier_value\x18\x03 \x01(\t\x12\x1a\n\x12positive_int_value\x18\x04 \x01(\x04\x12\x1a\n\x12negative_int_value\x18\x05 \x01(\x03\x12\x14\n\x0c\x64ouble_value\x18\x06 \x01(\x01\x12\x14\n\x0cstring_value\x18\x07 \x01(\x0c\x12\x17\n\x0f\x61ggregate_value\x18\x08 \x01(\t\x1a\x33\n\x08NamePart\x12\x11\n\tname_part\x18\x01 \x02(\t\x12\x14\n\x0cis_extension\x18\x02 \x02(\x08\"\xb1\x01\n\x0eSourceCodeInfo\x12:\n\x08location\x18\x01 \x03(\x0b\x32(.google.protobuf.SourceCodeInfo.Location\x1a\x63\n\x08Location\x12\x10\n\x04path\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x10\n\x04span\x18\x02 \x03(\x05\x42\x02\x10\x01\x12\x18\n\x10leading_comments\x18\x03 \x01(\t\x12\x19\n\x11trailing_comments\x18\x04 \x01(\tB)\n\x13\x63om.google.protobufB\x10\x44\x65scriptorProtosH\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.java.compatibility_tests.v2.5.0.more_protos.src.proto.google.protobuf.descriptor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.google.protobufB\020DescriptorProtosH\001'
  _globals['_SOURCECODEINFO_LOCATION'].fields_by_name['path']._loaded_options = None
  _globals['_SOURCECODEINFO_LOCATION'].fields_by_name['path']._serialized_options = b'\020\001'
  _globals['_SOURCECODEINFO_LOCATION'].fields_by_name['span']._loaded_options = None
  _globals['_SOURCECODEINFO_LOCATION'].fields_by_name['span']._serialized_options = b'\020\001'
  _globals['_FILEDESCRIPTORSET']._serialized_start=146
  _globals['_FILEDESCRIPTORSET']._serialized_end=217
  _globals['_FILEDESCRIPTORPROTO']._serialized_start=220
  _globals['_FILEDESCRIPTORPROTO']._serialized_end=679
  _globals['_DESCRIPTORPROTO']._serialized_start=682
  _globals['_DESCRIPTORPROTO']._serialized_end=1107
  _globals['_DESCRIPTORPROTO_EXTENSIONRANGE']._serialized_start=1063
  _globals['_DESCRIPTORPROTO_EXTENSIONRANGE']._serialized_end=1107
  _globals['_FIELDDESCRIPTORPROTO']._serialized_start=1110
  _globals['_FIELDDESCRIPTORPROTO']._serialized_end=1770
  _globals['_FIELDDESCRIPTORPROTO_TYPE']._serialized_start=1391
  _globals['_FIELDDESCRIPTORPROTO_TYPE']._serialized_end=1701
  _globals['_FIELDDESCRIPTORPROTO_LABEL']._serialized_start=1703
  _globals['_FIELDDESCRIPTORPROTO_LABEL']._serialized_end=1770
  _globals['_ENUMDESCRIPTORPROTO']._serialized_start=1773
  _globals['_ENUMDESCRIPTORPROTO']._serialized_end=1913
  _globals['_ENUMVALUEDESCRIPTORPROTO']._serialized_start=1915
  _globals['_ENUMVALUEDESCRIPTORPROTO']._serialized_end=2023
  _globals['_SERVICEDESCRIPTORPROTO']._serialized_start=2026
  _globals['_SERVICEDESCRIPTORPROTO']._serialized_end=2170
  _globals['_METHODDESCRIPTORPROTO']._serialized_start=2172
  _globals['_METHODDESCRIPTORPROTO']._serialized_end=2299
  _globals['_FILEOPTIONS']._serialized_start=2302
  _globals['_FILEOPTIONS']._serialized_end=2791
  _globals['_FILEOPTIONS_OPTIMIZEMODE']._serialized_start=2722
  _globals['_FILEOPTIONS_OPTIMIZEMODE']._serialized_end=2780
  _globals['_MESSAGEOPTIONS']._serialized_start=2794
  _globals['_MESSAGEOPTIONS']._serialized_end=2978
  _globals['_FIELDOPTIONS']._serialized_start=2981
  _globals['_FIELDOPTIONS']._serialized_end=3299
  _globals['_FIELDOPTIONS_CTYPE']._serialized_start=3241
  _globals['_FIELDOPTIONS_CTYPE']._serialized_end=3288
  _globals['_ENUMOPTIONS']._serialized_start=3301
  _globals['_ENUMOPTIONS']._serialized_end=3421
  _globals['_ENUMVALUEOPTIONS']._serialized_start=3423
  _globals['_ENUMVALUEOPTIONS']._serialized_end=3521
  _globals['_SERVICEOPTIONS']._serialized_start=3523
  _globals['_SERVICEOPTIONS']._serialized_end=3619
  _globals['_METHODOPTIONS']._serialized_start=3621
  _globals['_METHODOPTIONS']._serialized_end=3716
  _globals['_UNINTERPRETEDOPTION']._serialized_start=3719
  _globals['_UNINTERPRETEDOPTION']._serialized_end=4005
  _globals['_UNINTERPRETEDOPTION_NAMEPART']._serialized_start=3954
  _globals['_UNINTERPRETEDOPTION_NAMEPART']._serialized_end=4005
  _globals['_SOURCECODEINFO']._serialized_start=4008
  _globals['_SOURCECODEINFO']._serialized_end=4185
  _globals['_SOURCECODEINFO_LOCATION']._serialized_start=4086
  _globals['_SOURCECODEINFO_LOCATION']._serialized_end=4185
# @@protoc_insertion_point(module_scope)
