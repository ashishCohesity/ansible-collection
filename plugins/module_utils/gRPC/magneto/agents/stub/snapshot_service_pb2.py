# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/agents/stub/snapshot_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*magneto/agents/stub/snapshot_service.proto\x12\x1c\x63ohesity.magneto.agents.stub\"\xb0\x03\n\nVolumeInfo\x12\x0c\n\x04guid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1a\n\x12last_snapshot_uuid\x18\x03 \x01(\t\x12!\n\x19last_snapshot_time_micros\x18\x04 \x01(\x03\x12 \n\x18last_snapshot_size_bytes\x18\x05 \x01(\x03\x12#\n\x14is_snapshot_readable\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x46\n\ndelta_info\x18\x07 \x01(\x0b\x32\x32.cohesity.magneto.agents.stub.VolumeInfo.DeltaInfo\x12&\n\x1esnapshot_backup_components_xml\x18\x08 \x01(\x0c\x12$\n\x1csnapshot_writer_metadata_xml\x18\t \x01(\x0c\x12\x17\n\x0fsnapshot_device\x18\n \x01(\t\x1aQ\n\tDeltaInfo\x12\x1a\n\x12\x62\x61se_snapshot_uuid\x18\x01 \x01(\t\x12\x18\n\x10\x62lock_size_bytes\x18\x02 \x01(\x05\x12\x0e\n\x06\x62itmap\x18\x03 \x01(\x0c\"=\n\x0fQueryVolumesArg\x12*\n\x1brestrict_to_tracked_volumes\x18\x01 \x01(\x08:\x05\x66\x61lse\"R\n\x12QueryVolumesResult\x12<\n\nvolume_vec\x18\x01 \x03(\x0b\x32(.cohesity.magneto.agents.stub.VolumeInfo\"\xc5\x01\n\x12SnapshotVolumesArg\x12K\n\nvolume_vec\x18\x01 \x03(\x0b\x32\x37.cohesity.magneto.agents.stub.SnapshotVolumesArg.Volume\x12,\n\x1dinclude_volume_info_in_result\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x14\x65xcluded_vss_writers\x18\x03 \x03(\x0c\x1a\x16\n\x06Volume\x12\x0c\n\x04guid\x18\x01 \x02(\t\"\x90\x02\n\x15SnapshotVolumesResult\x12V\n\x0csnapshot_vec\x18\x01 \x03(\x0b\x32@.cohesity.magneto.agents.stub.SnapshotVolumesResult.SnapshotInfo\x1a\x9e\x01\n\x0cSnapshotInfo\x12\x0c\n\x04guid\x18\x01 \x02(\t\x12\x14\n\x05\x65rror\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x15\n\rsnapshot_uuid\x18\x03 \x01(\t\x12:\n\x08vol_info\x18\x04 \x01(\x0b\x32(.cohesity.magneto.agents.stub.VolumeInfo\x12\x17\n\x0fsnapshot_device\x18\x05 \x01(\t\"\x8f\x01\n\x13ReleaseSnapshotsArg\x12J\n\tentry_vec\x18\x01 \x03(\x0b\x32\x37.cohesity.magneto.agents.stub.ReleaseSnapshotsArg.Entry\x1a,\n\x05\x45ntry\x12\x0c\n\x04guid\x18\x01 \x01(\t\x12\x15\n\rsnapshot_uuid\x18\x02 \x01(\t\",\n\x15StopTrackingVolumeArg\x12\x13\n\x0bvolume_guid\x18\x01 \x01(\t\"\x1a\n\x18StopTrackingVolumeResult\",\n\x16ReleaseSnapshotsResult\x12\x12\n\nstatus_vec\x18\x01 \x03(\x08\x32\xfd\x03\n\x0fSnapshotService\x12o\n\x0cQueryVolumes\x12-.cohesity.magneto.agents.stub.QueryVolumesArg\x1a\x30.cohesity.magneto.agents.stub.QueryVolumesResult\x12x\n\x0fSnapshotVolumes\x12\x30.cohesity.magneto.agents.stub.SnapshotVolumesArg\x1a\x33.cohesity.magneto.agents.stub.SnapshotVolumesResult\x12{\n\x10ReleaseSnapshots\x12\x31.cohesity.magneto.agents.stub.ReleaseSnapshotsArg\x1a\x34.cohesity.magneto.agents.stub.ReleaseSnapshotsResult\x12\x81\x01\n\x12StopTrackingVolume\x12\x33.cohesity.magneto.agents.stub.StopTrackingVolumeArg\x1a\x36.cohesity.magneto.agents.stub.StopTrackingVolumeResult')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.agents.stub.snapshot_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VOLUMEINFO']._serialized_start=77
  _globals['_VOLUMEINFO']._serialized_end=509
  _globals['_VOLUMEINFO_DELTAINFO']._serialized_start=428
  _globals['_VOLUMEINFO_DELTAINFO']._serialized_end=509
  _globals['_QUERYVOLUMESARG']._serialized_start=511
  _globals['_QUERYVOLUMESARG']._serialized_end=572
  _globals['_QUERYVOLUMESRESULT']._serialized_start=574
  _globals['_QUERYVOLUMESRESULT']._serialized_end=656
  _globals['_SNAPSHOTVOLUMESARG']._serialized_start=659
  _globals['_SNAPSHOTVOLUMESARG']._serialized_end=856
  _globals['_SNAPSHOTVOLUMESARG_VOLUME']._serialized_start=834
  _globals['_SNAPSHOTVOLUMESARG_VOLUME']._serialized_end=856
  _globals['_SNAPSHOTVOLUMESRESULT']._serialized_start=859
  _globals['_SNAPSHOTVOLUMESRESULT']._serialized_end=1131
  _globals['_SNAPSHOTVOLUMESRESULT_SNAPSHOTINFO']._serialized_start=973
  _globals['_SNAPSHOTVOLUMESRESULT_SNAPSHOTINFO']._serialized_end=1131
  _globals['_RELEASESNAPSHOTSARG']._serialized_start=1134
  _globals['_RELEASESNAPSHOTSARG']._serialized_end=1277
  _globals['_RELEASESNAPSHOTSARG_ENTRY']._serialized_start=1233
  _globals['_RELEASESNAPSHOTSARG_ENTRY']._serialized_end=1277
  _globals['_STOPTRACKINGVOLUMEARG']._serialized_start=1279
  _globals['_STOPTRACKINGVOLUMEARG']._serialized_end=1323
  _globals['_STOPTRACKINGVOLUMERESULT']._serialized_start=1325
  _globals['_STOPTRACKINGVOLUMERESULT']._serialized_end=1351
  _globals['_RELEASESNAPSHOTSRESULT']._serialized_start=1353
  _globals['_RELEASESNAPSHOTSRESULT']._serialized_end=1397
  _globals['_SNAPSHOTSERVICE']._serialized_start=1400
  _globals['_SNAPSHOTSERVICE']._serialized_end=1909
# @@protoc_insertion_point(module_scope)
