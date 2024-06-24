# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yoda/base/reports.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.snap_fs.utils import track_data_pb2 as bridge_dot_snap__fs_dot_utils_dot_track__data__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from yoda.base import yoda_types_pb2 as yoda_dot_base_dot_yoda__types__pb2
from yoda.base import volume_info_pb2 as yoda_dot_base_dot_volume__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17yoda/base/reports.proto\x12\rcohesity.yoda\x1a%bridge/snap_fs/utils/track_data.proto\x1a\x19magneto/base/entity.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1ayoda/base/yoda_types.proto\x1a\x1byoda/base/volume_info.proto\"8\n\x06OSType\".\n\x04Type\x12\x0c\n\x08kUnknown\x10\x00\x12\n\n\x06kLinux\x10\x01\x12\x0c\n\x08kWindows\x10\x02\"\xa2\x01\n\x0fTimestampedSize\x12\x1b\n\x13snapshot_time_usecs\x18\x01 \x02(\x03\x12\x1a\n\x12logical_size_bytes\x18\x02 \x02(\x03\x12\x17\n\x0cobject_count\x18\x03 \x01(\x03:\x01\x31\x12#\n\x1bprimary_physical_size_bytes\x18\x04 \x01(\x03\x12\x18\n\x10\x64\x65lta_size_bytes\x18\x05 \x01(\x03\"U\n\x0f\x45ntityUsageInfo\x12\x13\n\x0bobject_name\x18\x01 \x02(\t\x12-\n\x05usage\x18\x03 \x03(\x0b\x32\x1e.cohesity.yoda.TimestampedSize\"\xa5\x01\n\x14ObjectTopFilesReport\x12\x39\n\x11top_files_by_size\x18\x01 \x03(\x0b\x32\x1e.cohesity.yoda.EntityUsageInfo2R\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18\x65 \x01(\x0b\x32#.cohesity.yoda.ObjectTopFilesReport\"\xc9\x03\n\x0eTopFilesReport\x12\x36\n\ttop_files\x18\x01 \x03(\x0b\x32#.cohesity.yoda.TopFilesReport.Entry\x1a\xb0\x02\n\x05\x45ntry\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x30\n\tobject_id\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x38\n\x11registered_source\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x1e\n\x16registered_source_hash\x18\x04 \x01(\x04\x12\x13\n\x0bview_box_id\x18\x05 \x01(\x03\x12\'\n\x1flatest_snapshot_timestamp_usecs\x18\x06 \x01(\x03\x12\x1a\n\x12logical_size_bytes\x18\x07 \x01(\x03\x12/\n\x07history\x18\t \x03(\x0b\x32\x1e.cohesity.yoda.TimestampedSize2L\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18g \x01(\x0b\x32\x1d.cohesity.yoda.TopFilesReport\"\xa4\x01\n\x13\x43\x61tegoryUsageReport\x12:\n\x12\x63\x61tegories_by_size\x18\x01 \x03(\x0b\x32\x1e.cohesity.yoda.EntityUsageInfo2Q\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18\x66 \x01(\x0b\x32\".cohesity.yoda.CategoryUsageReport\"\x94\x02\n\x12SourceGrowthReport\x12\x38\n\x07sources\x18\x01 \x03(\x0b\x32\'.cohesity.yoda.SourceGrowthReport.Entry\x1ar\n\x05\x45ntry\x12\x38\n\x11registered_source\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12/\n\x07history\x18\x02 \x03(\x0b\x32\x1e.cohesity.yoda.TimestampedSize2P\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18h \x01(\x0b\x32!.cohesity.yoda.SourceGrowthReport\"\x81\x02\n\x0cObjectReport\x12\x35\n\nobject_ids\x18\x01 \x03(\x0b\x32!.cohesity.yoda.ObjectReport.Entry\x1an\n\x05\x45ntry\x12\x34\n\tobject_id\x18\x01 \x02(\x0b\x32!.cohesity.magneto.MagnetoObjectId\x12/\n\x07history\x18\x02 \x03(\x0b\x32\x1e.cohesity.yoda.TimestampedSize2J\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18i \x01(\x0b\x32\x1b.cohesity.yoda.ObjectReport\"\x9b\x01\n\x0cOSTypeReport\x12+\n\x07os_type\x18\x01 \x02(\x0e\x32\x1a.cohesity.yoda.OSType.Type\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x32J\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18j \x01(\x0b\x32\x1b.cohesity.yoda.OSTypeReport\"\x8d\t\n\x13VolumeMappingReport\x12\x44\n\x0cmapping_work\x18\x01 \x01(\x0e\x32..cohesity.yoda.VolumeMappingReport.MappingWork\x12:\n\x0binstance_id\x18\x02 \x01(\x0b\x32%.cohesity.yoda.base.MagnetoInstanceId\x12>\n\x0finstance_id_vec\x18\x05 \x03(\x0b\x32%.cohesity.yoda.base.MagnetoInstanceId\x12;\n\nvolume_map\x18\x03 \x01(\x0b\x32\'.cohesity.yoda.volumeutil.VolumeNameMap\x12?\n\x10\x62\x61se_instance_id\x18\x04 \x01(\x0b\x32%.cohesity.yoda.base.MagnetoInstanceId\x12\x1b\n\x13skip_disk_or_volume\x18\x06 \x01(\x08\x12>\n\x10\x62oot_volume_info\x18\x07 \x01(\x0b\x32$.cohesity.yoda.volumeutil.VolumeInfo\x12#\n\x1bvol_mapping_file_mtime_secs\x18\x08 \x01(\x03\x12j\n!volume_mount_io_info_mapping_work\x18\t \x01(\x0e\x32?.cohesity.yoda.VolumeMappingReport.VolumeMountIOInfoMappingWork\x12V\n\x18volume_mount_io_info_map\x18\n \x01(\x0b\x32\x34.cohesity.yoda.VolumeMappingReport.VolumeMountIOInfo\x1a\xde\x01\n\x11VolumeMountIOInfo\x12\x66\n\x12volume_mount_reads\x18\x01 \x03(\x0b\x32J.cohesity.yoda.VolumeMappingReport.VolumeMountIOInfo.VolumeMountReadsEntry\x1a\x61\n\x15VolumeMountReadsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.cohesity.bridge.snap_fs.ReadIODataProto:\x02\x38\x01\"D\n\x0bMappingWork\x12\x0f\n\x0bkAddMapping\x10\x01\x12\x10\n\x0ckCopyMapping\x10\x02\x12\x12\n\x0ekRemoveMapping\x10\x03\"v\n\x1cVolumeMountIOInfoMappingWork\x12\x1a\n\x16kAddMountIOInfoMapping\x10\x01\x12\x1b\n\x17kCopyMountIOInfoMapping\x10\x02\x12\x1d\n\x19kRemoveMountIOInfoMapping\x10\x03\x32Q\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18k \x01(\x0b\x32\".cohesity.yoda.VolumeMappingReport\"p\n\x12VolumeIndexingInfo\x12\x13\n\x0bvolume_name\x18\x01 \x01(\t\x12\x1b\n\x13num_entries_indexed\x18\x02 \x01(\x03\x12(\n time_taken_in_vol_indexing_usecs\x18\x03 \x01(\x03\"\xcf\x02\n\x10VMIndexingReport\x12:\n\x0binstance_id\x18\x01 \x01(\x0b\x32%.cohesity.yoda.base.MagnetoInstanceId\x12!\n\x19num_undetected_partitions\x18\x02 \x01(\x05\x12$\n\x1ctime_taken_in_indexing_usecs\x18\x03 \x01(\x03\x12\x1b\n\x13num_entries_indexed\x18\x04 \x01(\x03\x12\x36\n\x0bvolume_info\x18\x05 \x03(\x0b\x32!.cohesity.yoda.VolumeIndexingInfo\x12\x11\n\ttenant_id\x18\x06 \x01(\t2N\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18l \x01(\x0b\x32\x1f.cohesity.yoda.VMIndexingReport\"\xa6\x02\n\x11ObjectIndexReport\x12@\n\x10index_report_vec\x18\x01 \x03(\x0b\x32&.cohesity.yoda.ObjectIndexReport.Entry\x1a~\n\x05\x45ntry\x12\x34\n\tobject_id\x18\x01 \x01(\x0b\x32!.cohesity.magneto.MagnetoObjectId\x12\x1c\n\x14num_detected_volumes\x18\x02 \x01(\x05\x12!\n\x19num_undetected_partitions\x18\x03 \x01(\x05\x32O\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18m \x01(\x0b\x32 .cohesity.yoda.ObjectIndexReport\"N\n\x15\x44irectoryIndexingInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12\x18\n\x10time_taken_usecs\x18\x03 \x01(\x03\"\xac\x01\n\x15SlowDirectoriesReport\x12>\n\x10slow_directories\x18\x01 \x03(\x0b\x32$.cohesity.yoda.DirectoryIndexingInfo2S\n\nreport_ext\x12\x19.cohesity.yoda.YodaReport\x18n \x01(\x0b\x32$.cohesity.yoda.SlowDirectoriesReport\"G\n\nYodaReport\x12\x1a\n\x12\x44\x45PRECATED_version\x18\x01 \x01(\x03\x12\x13\n\x0binstance_id\x18\x02 \x01(\x03*\x08\x08\x64\x10\x80\x80\x80\x80\x02\x42\x16Z\x14yoda/base/reports.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yoda.base.reports_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\024yoda/base/reports.pb'
  _globals['_VOLUMEMAPPINGREPORT_VOLUMEMOUNTIOINFO_VOLUMEMOUNTREADSENTRY']._loaded_options = None
  _globals['_VOLUMEMAPPINGREPORT_VOLUMEMOUNTIOINFO_VOLUMEMOUNTREADSENTRY']._serialized_options = b'8\001'
  _globals['_OSTYPE']._serialized_start=193
  _globals['_OSTYPE']._serialized_end=249
  _globals['_OSTYPE_TYPE']._serialized_start=203
  _globals['_OSTYPE_TYPE']._serialized_end=249
  _globals['_TIMESTAMPEDSIZE']._serialized_start=252
  _globals['_TIMESTAMPEDSIZE']._serialized_end=414
  _globals['_ENTITYUSAGEINFO']._serialized_start=416
  _globals['_ENTITYUSAGEINFO']._serialized_end=501
  _globals['_OBJECTTOPFILESREPORT']._serialized_start=504
  _globals['_OBJECTTOPFILESREPORT']._serialized_end=669
  _globals['_TOPFILESREPORT']._serialized_start=672
  _globals['_TOPFILESREPORT']._serialized_end=1129
  _globals['_TOPFILESREPORT_ENTRY']._serialized_start=747
  _globals['_TOPFILESREPORT_ENTRY']._serialized_end=1051
  _globals['_CATEGORYUSAGEREPORT']._serialized_start=1132
  _globals['_CATEGORYUSAGEREPORT']._serialized_end=1296
  _globals['_SOURCEGROWTHREPORT']._serialized_start=1299
  _globals['_SOURCEGROWTHREPORT']._serialized_end=1575
  _globals['_SOURCEGROWTHREPORT_ENTRY']._serialized_start=1379
  _globals['_SOURCEGROWTHREPORT_ENTRY']._serialized_end=1493
  _globals['_OBJECTREPORT']._serialized_start=1578
  _globals['_OBJECTREPORT']._serialized_end=1835
  _globals['_OBJECTREPORT_ENTRY']._serialized_start=1649
  _globals['_OBJECTREPORT_ENTRY']._serialized_end=1759
  _globals['_OSTYPEREPORT']._serialized_start=1838
  _globals['_OSTYPEREPORT']._serialized_end=1993
  _globals['_VOLUMEMAPPINGREPORT']._serialized_start=1996
  _globals['_VOLUMEMAPPINGREPORT']._serialized_end=3161
  _globals['_VOLUMEMAPPINGREPORT_VOLUMEMOUNTIOINFO']._serialized_start=2666
  _globals['_VOLUMEMAPPINGREPORT_VOLUMEMOUNTIOINFO']._serialized_end=2888
  _globals['_VOLUMEMAPPINGREPORT_VOLUMEMOUNTIOINFO_VOLUMEMOUNTREADSENTRY']._serialized_start=2791
  _globals['_VOLUMEMAPPINGREPORT_VOLUMEMOUNTIOINFO_VOLUMEMOUNTREADSENTRY']._serialized_end=2888
  _globals['_VOLUMEMAPPINGREPORT_MAPPINGWORK']._serialized_start=2890
  _globals['_VOLUMEMAPPINGREPORT_MAPPINGWORK']._serialized_end=2958
  _globals['_VOLUMEMAPPINGREPORT_VOLUMEMOUNTIOINFOMAPPINGWORK']._serialized_start=2960
  _globals['_VOLUMEMAPPINGREPORT_VOLUMEMOUNTIOINFOMAPPINGWORK']._serialized_end=3078
  _globals['_VOLUMEINDEXINGINFO']._serialized_start=3163
  _globals['_VOLUMEINDEXINGINFO']._serialized_end=3275
  _globals['_VMINDEXINGREPORT']._serialized_start=3278
  _globals['_VMINDEXINGREPORT']._serialized_end=3613
  _globals['_OBJECTINDEXREPORT']._serialized_start=3616
  _globals['_OBJECTINDEXREPORT']._serialized_end=3910
  _globals['_OBJECTINDEXREPORT_ENTRY']._serialized_start=3703
  _globals['_OBJECTINDEXREPORT_ENTRY']._serialized_end=3829
  _globals['_DIRECTORYINDEXINGINFO']._serialized_start=3912
  _globals['_DIRECTORYINDEXINGINFO']._serialized_end=3990
  _globals['_SLOWDIRECTORIESREPORT']._serialized_start=3993
  _globals['_SLOWDIRECTORIESREPORT']._serialized_end=4165
  _globals['_YODAREPORT']._serialized_start=4167
  _globals['_YODAREPORT']._serialized_end=4238
# @@protoc_insertion_point(module_scope)
