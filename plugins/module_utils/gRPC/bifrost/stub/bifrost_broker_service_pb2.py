# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bifrost/stub/bifrost_broker_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bifrost.base import bifrost_base_pb2 as bifrost_dot_base_dot_bifrost__base__pb2
from bifrost.base import rpc_id_pb2 as bifrost_dot_base_dot_rpc__id__pb2
from bifrost.base import error_pb2 as bifrost_dot_base_dot_error__pb2
from bifrost.portal_proxy import portal_proxy_pb2 as bifrost_dot_portal__proxy_dot_portal__proxy__pb2
from bifrost.stub import capabilities_pb2 as bifrost_dot_stub_dot_capabilities__pb2
from bifrost.stub import proxy_service_pb2 as bifrost_dot_stub_dot_proxy__service__pb2
from bifrost.task import bifrost_task_pb2 as bifrost_dot_task_dot_bifrost__task__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.master.stub import stub_pb2 as magneto_dot_master_dot_stub_dot_stub__pb2
from magneto.slave.stub import bridge_updates_pb2 as magneto_dot_slave_dot_stub_dot_bridge__updates__pb2
from gandalf.base import error_pb2 as gandalf_dot_base_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)bifrost/stub/bifrost_broker_service.proto\x12\x15\x63ohesity.bifrost.stub\x1a\x1f\x62ifrost/base/bifrost_base.proto\x1a\x19\x62ifrost/base/rpc_id.proto\x1a\x18\x62ifrost/base/error.proto\x1a\'bifrost/portal_proxy/portal_proxy.proto\x1a\x1f\x62ifrost/stub/capabilities.proto\x1a bifrost/stub/proxy_service.proto\x1a\x1f\x62ifrost/task/bifrost_task.proto\x1a\x1c\x63onfigs/cluster_config.proto\x1a\x18magneto/base/error.proto\x1a\x1fmagneto/agents/base/agent.proto\x1a\x1emagneto/master/stub/stub.proto\x1a\'magneto/slave/stub/bridge_updates.proto\x1a\x18gandalf/base/error.proto\"\xf5\x02\n\x0e\x43onnectMessage\x12\x11\n\ttenant_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63onstituent_id\x18\x02 \x01(\x03\x12\x12\n\nsession_id\x18\x03 \x01(\x03\x12\x13\n\x07ip_addr\x18\x04 \x01(\tB\x02\x18\x01\x12\x42\n\x12\x63\x61pability_message\x18\x05 \x01(\x0b\x32&.cohesity.bifrost.stub.CapabilityProto\x12\x13\n\x07version\x18\x06 \x01(\tB\x02\x18\x01\x12G\n\x14hyx_connector_config\x18\x08 \x01(\x0b\x32).cohesity.bifrost.HyxConnectorConfigProto\x12\x1c\n\ris_rigel_mode\x18\t \x01(\x08:\x05\x66\x61lse\x12I\n\x11resource_capacity\x18\n \x01(\x0b\x32..cohesity.bifrost.BifrostResourceCapacityProtoJ\x04\x08\x07\x10\x08\">\n\x05RpcId\x12!\n\x19\x62ifrost_broker_session_id\x18\x01 \x01(\x03\x12\x12\n\nrequest_id\x18\x02 \x01(\x03\"\x89\x01\n\rBrokerRequest\x12,\n\x06rpc_id\x18\x01 \x01(\x0b\x32\x1c.cohesity.bifrost.RpcIdProto\x12\x16\n\x0e\x64\x65\x61\x64line_msecs\x18\x03 \x01(\x03\x12\x32\n\x03\x61rg\x18\x02 \x01(\x0b\x32%.cohesity.bifrost.stub.BifrostCallArg\"y\n\x0f\x42ifrostResponse\x12,\n\x06rpc_id\x18\x01 \x01(\x0b\x32\x1c.cohesity.bifrost.RpcIdProto\x12\x38\n\x06result\x18\x02 \x01(\x0b\x32(.cohesity.bifrost.stub.BifrostCallResult\"\xb8\x01\n\rStreamMessage\x12\x36\n\x07\x63onnect\x18\x01 \x01(\x0b\x32%.cohesity.bifrost.stub.ConnectMessage\x12\x35\n\x07request\x18\x02 \x01(\x0b\x32$.cohesity.bifrost.stub.BrokerRequest\x12\x38\n\x08response\x18\x03 \x01(\x0b\x32&.cohesity.bifrost.stub.BifrostResponse\"I\n\x0bLivenessArg\x12:\n\x0b\x63onnect_arg\x18\x01 \x01(\x0b\x32%.cohesity.bifrost.stub.ConnectMessage\"\x12\n\x10LivenessResponse\"\x9e\x03\n\nMagnetoArg\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.cohesity.bifrost.stub.MagnetoArg.CallType\x12\x1e\n\x16magneto_constituent_id\x18\x02 \x01(\x03\x12G\n\x11\x61\x63tion_update_arg\x18\x03 \x01(\x0b\x32,.cohesity.magneto.slave.stub.ActionUpdateArg\x12Q\n\x16update_bridge_task_arg\x18\x04 \x01(\x0b\x32\x31.cohesity.magneto.master.stub.UpdateBridgeTaskArg\x12L\n\x17update_bifrost_task_arg\x18\x05 \x01(\x0b\x32+.cohesity.bifrost.task.UpdateBifrostTaskArg\"L\n\x08\x43\x61llType\x12\x11\n\rkActionUpdate\x10\x01\x12\x15\n\x11kUpdateBridgeTask\x10\x02\x12\x16\n\x12kUpdateBifrostTask\x10\x03\"\xf8\x02\n\rMagnetoResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x38\n\x04type\x18\x02 \x01(\x0e\x32*.cohesity.bifrost.stub.MagnetoArg.CallType\x12O\n\x16\x61\x63tion_update_response\x18\x03 \x01(\x0b\x32/.cohesity.magneto.slave.stub.ActionUpdateResult\x12Y\n\x1bupdate_bridge_task_response\x18\x04 \x01(\x0b\x32\x34.cohesity.magneto.master.stub.UpdateBridgeTaskResult\x12T\n\x1cupdate_bifrost_task_response\x18\x05 \x01(\x0b\x32..cohesity.bifrost.task.UpdateBifrostTaskResult\"9\n\nTestResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.bifrost.ErrorProto\"%\n\x10GetTenantInfoArg\x12\x11\n\ttenant_id\x18\x01 \x01(\t\"\x8c\x02\n\x13GetTenantInfoResult\x12@\n\x0cvault_config\x18\x01 \x01(\x0b\x32*.cohesity.configs.ClusterConfigProto.Vault\x12\x17\n\x0f\x63loud_domain_id\x18\x02 \x01(\x03\x12>\n\x08view_box\x18\x03 \x01(\x0b\x32,.cohesity.configs.ClusterConfigProto.ViewBox\x12\x12\n\ncluster_id\x18\x04 \x01(\x03\x12\x1d\n\x0eis_gcm_enabled\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\'\n\x18\x64\x65ny_embedded_agent_cert\x18\x06 \x01(\x08:\x05\x66\x61lse\"o\n\x16GetVaultCredentialsArg\x12\x10\n\x08vault_id\x18\x01 \x01(\x03\x12\x11\n\ttenant_id\x18\x02 \x01(\t\x12\x30\n%min_required_credential_validity_secs\x18\x03 \x01(\x03:\x01\x30\"m\n\x19GetVaultCredentialsResult\x12P\n\x11vault_credentials\x18\x01 \x01(\x0b\x32\x35.cohesity.configs.ClusterConfigProto.CloudCredentials\"\xe0\x01\n\x10UpdateGandalfArg\x12G\n\x0bupdate_type\x18\x01 \x01(\x0e\x32\x32.cohesity.bifrost.stub.UpdateGandalfArg.UpdateType\x12\x13\n\x0bgandalf_key\x18\x02 \x01(\t\x12\x11\n\ttenant_id\x18\x03 \x01(\t\x12\x16\n\x0ekey_data_zcbuf\x18\x04 \x01(\x0c\x12\x1b\n\x13gandalf_key_version\x18\x05 \x01(\x03\"&\n\nUpdateType\x12\x0b\n\x07kUpdate\x10\x01\x12\x0b\n\x07kDelete\x10\x02\"G\n\x13UpdateGandalfResult\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0e\x32!.cohesity.gandalf.ErrorProto.Type\"U\n\x16ReadFileFromLocalFsArg\x12\x10\n\x08\x66ilepath\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x19\n\x11num_bytes_to_read\x18\x04 \x01(\x03\"s\n\x19ReadFileFromLocalFsResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.bifrost.ErrorProto\x12\x0e\n\x06\x65rrnum\x18\x02 \x01(\x05\x12\x0b\n\x03\x65of\x18\x03 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\"D\n\x16GetClusterEndpointsArg\x12*\n\"min_cluster_config_gandalf_version\x18\x01 \x01(\x03\"\xfd\x01\n\x19GetClusterEndpointsResult\x12&\n\x1e\x63luster_config_gandalf_version\x18\x01 \x01(\x03\x12T\n\rendpoint_type\x18\x02 \x01(\x0e\x32=.cohesity.bifrost.stub.GetClusterEndpointsResult.EndpointType\x12\x19\n\x11\x63luster_endpoints\x18\x03 \x03(\t\"G\n\x0c\x45ndpointType\x12\x0c\n\x08kUnknown\x10\x01\x12\x15\n\x11kPrimaryIfaceVips\x10\x02\x12\x12\n\x0ekStaticNodeIps\x10\x03\"\x1d\n\x1bGetConnectorCertificatesArg\"\xa0\x02\n\x1eGetConnectorCertificatesResult\x12P\n\x0c\x63\x65rtificates\x18\x01 \x03(\x0b\x32:.cohesity.bifrost.stub.GetConnectorCertificatesResult.Cert\x1a\xab\x01\n\x04\x43\x65rt\x12\x16\n\x0epem_root_certs\x18\x01 \x02(\x0c\x12\x17\n\x0fpem_private_key\x18\x02 \x02(\x0c\x12\x16\n\x0epem_cert_chain\x18\x03 \x02(\x0c\x12Z\n\tcert_type\x18\x04 \x02(\x0e\x32=.cohesity.magneto.agents.AgentCertificateInformation.CertType:\x08kUnknown\"\xed\x06\n\x0e\x42ifrostRequest\x12<\n\x04type\x18\x01 \x01(\x0e\x32..cohesity.bifrost.stub.BifrostRequest.CallType\x12\x38\n\x0cliveness_arg\x18\x02 \x01(\x0b\x32\".cohesity.bifrost.stub.LivenessArg\x12\x36\n\x0bmagneto_arg\x18\x03 \x01(\x0b\x32!.cohesity.bifrost.stub.MagnetoArg\x12\x44\n\x13get_tenant_info_arg\x18\x04 \x01(\x0b\x32\'.cohesity.bifrost.stub.GetTenantInfoArg\x12P\n\x19get_vault_credentials_arg\x18\x05 \x01(\x0b\x32-.cohesity.bifrost.stub.GetVaultCredentialsArg\x12\x43\n\x12update_gandalf_arg\x18\x06 \x01(\x0b\x32\'.cohesity.bifrost.stub.UpdateGandalfArg\x12R\n\x1bread_file_from_local_fs_arg\x18\x07 \x01(\x0b\x32-.cohesity.bifrost.stub.ReadFileFromLocalFsArg\x12P\n\x19get_cluster_endpoints_arg\x18\x08 \x01(\x0b\x32-.cohesity.bifrost.stub.GetClusterEndpointsArg\x12Z\n\x1eget_connector_certificates_arg\x18\t \x01(\x0b\x32\x32.cohesity.bifrost.stub.GetConnectorCertificatesArg\"\xcb\x01\n\x08\x43\x61llType\x12\x11\n\rkLivenessPing\x10\x01\x12\x0c\n\x08kMagneto\x10\x02\x12\t\n\x05kTest\x10\x03\x12\x12\n\x0ekGetTenantInfo\x10\x04\x12\x18\n\x14kGetVaultCredentials\x10\x05\x12\x12\n\x0ekUpdateGandalf\x10\x06\x12\x18\n\x14kReadFileFromLocalFs\x10\x07\x12\x18\n\x14kGetClusterEndpoints\x10\x08\x12\x1d\n\x19kGetConnectorCertificates\x10\t\"\xb8\x06\n\x0e\x42rokerResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.bifrost.ErrorProto\x12<\n\x04type\x18\x02 \x01(\x0e\x32..cohesity.bifrost.stub.BifrostRequest.CallType\x12\x42\n\x11liveness_response\x18\x03 \x01(\x0b\x32\'.cohesity.bifrost.stub.LivenessResponse\x12<\n\x0emagneto_result\x18\x04 \x01(\x0b\x32$.cohesity.bifrost.stub.MagnetoResult\x12\x36\n\x0btest_result\x18\x05 \x01(\x0b\x32!.cohesity.bifrost.stub.TestResult\x12J\n\x16get_tenant_info_result\x18\x06 \x01(\x0b\x32*.cohesity.bifrost.stub.GetTenantInfoResult\x12V\n\x1cget_vault_credentials_result\x18\x07 \x01(\x0b\x32\x30.cohesity.bifrost.stub.GetVaultCredentialsResult\x12I\n\x15update_gandalf_result\x18\x08 \x01(\x0b\x32*.cohesity.bifrost.stub.UpdateGandalfResult\x12X\n\x1eread_file_from_local_fs_result\x18\t \x01(\x0b\x32\x30.cohesity.bifrost.stub.ReadFileFromLocalFsResult\x12V\n\x1cget_cluster_endpoints_result\x18\n \x01(\x0b\x32\x30.cohesity.bifrost.stub.GetClusterEndpointsResult\x12`\n!get_connector_certificates_result\x18\x0b \x01(\x0b\x32\x35.cohesity.bifrost.stub.GetConnectorCertificatesResult2\xf7\x03\n\x14\x42ifrostBrokerService\x12\\\n\x08\x42idiCall\x12$.cohesity.bifrost.stub.StreamMessage\x1a$.cohesity.bifrost.stub.StreamMessage\"\x00(\x01\x30\x01\x12\\\n\nBrokerCall\x12%.cohesity.bifrost.stub.BifrostRequest\x1a%.cohesity.bifrost.stub.BrokerResponse\"\x00\x12\x8c\x01\n\nBidiStream\x12;.cohesity.bifrost.portal_proxy.BifrostPortalProxyStreamData\x1a;.cohesity.bifrost.portal_proxy.BifrostPortalProxyStreamData\"\x00(\x01\x30\x01\x12\x93\x01\n\x11TunnelProxyStream\x12;.cohesity.bifrost.portal_proxy.BifrostPortalProxyStreamData\x1a;.cohesity.bifrost.portal_proxy.BifrostPortalProxyStreamData\"\x00(\x01\x30\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bifrost.stub.bifrost_broker_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONNECTMESSAGE'].fields_by_name['ip_addr']._loaded_options = None
  _globals['_CONNECTMESSAGE'].fields_by_name['ip_addr']._serialized_options = b'\030\001'
  _globals['_CONNECTMESSAGE'].fields_by_name['version']._loaded_options = None
  _globals['_CONNECTMESSAGE'].fields_by_name['version']._serialized_options = b'\030\001'
  _globals['_CONNECTMESSAGE']._serialized_start=484
  _globals['_CONNECTMESSAGE']._serialized_end=857
  _globals['_RPCID']._serialized_start=859
  _globals['_RPCID']._serialized_end=921
  _globals['_BROKERREQUEST']._serialized_start=924
  _globals['_BROKERREQUEST']._serialized_end=1061
  _globals['_BIFROSTRESPONSE']._serialized_start=1063
  _globals['_BIFROSTRESPONSE']._serialized_end=1184
  _globals['_STREAMMESSAGE']._serialized_start=1187
  _globals['_STREAMMESSAGE']._serialized_end=1371
  _globals['_LIVENESSARG']._serialized_start=1373
  _globals['_LIVENESSARG']._serialized_end=1446
  _globals['_LIVENESSRESPONSE']._serialized_start=1448
  _globals['_LIVENESSRESPONSE']._serialized_end=1466
  _globals['_MAGNETOARG']._serialized_start=1469
  _globals['_MAGNETOARG']._serialized_end=1883
  _globals['_MAGNETOARG_CALLTYPE']._serialized_start=1807
  _globals['_MAGNETOARG_CALLTYPE']._serialized_end=1883
  _globals['_MAGNETORESULT']._serialized_start=1886
  _globals['_MAGNETORESULT']._serialized_end=2262
  _globals['_TESTRESULT']._serialized_start=2264
  _globals['_TESTRESULT']._serialized_end=2321
  _globals['_GETTENANTINFOARG']._serialized_start=2323
  _globals['_GETTENANTINFOARG']._serialized_end=2360
  _globals['_GETTENANTINFORESULT']._serialized_start=2363
  _globals['_GETTENANTINFORESULT']._serialized_end=2631
  _globals['_GETVAULTCREDENTIALSARG']._serialized_start=2633
  _globals['_GETVAULTCREDENTIALSARG']._serialized_end=2744
  _globals['_GETVAULTCREDENTIALSRESULT']._serialized_start=2746
  _globals['_GETVAULTCREDENTIALSRESULT']._serialized_end=2855
  _globals['_UPDATEGANDALFARG']._serialized_start=2858
  _globals['_UPDATEGANDALFARG']._serialized_end=3082
  _globals['_UPDATEGANDALFARG_UPDATETYPE']._serialized_start=3044
  _globals['_UPDATEGANDALFARG_UPDATETYPE']._serialized_end=3082
  _globals['_UPDATEGANDALFRESULT']._serialized_start=3084
  _globals['_UPDATEGANDALFRESULT']._serialized_end=3155
  _globals['_READFILEFROMLOCALFSARG']._serialized_start=3157
  _globals['_READFILEFROMLOCALFSARG']._serialized_end=3242
  _globals['_READFILEFROMLOCALFSRESULT']._serialized_start=3244
  _globals['_READFILEFROMLOCALFSRESULT']._serialized_end=3359
  _globals['_GETCLUSTERENDPOINTSARG']._serialized_start=3361
  _globals['_GETCLUSTERENDPOINTSARG']._serialized_end=3429
  _globals['_GETCLUSTERENDPOINTSRESULT']._serialized_start=3432
  _globals['_GETCLUSTERENDPOINTSRESULT']._serialized_end=3685
  _globals['_GETCLUSTERENDPOINTSRESULT_ENDPOINTTYPE']._serialized_start=3614
  _globals['_GETCLUSTERENDPOINTSRESULT_ENDPOINTTYPE']._serialized_end=3685
  _globals['_GETCONNECTORCERTIFICATESARG']._serialized_start=3687
  _globals['_GETCONNECTORCERTIFICATESARG']._serialized_end=3716
  _globals['_GETCONNECTORCERTIFICATESRESULT']._serialized_start=3719
  _globals['_GETCONNECTORCERTIFICATESRESULT']._serialized_end=4007
  _globals['_GETCONNECTORCERTIFICATESRESULT_CERT']._serialized_start=3836
  _globals['_GETCONNECTORCERTIFICATESRESULT_CERT']._serialized_end=4007
  _globals['_BIFROSTREQUEST']._serialized_start=4010
  _globals['_BIFROSTREQUEST']._serialized_end=4887
  _globals['_BIFROSTREQUEST_CALLTYPE']._serialized_start=4684
  _globals['_BIFROSTREQUEST_CALLTYPE']._serialized_end=4887
  _globals['_BROKERRESPONSE']._serialized_start=4890
  _globals['_BROKERRESPONSE']._serialized_end=5714
  _globals['_BIFROSTBROKERSERVICE']._serialized_start=5717
  _globals['_BIFROSTBROKERSERVICE']._serialized_end=6220
# @@protoc_insertion_point(module_scope)
