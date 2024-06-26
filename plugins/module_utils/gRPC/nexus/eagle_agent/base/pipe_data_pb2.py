# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/eagle_agent/base/pipe_data.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&nexus/eagle_agent/base/pipe_data.proto\x12\x04pipe\"\xae\x01\n\x11\x43lusterIdentifier\x12\x12\n\ncluster_id\x18\x01 \x01(\x03\x12\x1e\n\x16\x63luster_incarnation_id\x18\x02 \x01(\x03\x12\x15\n\rsf_account_id\x18\x03 \x01(\t\x12\x12\n\nrigel_guid\x18\x04 \x01(\x03\x12\x18\n\x10global_tenant_id\x18\x05 \x01(\t\x12 \n\x18rigel_connector_group_id\x18\x06 \x01(\x03\"M\n\x15\x43lusterIdentifierList\x12\x34\n\x13\x63luster_identifiers\x18\x01 \x03(\x0b\x32\x17.pipe.ClusterIdentifier\"^\n\x16\x43ontrolPlaneApiRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x0f\n\x07request\x18\x02 \x01(\x0c\"+\n\x17\x43ontrolPlaneApiResponse\x12\x10\n\x08response\x18\x01 \x01(\x0c\"z\n\x19IrisDataCollectorResponse\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x11\n\tiris_data\x18\x02 \x01(\x0c\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\"\x1d\n\x1bSendIrisCollectorDataResult\"\xa6\x01\n\rSendAlertsArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x13\n\x0b\x61lerts_data\x18\x02 \x01(\x0c\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\x12\x1d\n\x15last_collection_usecs\x18\x04 \x01(\x03\x12\x15\n\ris_timeseries\x18\x05 \x01(\x08\"\x14\n\x12SendAlertsResponse\"\x7f\n\x14SendClusterConfigArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x1b\n\x13\x63luster_config_data\x18\x02 \x01(\x0c\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\"\x1b\n\x19SendClusterConfigResponse\"\x83\x01\n\x0cSendStatsArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x12\n\nstats_data\x18\x02 \x01(\x0c\x12\x13\n\x0bisLastBatch\x18\x03 \x01(\x08\x12\x15\n\ris_compressed\x18\x04 \x01(\x08\"\x13\n\x11SendStatsResponse\"~\n\x16SendHealthcheckDataArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x18\n\x10healthcheck_data\x18\x02 \x01(\x0c\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\"\x1d\n\x1bSendHealthcheckDataResponse\"t\n\x0fSendRunbooksArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x15\n\rrunbooks_data\x18\x02 \x01(\x0c\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\"\x16\n\x14SendRunbooksResponse\"Q\n\x1aQuorumRestrictedOpsRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\"+\n\x1bQuorumRestrictedOpsResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"B\n\x0b\x43lusterType\"3\n\x05Value\x12\x0c\n\x08kUnknown\x10\x00\x12\r\n\tkCohesity\x10\x01\x12\r\n\tkExternal\x10\x02\"V\n\x0f\x43lusterMetadata\x12\x14\n\x0credirect_url\x18\x01 \x01(\t\x12-\n\x0c\x63luster_type\x18\x02 \x01(\x0e\x32\x17.pipe.ClusterType.Value\"R\n\x11\x44\x61taplaneMetadata\x12\x31\n\x10\x63luster_metadata\x18\x01 \x01(\x0b\x32\x15.pipe.ClusterMetadataH\x00\x42\n\n\x08metadata\"\x87\x01\n\x1bHeliosAgentHeartBeatRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x33\n\x12\x64\x61taplane_metadata\x18\x02 \x01(\x0b\x32\x17.pipe.DataplaneMetadata\"\x1e\n\x1cHeliosAgentHeartBeatResponse\"S\n\x1cHeliosServerHeartBeatRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\"D\n\x1dHeliosServerHeartBeatResponse\x12#\n\x1b\x64\x61taplane_connection_status\x18\x01 \x01(\x0c\"\x87\x01\n\x10\x42ulletinBoardArg\x12\x17\n\x0fuser_account_id\x18\x01 \x01(\t\x12\x33\n\x12\x63luster_identifier\x18\x02 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x12\n\ntenant_ids\x18\x03 \x03(\t\x12\x11\n\tdata_keys\x18\x04 \x03(\x05\"Z\n\x16UpdateBulletinBoardArg\x12\x32\n\x12\x62ulletin_board_arg\x18\x01 \x01(\x0b\x32\x16.pipe.BulletinBoardArg\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x07\n\x05\x45mpty\"%\n\x15\x42ulletinBoardResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"5\n\x12\x41ppMetadataRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\x03\"0\n\x13\x41ppMetadataResponse\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0b\n\x03md5\x18\x02 \x01(\t\"U\n\x0f\x41ppChunkRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\x03\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x11\n\tchunkSize\x18\x04 \x01(\x03\"!\n\x10\x41ppChunkResponse\x12\r\n\x05\x63hunk\x18\x01 \x01(\x0c\"^\n\x13SnapshotDiffRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x12\n\nprepareArg\x18\x02 \x01(\x0c\"#\n\x14SnapshotDiffResponse\x12\x0b\n\x03key\x18\x01 \x01(\t\"]\n\x19SnapshotDiffStatusRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x0b\n\x03key\x18\x02 \x01(\t\"\x94\x01\n\x1aSnapshotDiffStatusResponse\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x06status\x18\x02 \x01(\x0e\x32\'.pipe.SnapshotDiffStatusResponse.Status\"0\n\x06Status\x12\x0b\n\x07RUNNING\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\"\xea\x01\n\nTenantInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08tenantId\x18\x03 \x01(\t\x12!\n\x19lastUpdatedTimeStampUsecs\x18\x04 \x01(\x03\x12\"\n\x06status\x18\x05 \x01(\x0e\x32\x12.pipe.TenantStatus\x12\x18\n\x10\x63onnectorEnabled\x18\x06 \x01(\x08\x12\x17\n\x0f\x63lusterHostname\x18\x07 \x01(\t\x12\x12\n\nclusterIps\x18\x08 \x03(\t\x12\x19\n\x11isManagedOnHelios\x18\t \x01(\x08\"\x80\x01\n\x17SendRigelHealthCheckArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x19\n\x11\x63onnectivity_data\x18\x02 \x01(\x0c\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\"\x1e\n\x1cSendRigelHealthCheckResponse\"K\n\x14GetClusterKeyRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\"=\n\x15GetClusterKeyResponse\x12\x13\n\x0b\x63luster_key\x18\x01 \x01(\x0c\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\"t\n\x13SendAuditLogDataArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x11\n\taudit_log\x18\x02 \x01(\x0c\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\"\x18\n\x16SendAuditLogDataResult\"h\n\x16SendNodesConfigDataArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x19\n\x11nodes_config_data\x18\x02 \x01(\x0c\"\x1b\n\x19SendNodesConfigDataResult\"Z\n\x11\x43lusterPairingArg\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x10\n\x08\x61ws_role\x18\x02 \x01(\t\"\x16\n\x14\x43lusterPairingResult\"s\n\"GetMagnetoUpcomingJobsStatsRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x18\n\x10time_period_secs\x18\x02 \x01(\x03\"l\n#GetMagnetoUpcomingJobsStatsResponse\x12\x1a\n\x12upcoming_job_count\x18\x01 \x01(\x05\x12\x18\n\x10time_period_secs\x18\x02 \x01(\x03\x12\x0f\n\x07\x65rr_msg\x18\x03 \x01(\t\"W\n\x16UpdateClusterConfigMap\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x19\n\x11storage_type_name\x18\x02 \x01(\t\x12\x13\n\x0bint32_value\x18\x03 \x01(\x05\"\xc8\x01\n\x1dSetupClusterForScalingRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.pipe.ClusterScalingRequestType\x12\x43\n\x1dupdate_cluster_config_map_vec\x18\x03 \x03(\x0b\x32\x1c.pipe.UpdateClusterConfigMap\"b\n\x1eSetupClusterForScalingResponse\x12\x0f\n\x07\x65rr_msg\x18\x01 \x01(\t\x12\x1c\n\x14\x65\x61gle_master_node_ip\x18\x02 \x01(\t\x12\x11\n\trss_usage\x18\x03 \x01(\x05\"%\n\x0bMinSelector\x12\x16\n\x0emin_ruleset_id\x18\x01 \x01(\x03\"#\n\x0cListSelector\x12\x13\n\x0bruleset_ids\x18\x01 \x03(\x03\"\x8e\x01\n\rSpecification\x12\x11\n\tvendor_id\x18\x01 \x01(\x03\x12)\n\x0cmin_selector\x18\x02 \x01(\x0b\x32\x11.pipe.MinSelectorH\x00\x12+\n\rlist_selector\x18\x03 \x01(\x0b\x32\x12.pipe.ListSelectorH\x00\x42\x12\n\x10ruleset_selector\"\x9f\x02\n\"TriggerSnapshotSecurityScanRequest\x12\x33\n\x12\x63luster_identifier\x18\x01 \x01(\x0b\x32\x17.pipe.ClusterIdentifier\x12\x1b\n\x13protection_group_id\x18\x02 \x01(\t\x12$\n\x1cprotection_group_instance_id\x18\x03 \x01(\x03\x12\x13\n\x0bsnapshot_id\x18\x04 \x01(\t\x12\x0f\n\x07scan_id\x18\x05 \x01(\t\x12+\n\x0especifications\x18\x06 \x03(\x0b\x32\x13.pipe.Specification\x12.\n&latest_ruleset_updated_timestamp_usecs\x18\x07 \x01(\x03\"\x92\x02\n#TriggerSnapshotSecurityScanResponse\x12\x1b\n\x13protection_group_id\x18\x01 \x01(\t\x12$\n\x1cprotection_group_instance_id\x18\x02 \x01(\x03\x12\x13\n\x0bsnapshot_id\x18\x03 \x01(\t\x12\x0f\n\x07scan_id\x18\x04 \x01(\t\x12@\n\x06status\x18\x05 \x01(\x0e\x32\x30.pipe.TriggerSnapshotSecurityScanResponse.Status\"@\n\x06Status\x12\x14\n\x10VALIDATION_ERROR\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x02*^\n\x0cTenantStatus\x12\n\n\x06\x41\x63tive\x10\x00\x12\x0c\n\x08Inactive\x10\x01\x12\x15\n\x11MarkedForDeletion\x10\x02\x12\x0b\n\x07\x44\x65leted\x10\x03\x12\x10\n\x0cUnregistered\x10\x04*\x90\x01\n\x19\x43lusterScalingRequestType\x12\x0b\n\x07INVALID\x10\x00\x12\x12\n\x0eREAD_ONLY_MODE\x10\x01\x12\x0f\n\x0b\x43LEAR_CACHE\x10\x02\x12\x19\n\x15UPDATE_CLUSTER_CONFIG\x10\x03\x12\x0f\n\x0bGET_RSS_MEM\x10\x04\x12\x15\n\x11SWITCH_MASTERSHIP\x10\x05\x42\x34\n\x18\x63om.cohesity.helios.pipeZ\x18\x63ohesity/prana/pipe/datab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.eagle_agent.base.pipe_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.cohesity.helios.pipeZ\030cohesity/prana/pipe/data'
  _globals['_TENANTSTATUS']._serialized_start=5324
  _globals['_TENANTSTATUS']._serialized_end=5418
  _globals['_CLUSTERSCALINGREQUESTTYPE']._serialized_start=5421
  _globals['_CLUSTERSCALINGREQUESTTYPE']._serialized_end=5565
  _globals['_CLUSTERIDENTIFIER']._serialized_start=49
  _globals['_CLUSTERIDENTIFIER']._serialized_end=223
  _globals['_CLUSTERIDENTIFIERLIST']._serialized_start=225
  _globals['_CLUSTERIDENTIFIERLIST']._serialized_end=302
  _globals['_CONTROLPLANEAPIREQUEST']._serialized_start=304
  _globals['_CONTROLPLANEAPIREQUEST']._serialized_end=398
  _globals['_CONTROLPLANEAPIRESPONSE']._serialized_start=400
  _globals['_CONTROLPLANEAPIRESPONSE']._serialized_end=443
  _globals['_IRISDATACOLLECTORRESPONSE']._serialized_start=445
  _globals['_IRISDATACOLLECTORRESPONSE']._serialized_end=567
  _globals['_SENDIRISCOLLECTORDATARESULT']._serialized_start=569
  _globals['_SENDIRISCOLLECTORDATARESULT']._serialized_end=598
  _globals['_SENDALERTSARG']._serialized_start=601
  _globals['_SENDALERTSARG']._serialized_end=767
  _globals['_SENDALERTSRESPONSE']._serialized_start=769
  _globals['_SENDALERTSRESPONSE']._serialized_end=789
  _globals['_SENDCLUSTERCONFIGARG']._serialized_start=791
  _globals['_SENDCLUSTERCONFIGARG']._serialized_end=918
  _globals['_SENDCLUSTERCONFIGRESPONSE']._serialized_start=920
  _globals['_SENDCLUSTERCONFIGRESPONSE']._serialized_end=947
  _globals['_SENDSTATSARG']._serialized_start=950
  _globals['_SENDSTATSARG']._serialized_end=1081
  _globals['_SENDSTATSRESPONSE']._serialized_start=1083
  _globals['_SENDSTATSRESPONSE']._serialized_end=1102
  _globals['_SENDHEALTHCHECKDATAARG']._serialized_start=1104
  _globals['_SENDHEALTHCHECKDATAARG']._serialized_end=1230
  _globals['_SENDHEALTHCHECKDATARESPONSE']._serialized_start=1232
  _globals['_SENDHEALTHCHECKDATARESPONSE']._serialized_end=1261
  _globals['_SENDRUNBOOKSARG']._serialized_start=1263
  _globals['_SENDRUNBOOKSARG']._serialized_end=1379
  _globals['_SENDRUNBOOKSRESPONSE']._serialized_start=1381
  _globals['_SENDRUNBOOKSRESPONSE']._serialized_end=1403
  _globals['_QUORUMRESTRICTEDOPSREQUEST']._serialized_start=1405
  _globals['_QUORUMRESTRICTEDOPSREQUEST']._serialized_end=1486
  _globals['_QUORUMRESTRICTEDOPSRESPONSE']._serialized_start=1488
  _globals['_QUORUMRESTRICTEDOPSRESPONSE']._serialized_end=1531
  _globals['_CLUSTERTYPE']._serialized_start=1533
  _globals['_CLUSTERTYPE']._serialized_end=1599
  _globals['_CLUSTERTYPE_VALUE']._serialized_start=1548
  _globals['_CLUSTERTYPE_VALUE']._serialized_end=1599
  _globals['_CLUSTERMETADATA']._serialized_start=1601
  _globals['_CLUSTERMETADATA']._serialized_end=1687
  _globals['_DATAPLANEMETADATA']._serialized_start=1689
  _globals['_DATAPLANEMETADATA']._serialized_end=1771
  _globals['_HELIOSAGENTHEARTBEATREQUEST']._serialized_start=1774
  _globals['_HELIOSAGENTHEARTBEATREQUEST']._serialized_end=1909
  _globals['_HELIOSAGENTHEARTBEATRESPONSE']._serialized_start=1911
  _globals['_HELIOSAGENTHEARTBEATRESPONSE']._serialized_end=1941
  _globals['_HELIOSSERVERHEARTBEATREQUEST']._serialized_start=1943
  _globals['_HELIOSSERVERHEARTBEATREQUEST']._serialized_end=2026
  _globals['_HELIOSSERVERHEARTBEATRESPONSE']._serialized_start=2028
  _globals['_HELIOSSERVERHEARTBEATRESPONSE']._serialized_end=2096
  _globals['_BULLETINBOARDARG']._serialized_start=2099
  _globals['_BULLETINBOARDARG']._serialized_end=2234
  _globals['_UPDATEBULLETINBOARDARG']._serialized_start=2236
  _globals['_UPDATEBULLETINBOARDARG']._serialized_end=2326
  _globals['_EMPTY']._serialized_start=2328
  _globals['_EMPTY']._serialized_end=2335
  _globals['_BULLETINBOARDRESPONSE']._serialized_start=2337
  _globals['_BULLETINBOARDRESPONSE']._serialized_end=2374
  _globals['_APPMETADATAREQUEST']._serialized_start=2376
  _globals['_APPMETADATAREQUEST']._serialized_end=2429
  _globals['_APPMETADATARESPONSE']._serialized_start=2431
  _globals['_APPMETADATARESPONSE']._serialized_end=2479
  _globals['_APPCHUNKREQUEST']._serialized_start=2481
  _globals['_APPCHUNKREQUEST']._serialized_end=2566
  _globals['_APPCHUNKRESPONSE']._serialized_start=2568
  _globals['_APPCHUNKRESPONSE']._serialized_end=2601
  _globals['_SNAPSHOTDIFFREQUEST']._serialized_start=2603
  _globals['_SNAPSHOTDIFFREQUEST']._serialized_end=2697
  _globals['_SNAPSHOTDIFFRESPONSE']._serialized_start=2699
  _globals['_SNAPSHOTDIFFRESPONSE']._serialized_end=2734
  _globals['_SNAPSHOTDIFFSTATUSREQUEST']._serialized_start=2736
  _globals['_SNAPSHOTDIFFSTATUSREQUEST']._serialized_end=2829
  _globals['_SNAPSHOTDIFFSTATUSRESPONSE']._serialized_start=2832
  _globals['_SNAPSHOTDIFFSTATUSRESPONSE']._serialized_end=2980
  _globals['_SNAPSHOTDIFFSTATUSRESPONSE_STATUS']._serialized_start=2932
  _globals['_SNAPSHOTDIFFSTATUSRESPONSE_STATUS']._serialized_end=2980
  _globals['_TENANTINFO']._serialized_start=2983
  _globals['_TENANTINFO']._serialized_end=3217
  _globals['_SENDRIGELHEALTHCHECKARG']._serialized_start=3220
  _globals['_SENDRIGELHEALTHCHECKARG']._serialized_end=3348
  _globals['_SENDRIGELHEALTHCHECKRESPONSE']._serialized_start=3350
  _globals['_SENDRIGELHEALTHCHECKRESPONSE']._serialized_end=3380
  _globals['_GETCLUSTERKEYREQUEST']._serialized_start=3382
  _globals['_GETCLUSTERKEYREQUEST']._serialized_end=3457
  _globals['_GETCLUSTERKEYRESPONSE']._serialized_start=3459
  _globals['_GETCLUSTERKEYRESPONSE']._serialized_end=3520
  _globals['_SENDAUDITLOGDATAARG']._serialized_start=3522
  _globals['_SENDAUDITLOGDATAARG']._serialized_end=3638
  _globals['_SENDAUDITLOGDATARESULT']._serialized_start=3640
  _globals['_SENDAUDITLOGDATARESULT']._serialized_end=3664
  _globals['_SENDNODESCONFIGDATAARG']._serialized_start=3666
  _globals['_SENDNODESCONFIGDATAARG']._serialized_end=3770
  _globals['_SENDNODESCONFIGDATARESULT']._serialized_start=3772
  _globals['_SENDNODESCONFIGDATARESULT']._serialized_end=3799
  _globals['_CLUSTERPAIRINGARG']._serialized_start=3801
  _globals['_CLUSTERPAIRINGARG']._serialized_end=3891
  _globals['_CLUSTERPAIRINGRESULT']._serialized_start=3893
  _globals['_CLUSTERPAIRINGRESULT']._serialized_end=3915
  _globals['_GETMAGNETOUPCOMINGJOBSSTATSREQUEST']._serialized_start=3917
  _globals['_GETMAGNETOUPCOMINGJOBSSTATSREQUEST']._serialized_end=4032
  _globals['_GETMAGNETOUPCOMINGJOBSSTATSRESPONSE']._serialized_start=4034
  _globals['_GETMAGNETOUPCOMINGJOBSSTATSRESPONSE']._serialized_end=4142
  _globals['_UPDATECLUSTERCONFIGMAP']._serialized_start=4144
  _globals['_UPDATECLUSTERCONFIGMAP']._serialized_end=4231
  _globals['_SETUPCLUSTERFORSCALINGREQUEST']._serialized_start=4234
  _globals['_SETUPCLUSTERFORSCALINGREQUEST']._serialized_end=4434
  _globals['_SETUPCLUSTERFORSCALINGRESPONSE']._serialized_start=4436
  _globals['_SETUPCLUSTERFORSCALINGRESPONSE']._serialized_end=4534
  _globals['_MINSELECTOR']._serialized_start=4536
  _globals['_MINSELECTOR']._serialized_end=4573
  _globals['_LISTSELECTOR']._serialized_start=4575
  _globals['_LISTSELECTOR']._serialized_end=4610
  _globals['_SPECIFICATION']._serialized_start=4613
  _globals['_SPECIFICATION']._serialized_end=4755
  _globals['_TRIGGERSNAPSHOTSECURITYSCANREQUEST']._serialized_start=4758
  _globals['_TRIGGERSNAPSHOTSECURITYSCANREQUEST']._serialized_end=5045
  _globals['_TRIGGERSNAPSHOTSECURITYSCANRESPONSE']._serialized_start=5048
  _globals['_TRIGGERSNAPSHOTSECURITYSCANRESPONSE']._serialized_end=5322
  _globals['_TRIGGERSNAPSHOTSECURITYSCANRESPONSE_STATUS']._serialized_start=5258
  _globals['_TRIGGERSNAPSHOTSECURITYSCANRESPONSE_STATUS']._serialized_end=5322
# @@protoc_insertion_point(module_scope)
