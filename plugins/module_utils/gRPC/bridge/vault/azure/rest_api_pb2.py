# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/vault/azure/rest_api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!bridge/vault/azure/rest_api.proto\x12\x1b\x63ohesity.bridge.vault.azure\"\xf2\x01\n\x1dGetImmutabilityPolicyResponse\x12Y\n\nproperties\x18\x01 \x01(\x0b\x32\x45.cohesity.bridge.vault.azure.GetImmutabilityPolicyResponse.Properties\x1av\n\nProperties\x12\x32\n*immutability_period_since_creation_in_days\x18\x01 \x01(\x05\x12%\n\x1d\x61llow_protected_append_writes\x18\x02 \x01(\x08\x12\r\n\x05state\x18\x03 \x01(\t\"\\\n\x1cGetOAuth2AccessTokenResponse\x12\x12\n\ntoken_type\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x12\x12\n\nexpires_in\x18\x03 \x01(\x03\"\xce\x16\n\x1dGetManagementPoliciesResponse\x12Y\n\nproperties\x18\x01 \x01(\x0b\x32\x45.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties\x1a\xd1\x15\n\nProperties\x12\\\n\x06policy\x18\x01 \x01(\x0b\x32L.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy\x12\x1a\n\x12last_modified_time\x18\x02 \x01(\t\x1a\xc8\x14\n\x06Policy\x12`\n\x05rules\x18\x01 \x03(\x0b\x32Q.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule\x1a\xdb\x13\n\x04Rule\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12p\n\ndefinition\x18\x04 \x01(\x0b\x32\\.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition\x1a\xb3\x12\n\nDefinition\x12u\n\x07\x61\x63tions\x18\x01 \x01(\x0b\x32\x64.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions\x12u\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x64.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Filters\x1a\x81\x10\n\x07\x41\x63tions\x12\x87\x01\n\tbase_blob\x18\x01 \x01(\x0b\x32t.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.BaseBlobActions\x12\x86\x01\n\x08snapshot\x18\x02 \x01(\x0b\x32t.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.SnapshotActions\x12\x84\x01\n\x07version\x18\x03 \x01(\x0b\x32s.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.VersionActions\x1a\xd3\x01\n\x15\x44\x61teAfterModification\x12(\n days_after_creation_greater_than\x18\x01 \x01(\x03\x12\x30\n(days_after_last_access_time_greater_than\x18\x02 \x01(\x03\x12\x30\n(days_after_last_tier_change_greater_than\x18\x03 \x01(\x03\x12,\n$days_after_modification_greater_than\x18\x04 \x01(\x03\x1a\xf2\x03\n\x0f\x42\x61seBlobActions\x12\x8a\x01\n\x06\x64\x65lete\x18\x01 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x12)\n!enable_auto_tier_to_hot_from_cool\x18\x02 \x01(\x08\x12\x93\x01\n\x0ftier_to_archive\x18\x03 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x12\x90\x01\n\x0ctier_to_cool\x18\x04 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x1a\xc7\x03\n\x0fSnapshotActions\x12\x8a\x01\n\x06\x64\x65lete\x18\x01 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x12\x93\x01\n\x0ftier_to_archive\x18\x02 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x12\x90\x01\n\x0ctier_to_cool\x18\x03 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x1a\xc6\x03\n\x0eVersionActions\x12\x8a\x01\n\x06\x64\x65lete\x18\x01 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x12\x93\x01\n\x0ftier_to_archive\x18\x02 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x12\x90\x01\n\x0ctier_to_cool\x18\x03 \x01(\x0b\x32z.cohesity.bridge.vault.azure.GetManagementPoliciesResponse.Properties.Policy.Rule.Definition.Actions.DateAfterModification\x1a\x33\n\x07\x46ilters\x12\x12\n\nblob_types\x18\x01 \x03(\t\x12\x14\n\x0cprefix_match\x18\x02 \x03(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.vault.azure.rest_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETIMMUTABILITYPOLICYRESPONSE']._serialized_start=67
  _globals['_GETIMMUTABILITYPOLICYRESPONSE']._serialized_end=309
  _globals['_GETIMMUTABILITYPOLICYRESPONSE_PROPERTIES']._serialized_start=191
  _globals['_GETIMMUTABILITYPOLICYRESPONSE_PROPERTIES']._serialized_end=309
  _globals['_GETOAUTH2ACCESSTOKENRESPONSE']._serialized_start=311
  _globals['_GETOAUTH2ACCESSTOKENRESPONSE']._serialized_end=403
  _globals['_GETMANAGEMENTPOLICIESRESPONSE']._serialized_start=406
  _globals['_GETMANAGEMENTPOLICIESRESPONSE']._serialized_end=3300
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES']._serialized_start=531
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES']._serialized_end=3300
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY']._serialized_start=668
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY']._serialized_end=3300
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE']._serialized_start=777
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE']._serialized_end=3300
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION']._serialized_start=945
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION']._serialized_end=3300
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS']._serialized_start=1198
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS']._serialized_end=3247
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS_DATEAFTERMODIFICATION']._serialized_start=1620
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS_DATEAFTERMODIFICATION']._serialized_end=1831
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS_BASEBLOBACTIONS']._serialized_start=1834
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS_BASEBLOBACTIONS']._serialized_end=2332
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS_SNAPSHOTACTIONS']._serialized_start=2335
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS_SNAPSHOTACTIONS']._serialized_end=2790
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS_VERSIONACTIONS']._serialized_start=2793
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_ACTIONS_VERSIONACTIONS']._serialized_end=3247
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_FILTERS']._serialized_start=3249
  _globals['_GETMANAGEMENTPOLICIESRESPONSE_PROPERTIES_POLICY_RULE_DEFINITION_FILTERS']._serialized_end=3300
# @@protoc_insertion_point(module_scope)
