# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nexus/eagle_agent/base/eagle_agent_uris.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-nexus/eagle_agent/base/eagle_agent_uris.proto\x12\x1b\x63ohesity.nexus.helios.agent\"\xb9\x0e\n\x14HeliosAgentUrisProto\x12\x1f\n\x08\x62\x61se_uri\x18\x01 \x01(\t:\r/heliosAgent/\x12\x17\n\x0b\x61pi_version\x18\x02 \x01(\t:\x02v1\x12+\n\x12support_bundle_uri\x18\x03 \x01(\t:\x0f/support/bundle\x12!\n\x0bmaster_info\x18\x04 \x01(\t:\x0c/master/info\x12\x31\n\x12helios_conn_status\x18\x05 \x01(\t:\x15/master/helios/status\x12$\n\x0c\x61udit_report\x18\x06 \x01(\t:\x0e/license/audit\x12(\n\x11send_magneto_data\x18\x07 \x01(\t:\r/data/magneto\x12\"\n\x0esend_iris_data\x18\x08 \x01(\t:\n/data/iris\x12*\n\x12stats_metrics_data\x18\t \x01(\t:\x0e/stats/metrics\x12(\n\x13simulation_base_uri\x18\x64 \x01(\t:\x0b/simulation\x12\x36\n\x1dsimulation_cluster_create_uri\x18\x65 \x01(\t:\x0f/cluster/create\x12\x34\n\x1csimulation_cluster_claim_uri\x18\x66 \x01(\t:\x0e/cluster/claim\x12:\n simulation_alerts_generation_uri\x18g \x01(\t:\x10/generate/alerts\x12@\n)simulation_create_proxy_configuration_uri\x18h \x01(\t:\r/create/proxy\x12@\n)simulation_remove_proxy_configuration_uri\x18i \x01(\t:\r/remove/proxy\x12&\n\x0e\x62ulletin_board\x18j \x01(\t:\x0e/bulletinBoard\x12\x34\n\x17\x61pp_download_status_uri\x18k \x01(\t:\x13/app/downloadStatus\x12/\n\x12unregister_cluster\x18l \x01(\t:\x13/cluster/unregister\x12#\n\x0eunregister_uri\x18m \x01(\t:\x0b/unregister\x12(\n\x13\x63hange_id_reset_uri\x18n \x01(\t:\x0b/data/reset\x12\x35\n\x1fsimulation_get_cluster_data_uri\x18o \x01(\t:\x0c/clusterData\x12(\n\x11snapshot_diff_uri\x18p \x01(\t:\r/snapshotDiff\x12\x36\n\x16refresh_bulletin_board\x18q \x01(\t:\x16/bulletinBoard/refresh\x12\x31\n\x13helios_proxy_config\x18r \x01(\t:\x14/helios/proxy/config\x12\x32\n\x14healthcheck_data_uri\x18s \x01(\t:\x14/healthcheck/collect\x12=\n\x16rigel_maintenance_mode\x18t \x01(\t:\x1d/helios/rigel/maintenanceMode\x12\x1d\n\x0bmetrics_uri\x18u \x01(\t:\x08/metrics\x12\"\n\x0cutility_apps\x18v \x01(\t:\x0c/utilityApps\x12!\n\nrpaas_base\x18w \x01(\t:\r/helios/rpaas\x12 \n\x0bpairing_key\x18x \x01(\t:\x0b/pairingKey\x12\x37\n\x19\x61uthenticate_aws_role_uri\x18y \x01(\t:\x14/authenticateAwsRole\x12\x34\n\x11rigel_s3_endpoint\x18z \x01(\t:\x19/helios/rigel/s3-endpoint\x12)\n\x0fhelios_endpoint\x18{ \x01(\t:\x10/helios/endpoint\x12-\n\x0e\x62ring_up_rigel\x18| \x01(\t:\x15/helios/rigel/bringup\x12*\n\x12s3_credentials_uri\x18} \x01(\t:\x0e/s3Credentials\x12,\n\x13kms_credentials_uri\x18~ \x01(\t:\x0f/kmsCredentials\x12\'\n\rfortknox_base\x18\x7f \x01(\t:\x10/helios/fortknox\x12>\n\x1cobject_store_credentials_uri\x18\x80\x01 \x01(\t:\x17/objectStoreCredentials\x12;\n\x18\x63reate_agent_certificate\x18\x81\x01 \x01(\t:\x18/heliosAgent/certificateBF\n\x18\x63om.cohesity.helios.pipeZ*nexus/eagle_agent/base/eagle_agent_uris.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nexus.eagle_agent.base.eagle_agent_uris_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.cohesity.helios.pipeZ*nexus/eagle_agent/base/eagle_agent_uris.pb'
  _globals['_HELIOSAGENTURISPROTO']._serialized_start=79
  _globals['_HELIOSAGENTURISPROTO']._serialized_end=1928
# @@protoc_insertion_point(module_scope)
