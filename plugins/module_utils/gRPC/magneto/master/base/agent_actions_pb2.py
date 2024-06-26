# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/master/base/agent_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.agents.stub import agent_param_pb2 as magneto_dot_agents_dot_stub_dot_agent__param__pb2
from magneto.agents.windows.sql.base import sql_param_pb2 as magneto_dot_agents_dot_windows_dot_sql_dot_base_dot_sql__param__pb2
from magneto.agents.windows.stub import ad_param_pb2 as magneto_dot_agents_dot_windows_dot_stub_dot_ad__param__pb2
from magneto.agents.windows.stub import exchange_param_pb2 as magneto_dot_agents_dot_windows_dot_stub_dot_exchange__param__pb2
from magneto.base import api_version_pb2 as magneto_dot_base_dot_api__version__pb2
from magneto.base import credentials_pb2 as magneto_dot_base_dot_credentials__pb2
from magneto.base.entities import exchange_pb2 as magneto_dot_base_dot_entities_dot_exchange__pb2
from magneto.base.entities import sql_pb2 as magneto_dot_base_dot_entities_dot_sql__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import permissions_pb2 as magneto_dot_base_dot_permissions__pb2
from magneto.master.base import master_pb2 as magneto_dot_master_dot_base_dot_master__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'magneto/master/base/agent_actions.proto\x12\x17\x63ohesity.magneto.master\x1a\x1fmagneto/agents/base/agent.proto\x1a%magneto/agents/stub/agent_param.proto\x1a/magneto/agents/windows/sql/base/sql_param.proto\x1a*magneto/agents/windows/stub/ad_param.proto\x1a\x30magneto/agents/windows/stub/exchange_param.proto\x1a\x1emagneto/base/api_version.proto\x1a\x1emagneto/base/credentials.proto\x1a$magneto/base/entities/exchange.proto\x1a\x1fmagneto/base/entities/sql.proto\x1a\x18magneto/base/enums.proto\x1a\x18magneto/base/error.proto\x1a\x1emagneto/base/permissions.proto\x1a magneto/master/base/master.proto\"\xae\x06\n\x15\x45xecuteAgentActionArg\x12\x41\n\x10\x61pi_request_attr\x18\x0c \x01(\x0b\x32\'.cohesity.magneto.master.APIRequestAttr\x12\x34\n\x08\x65nv_type\x18\x01 \x01(\x0e\x32\".cohesity.magneto.Environment.Type\x12\x31\n\x0b\x61pi_version\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.APIVersion\x12\x34\n\tuser_info\x18\x03 \x01(\x0b\x32!.cohesity.magneto.UserInformation\x12\x0f\n\x07task_id\x18\x04 \x01(\x03\x12\x1b\n\x13\x61\x64_parent_entity_id\x18\x07 \x01(\x03\x12W\n\x16\x65xchange_action_params\x18\x08 \x01(\x0b\x32\x37.cohesity.magneto.master.ExchangeActionAdditionalParams\x12O\n\rad_action_arg\x18\x05 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.ExecuteADActionArg\x12[\n\x13\x65xchange_action_arg\x18\x06 \x01(\x0b\x32>.cohesity.magneto.agents.windows.stub.ExecuteExchangeActionArg\x12M\n\x14get_app_topology_arg\x18\t \x01(\x0b\x32/.cohesity.magneto.agents.stub.GetAppTopologyArg\x12P\n\x0esql_action_arg\x18\n \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.sql.ExecuteSQLActionArg\x12\x1c\n\x10network_realm_id\x18\x0b \x01(\x03:\x02-1\x12?\n\x0fo365_action_arg\x18\r \x01(\x0b\x32&.cohesity.magneto.master.O365ActionArg\"\xee\x04\n\x18\x45xecuteAgentActionResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x34\n\x08\x65nv_type\x18\x02 \x01(\x0e\x32\".cohesity.magneto.Environment.Type\x12U\n\x10\x61\x64_action_result\x18\x03 \x01(\x0b\x32;.cohesity.magneto.agents.windows.stub.ExecuteADActionResult\x12\x61\n\x16\x65xchange_action_result\x18\x04 \x01(\x0b\x32\x41.cohesity.magneto.agents.windows.stub.ExecuteExchangeActionResult\x12\x46\n\x0f\x65xchange_result\x18\x05 \x01(\x0b\x32-.cohesity.magneto.master.ExchangeActionResult\x12N\n\x17get_app_topology_result\x18\x06 \x01(\x0b\x32-.cohesity.magneto.master.GetAppTopologyResult\x12V\n\x11sql_action_result\x18\x07 \x01(\x0b\x32;.cohesity.magneto.agents.windows.sql.ExecuteSQLActionResult\x12\x45\n\x12o365_action_result\x18\x08 \x01(\x0b\x32).cohesity.magneto.master.O365ActionResult\"[\n\x1e\x45xchangeActionAdditionalParams\x12\x19\n\x11\x65xchange_endpoint\x18\x01 \x01(\t\x12\x1e\n\x16\x65xchange_dag_entity_id\x18\x02 \x01(\x03\"\xb0\x01\n\x14\x45xchangeActionResult\x12R\n\x0b\x61\x63tion_type\x18\x01 \x01(\x0e\x32=.cohesity.magneto.agents.windows.stub.ExchangeActionType.Type\x12\x44\n\x11\x65xchange_topology\x18\x02 \x01(\x0b\x32).cohesity.magneto.master.ExchangeTopology\"\x97\x01\n\x10\x45xchangeTopology\x12\x1c\n\x14is_standalone_server\x18\x01 \x01(\x08\x12\x45\n\x11\x65xchange_dag_info\x18\x02 \x01(\x0b\x32*.cohesity.magneto.exchange.ExchangeDAGInfo\x12\x1e\n\x16\x65xchange_dag_entity_id\x18\x03 \x01(\x03\"\x83\x01\n\x14GetAppTopologyResult\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12>\n\x10\x61pp_topology_vec\x18\x02 \x03(\x0b\x32$.cohesity.magneto.master.AppTopology\"\xe6\x06\n\tSqlServer\x12I\n\x08resource\x18\x01 \x01(\x0b\x32\x37.cohesity.magneto.agents.ClusterNetworkingInfo.Resource\x12=\n\x02id\x18\x0c \x01(\x0b\x32\x31.cohesity.magneto.agents.stub.TopologyNode.NodeID\x12H\n\x06status\x18\x03 \x01(\x0e\x32..cohesity.magneto.master.SqlServer.Status.Type:\x08kUnknown\x12+\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x1c\n\x14\x61gent_sw_version_str\x18\x0b \x01(\t\x12h\n\x16\x61gent_supported_status\x18\x05 \x01(\x0e\x32<.cohesity.magneto.master.SqlServer.AgentSupportedStatus.Type:\nkSupported\x12\"\n\x1alast_agent_info_time_usecs\x18\x06 \x01(\x03\x12\x12\n\nis_primary\x18\x07 \x01(\x08\x12?\n\x10sql_instance_vec\x18\x08 \x03(\x0b\x32%.cohesity.magneto.sql.SQLInstanceInfo\x12\x18\n\x10\x64isplay_messages\x18\t \x03(\t\x12X\n\x1ehost_settings_check_result_vec\x18\n \x03(\x0b\x32\x30.cohesity.magneto.agents.HostSettingsCheckResult\x12\x1e\n\x16is_selected_by_default\x18\r \x01(\x08\x1am\n\x06Status\"c\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\x0c\n\x08kHealthy\x10\x01\x12\x11\n\rkUnregistered\x10\x02\x12\x10\n\x0ckUnreachable\x10\x03\x12\x0e\n\nkUnHealthy\x10\x04\x12\n\n\x06kError\x10\x05\x1aN\n\x14\x41gentSupportedStatus\"6\n\x04Type\x12\x0e\n\nkSupported\x10\x00\x12\x0c\n\x08kUpgrade\x10\x01\x12\x10\n\x0ckUnsupported\x10\x02J\x04\x08\x02\x10\x03\"\xbc\x07\n\x0eSqlAppTopology\x12\x1c\n\x14is_standalone_server\x18\x01 \x01(\x08\x12:\n\x0estandalone_vec\x18\x02 \x03(\x0b\x32\".cohesity.magneto.master.SqlServer\x12K\n\x0f\x66\x63i_cluster_vec\x18\x03 \x03(\x0b\x32\x32.cohesity.magneto.master.SqlAppTopology.FCICluster\x12G\n\raag_group_vec\x18\x05 \x03(\x0b\x32\x30.cohesity.magneto.master.SqlAppTopology.AAGGroup\x1a\xc0\x02\n\nFCICluster\x12=\n\x02id\x18\x06 \x01(\x0b\x32\x31.cohesity.magneto.agents.stub.TopologyNode.NodeID\x12\x15\n\rinstance_name\x18\x02 \x01(\t\x12I\n\x08resource\x18\x03 \x01(\x0b\x32\x37.cohesity.magneto.agents.ClusterNetworkingInfo.Resource\x12\x38\n\x0c\x66\x63i_node_vec\x18\x04 \x03(\x0b\x32\".cohesity.magneto.master.SqlServer\x12\x1e\n\x16is_selected_by_default\x18\x07 \x01(\x08\x12+\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProtoJ\x04\x08\x01\x10\x02J\x04\x08\x05\x10\x06\x1a\xea\x02\n\x08\x41\x41GGroup\x12=\n\x02id\x18\x07 \x01(\x0b\x32\x31.cohesity.magneto.agents.stub.TopologyNode.NodeID\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12I\n\x08resource\x18\x03 \x01(\x0b\x32\x37.cohesity.magneto.agents.ClusterNetworkingInfo.Resource\x12\x38\n\x0c\x61\x61g_node_vec\x18\x04 \x03(\x0b\x32\".cohesity.magneto.master.SqlServer\x12O\n\x13\x61\x61g_fci_cluster_vec\x18\x05 \x03(\x0b\x32\x32.cohesity.magneto.master.SqlAppTopology.FCICluster\x12/\n\x08\x61\x61g_info\x18\x06 \x01(\x0b\x32\x1d.cohesity.magneto.sql.AAGInfoJ\x04\x08\x01\x10\x02J\x04\x08\x04\x10\x05J\x04\x08\x64\x10\x65\"\xb9\x01\n\x0b\x41ppTopology\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x34\n\x08\x65nv_type\x18\x02 \x01(\x0e\x32\".cohesity.magneto.Environment.Type\x12\x41\n\x10sql_app_topology\x18\x03 \x01(\x0b\x32\'.cohesity.magneto.master.SqlAppTopologyJ\x04\x08\x64\x10\x65\"T\n\x0eO365ActionType\"B\n\x04Type\x12\x1c\n\x18kCreateAzureApplications\x10\x01\x12\x1c\n\x18kUpdateAzureApplications\x10\x02\"\xab\x01\n\rO365ActionArg\x12\x41\n\x0b\x61\x63tion_type\x18\x01 \x02(\x0e\x32,.cohesity.magneto.master.O365ActionType.Type\x12\x45\n\x12\x65ntity_access_info\x18\x02 \x01(\x0b\x32).cohesity.magneto.master.EntityAccessInfo\x12\x10\n\x05\x63ount\x18\x03 \x01(\x05:\x01\x31\"\x9b\x01\n\x10O365ActionResult\x12\x41\n\x0b\x61\x63tion_type\x18\x01 \x02(\x0e\x32,.cohesity.magneto.master.O365ActionType.Type\x12\x44\n\x13\x61pp_credentials_vec\x18\x02 \x03(\x0b\x32\'.cohesity.magneto.MSGraphAppCredentialsB&Z$magneto/master/base/agent_actions.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.master.base.agent_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$magneto/master/base/agent_actions.pb'
  _globals['_EXECUTEAGENTACTIONARG']._serialized_start=537
  _globals['_EXECUTEAGENTACTIONARG']._serialized_end=1351
  _globals['_EXECUTEAGENTACTIONRESULT']._serialized_start=1354
  _globals['_EXECUTEAGENTACTIONRESULT']._serialized_end=1976
  _globals['_EXCHANGEACTIONADDITIONALPARAMS']._serialized_start=1978
  _globals['_EXCHANGEACTIONADDITIONALPARAMS']._serialized_end=2069
  _globals['_EXCHANGEACTIONRESULT']._serialized_start=2072
  _globals['_EXCHANGEACTIONRESULT']._serialized_end=2248
  _globals['_EXCHANGETOPOLOGY']._serialized_start=2251
  _globals['_EXCHANGETOPOLOGY']._serialized_end=2402
  _globals['_GETAPPTOPOLOGYRESULT']._serialized_start=2405
  _globals['_GETAPPTOPOLOGYRESULT']._serialized_end=2536
  _globals['_SQLSERVER']._serialized_start=2539
  _globals['_SQLSERVER']._serialized_end=3409
  _globals['_SQLSERVER_STATUS']._serialized_start=3214
  _globals['_SQLSERVER_STATUS']._serialized_end=3323
  _globals['_SQLSERVER_STATUS_TYPE']._serialized_start=3224
  _globals['_SQLSERVER_STATUS_TYPE']._serialized_end=3323
  _globals['_SQLSERVER_AGENTSUPPORTEDSTATUS']._serialized_start=3325
  _globals['_SQLSERVER_AGENTSUPPORTEDSTATUS']._serialized_end=3403
  _globals['_SQLSERVER_AGENTSUPPORTEDSTATUS_TYPE']._serialized_start=3349
  _globals['_SQLSERVER_AGENTSUPPORTEDSTATUS_TYPE']._serialized_end=3403
  _globals['_SQLAPPTOPOLOGY']._serialized_start=3412
  _globals['_SQLAPPTOPOLOGY']._serialized_end=4368
  _globals['_SQLAPPTOPOLOGY_FCICLUSTER']._serialized_start=3671
  _globals['_SQLAPPTOPOLOGY_FCICLUSTER']._serialized_end=3991
  _globals['_SQLAPPTOPOLOGY_AAGGROUP']._serialized_start=3994
  _globals['_SQLAPPTOPOLOGY_AAGGROUP']._serialized_end=4356
  _globals['_APPTOPOLOGY']._serialized_start=4371
  _globals['_APPTOPOLOGY']._serialized_end=4556
  _globals['_O365ACTIONTYPE']._serialized_start=4558
  _globals['_O365ACTIONTYPE']._serialized_end=4642
  _globals['_O365ACTIONTYPE_TYPE']._serialized_start=4576
  _globals['_O365ACTIONTYPE_TYPE']._serialized_end=4642
  _globals['_O365ACTIONARG']._serialized_start=4645
  _globals['_O365ACTIONARG']._serialized_end=4816
  _globals['_O365ACTIONRESULT']._serialized_start=4819
  _globals['_O365ACTIONRESULT']._serialized_end=4974
# @@protoc_insertion_point(module_scope)
