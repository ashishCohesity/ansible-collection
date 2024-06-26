# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/agents/windows/stub/hyperv_param.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.agents.base import error_pb2 as magneto_dot_agents_dot_base_dot_error__pb2
from magneto.agents.stub import agent_base_pb2 as magneto_dot_agents_dot_stub_dot_agent__base__pb2
from magneto.agents.windows.base import hyperv_pb2 as magneto_dot_agents_dot_windows_dot_base_dot_hyperv__pb2
from magneto.base import credentials_pb2 as magneto_dot_base_dot_credentials__pb2
from magneto.base.entities import hyperv_pb2 as magneto_dot_base_dot_entities_dot_hyperv__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from util import cbt_delta_pb2 as util_dot_cbt__delta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.magneto/agents/windows/stub/hyperv_param.proto\x12$cohesity.magneto.agents.windows.stub\x1a\x1fmagneto/agents/base/agent.proto\x1a\x1fmagneto/agents/base/error.proto\x1a$magneto/agents/stub/agent_base.proto\x1a(magneto/agents/windows/base/hyperv.proto\x1a\x1emagneto/base/credentials.proto\x1a\"magneto/base/entities/hyperv.proto\x1a\x1amagneto/base/magneto.proto\x1a\x14util/cbt_delta.proto\"~\n\x12HyperVAccessParams\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x32\n\x04type\x18\x04 \x01(\x0e\x32$.cohesity.magneto.hyperv.Entity.Type\"\xad\x03\n\x17HyperVGuestAccessParams\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x14\n\x0chyperv_vm_id\x18\x04 \x01(\t\x12\x16\n\x08is_guest\x18\x05 \x01(\x08:\x04true\x12\x11\n\texec_path\x18\x06 \x01(\t\x12`\n\rguest_os_type\x18\x07 \x01(\x0e\x32I.cohesity.magneto.agents.windows.stub.HyperVGuestAccessParams.GuestOsType\x12M\n\x0c\x61\x63\x63\x65ss_state\x18\x08 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.stub.HyperVAccessState\x12\x1b\n\x13\x61\x64\x64itional_rpc_args\x18\t \x01(\t\x12\x16\n\x0eip_address_vec\x18\n \x03(\t\"5\n\x0bGuestOsType\x12\x0c\n\x08kWindows\x10\x01\x12\n\n\x06kLinux\x10\x02\x12\x0c\n\x08kUnknown\x10\x03\">\n\x11HyperVAccessState\x12\x12\n\nprocess_id\x18\x01 \x01(\r\x12\x15\n\rguest_tmp_dir\x18\x02 \x01(\t\"\xe3\x01\n\x15GetHyperVHierarchyArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12%\n\x16return_unsupported_vms\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07minimal\x18\x04 \x01(\x08:\x05\x66\x61lse\"\x90\x01\n\x18GetHyperVHierarchyResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12@\n\x10\x65ntity_hierarchy\x18\x02 \x01(\x0b\x32&.cohesity.magneto.EntityHierarchyProto\"\xae\x02\n\x15\x43reateVMCheckpointArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x14\n\x0chyperv_vm_id\x18\x03 \x01(\t\x12\x17\n\x0f\x63heckpoint_name\x18\x04 \x01(\t\x12\x0f\n\x07quiesce\x18\x05 \x01(\x08\x12\'\n\x1f\x61llow_crash_consistent_snapshot\x18\x06 \x01(\x08\x12\x1f\n\x10is_vss_copy_only\x18\x07 \x01(\x08:\x05\x66\x61lse\"\x89\x01\n\x18\x43reateVMCheckpointResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x1e\n\x16\x63heckpoint_instance_id\x18\x02 \x01(\x0c\x12\x19\n\x11is_app_consistent\x18\x03 \x01(\x08\"\xda\x01\n\x15\x44\x65leteVMCheckpointArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x14\n\x0chyperv_vm_id\x18\x03 \x01(\t\x12\x1e\n\x16\x63heckpoint_instance_id\x18\x04 \x01(\x0c\"N\n\x18\x44\x65leteVMCheckpointResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xf3\x02\n\x14GetCheckpointInfoArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x14\n\x0chyperv_vm_id\x18\x03 \x01(\t\x12\x1e\n\x16\x63heckpoint_instance_id\x18\x04 \x01(\x0c\x12K\n\x1ahyperv_disk_exclusion_info\x18\x05 \x03(\x0b\x32\'.cohesity.magneto.HyperVDiskFilterProto\x12K\n\x1ahyperv_disk_inclusion_info\x18\x06 \x03(\x0b\x32\'.cohesity.magneto.HyperVDiskFilterProto\"\xe5\x01\n\x17GetCheckpointInfoResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12O\n\x0f\x63heckpoint_info\x18\x02 \x01(\x0b\x32\x36.cohesity.magneto.agents.windows.hyperv.CheckpointInfo\x12\x45\n\x07vm_info\x18\x03 \x01(\x0b\x32\x34.cohesity.magneto.agents.windows.hyperv.HyperVVMInfo\"\xd1\x01\n\x18GetCheckpointVMConfigArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12P\n\x12vm_config_file_vec\x18\x02 \x03(\x0b\x32\x34.cohesity.magneto.agents.windows.hyperv.VMConfigFile\x12\'\n\x19\x66\x61il_on_large_config_file\x18\x03 \x01(\x08:\x04true\"\xb2\x01\n\x1bGetCheckpointVMConfigResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12Y\n\x17vm_config_file_info_vec\x18\x03 \x03(\x0b\x32\x38.cohesity.magneto.agents.windows.hyperv.VMConfigFileInfoJ\x04\x08\x02\x10\x03\"\xab\x01\n\x0bLocateVMArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x0f\n\x07vm_uuid\x18\x03 \x01(\x0c\"\x8b\x01\n\x0eLocateVMResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x45\n\x07vm_info\x18\x02 \x01(\x0b\x32\x34.cohesity.magneto.agents.windows.hyperv.HyperVVMInfo\"\xa7\x01\n\x18GetVirtualDiskChangesArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x16\n\x0e\x64isk_full_path\x18\x02 \x01(\t\x12\x17\n\x0fprevious_rct_id\x18\x03 \x01(\x0c\x12\x0e\n\x06offset\x18\x04 \x01(\x04\x12\x0e\n\x06length\x18\x05 \x01(\x04\"\xb8\x01\n\x1bGetVirtualDiskChangesResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x34\n\ndelta_type\x18\x02 \x01(\x0e\x32 .cohesity.util.CBTDeltaType.Type\x12/\n\ndelta_info\x18\x03 \x01(\x0b\x32\x1b.cohesity.util.CBTDeltaInfo\"\xe9\x01\n\x12ReadVirtualDiskArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x16\n\x0e\x64isk_full_path\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x0e\n\x06length\x18\x04 \x01(\x04\x12)\n\x1aoptimize_zero_filled_reads\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x34\n\trpc_stats\x18\x06 \x01(\x0b\x32!.cohesity.magneto.agents.RpcStats\"\xdd\x01\n\x15ReadVirtualDiskResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\"\n\x13is_data_zero_filled\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06length\x18\x05 \x01(\x04\x12\x18\n\x10io_latency_usecs\x18\x03 \x01(\x03\x12\x34\n\trpc_stats\x18\x06 \x01(\x0b\x32!.cohesity.magneto.agents.RpcStats\"q\n\x14\x44\x65tachVirtualDiskArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x1d\n\x15virtual_disk_path_vec\x18\x02 \x03(\t\"M\n\x17\x44\x65tachVirtualDiskResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xd3\x02\n\x1a\x43onvertToReferencePointArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x14\n\x0chyperv_vm_id\x18\x03 \x01(\t\x12\x1e\n\x16\x63heckpoint_instance_id\x18\x04 \x01(\x0c\x12#\n\x1bprevious_reference_point_id\x18\x05 \x01(\x0c\x12M\n\x10virtual_disk_vec\x18\x06 \x03(\x0b\x32\x33.cohesity.magneto.agents.windows.hyperv.VirtualDisk\"\xa9\x01\n\x1d\x43onvertToReferencePointResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12T\n\x12vm_reference_point\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.hyperv.VMReferencePoint\"\xd9\x01\n\x15GetHostClusterInfoArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x33\n\nentity_vec\x18\x03 \x03(\x0b\x32\x1f.cohesity.magneto.hyperv.Entity\"\xa4\x01\n\x18GetHostClusterInfoResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12T\n\x14hyperv_host_info_vec\x18\x02 \x03(\x0b\x32\x36.cohesity.magneto.agents.windows.hyperv.HyperVHostInfo\"\x9d\x01\n\x0bImportVMArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12R\n\x11restore_vm_params\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMParams\"\x98\x01\n\x0eImportVMResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12R\n\x11restore_vm_handle\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\"\xa5\x01\n\x13MigrateVMStorageArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12R\n\x11restore_vm_handle\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\"\xa0\x01\n\x16MigrateVMStorageResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12R\n\x11restore_vm_handle\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\"\x9e\x01\n\x0cRealizeVMArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12R\n\x11restore_vm_handle\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\"\x9d\x02\n\x0fRealizeVMResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12R\n\x11restore_vm_handle\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\x12:\n\rpoweron_error\x18\x03 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x46\n\x19makehighlyavailable_error\x18\x04 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xca\x01\n\x12GetClonedVMInfoArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x11\n\thost_uuid\x18\x03 \x01(\t\x12\x14\n\x0chyperv_vm_id\x18\x04 \x01(\t\"\x92\x01\n\x15GetClonedVMInfoResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x45\n\x07vm_info\x18\x02 \x01(\x0b\x32\x34.cohesity.magneto.agents.windows.hyperv.HyperVVMInfo\"\xde\x01\n GetVMStorageMigrationProgressArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12R\n\x11restore_vm_handle\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\x12*\n\x1b\x63\x61ncel_vm_storage_migration\x18\x03 \x01(\x08:\x05\x66\x61lse\"\xad\x01\n#GetVMStorageMigrationProgressResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12R\n\x11restore_vm_handle\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\"\xbc\x01\n\rFinalizeVMArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12R\n\x11restore_vm_handle\x18\x02 \x01(\x0b\x32\x37.cohesity.magneto.agents.windows.hyperv.RestoreVMHandle\x12\x1b\n\rshould_commit\x18\x03 \x01(\x08:\x04true\"\x9a\x02\n\x13GetVMVSSSnapshotArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x17\n\x0fsnapshot_set_id\x18\x02 \x01(\x0c\x12\x14\n\x0chyperv_vm_id\x18\x03 \x01(\t\x12K\n\x1ahyperv_disk_exclusion_info\x18\x04 \x03(\x0b\x32\'.cohesity.magneto.HyperVDiskFilterProto\x12K\n\x1ahyperv_disk_inclusion_info\x18\x05 \x03(\x0b\x32\'.cohesity.magneto.HyperVDiskFilterProto\"\x97\x01\n\x16GetVMVSSSnapshotResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12I\n\x14server_snapshot_info\x18\x02 \x01(\x0b\x32+.cohesity.magneto.agents.ServerSnapshotInfo\"\x80\x02\n\x18\x43reateTempFileInGuestArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x14\n\x0cis_directory\x18\x03 \x01(\x08\x12\x16\n\x0e\x64irectory_path\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x05 \x01(\t\x12\x0e\n\x06suffix\x18\x06 \x01(\t\x12Z\n\x13guest_access_params\x18\x07 \x01(\x0b\x32=.cohesity.magneto.agents.windows.stub.HyperVGuestAccessParams\"h\n\x1b\x43reateTempFileInGuestResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x15\n\rtemp_fullpath\x18\x02 \x01(\t\"\xc6\x03\n\x12PushFileToGuestArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x14\n\x0chyperv_vm_id\x18\x02 \x01(\t\x12X\n\rfile_info_vec\x18\x03 \x03(\x0b\x32\x41.cohesity.magneto.agents.windows.stub.PushFileToGuestArg.FileInfo\x1a\xcc\x01\n\x08\x46ileInfo\x12\x17\n\x0flocal_file_path\x18\x01 \x01(\t\x12\x18\n\x10remote_file_path\x18\x02 \x01(\t\x12\x16\n\x0eoverwrite_file\x18\x03 \x01(\x08\x12\x1f\n\x17\x63reate_remote_file_path\x18\x04 \x01(\x08\x12T\n\tfile_type\x18\x05 \x01(\x0e\x32\x41.cohesity.magneto.agents.windows.stub.PushFileToGuestArg.FileType\"5\n\x08\x46ileType\x12\x18\n\x14kWindowsAgentService\x10\x01\x12\x0f\n\x0bkParamsFile\x10\x02\"\x88\x02\n\x15PushFileToGuestResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12_\n\x0f\x66ile_result_vec\x18\x02 \x03(\x0b\x32\x46.cohesity.magneto.agents.windows.stub.PushFileToGuestResult.FileResult\x1aZ\n\nFileResult\x12\x18\n\x10remote_file_path\x18\x02 \x01(\t\x12\x32\n\x05\x65rror\x18\x03 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"V\n\x18\x46\x65tchVMDiskDeviceInfoArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\"Q\n\x1b\x46\x65tchVMDiskDeviceInfoResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xdd\x02\n\x16\x46\x65tchFilesFromGuestArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12X\n\tfile_type\x18\x02 \x01(\x0e\x32\x45.cohesity.magneto.agents.windows.stub.FetchFilesFromGuestArg.FileType\x12\x1b\n\x13host_file_directory\x18\x03 \x01(\t\x12Z\n\x13guest_access_params\x18\x04 \x01(\x0b\x32=.cohesity.magneto.agents.windows.stub.HyperVGuestAccessParams\"4\n\x08\x46ileType\x12\x1b\n\x17kWindowsAgentServiceLog\x10\x01\x12\x0b\n\x07kScript\x10\x02\"\xb4\x02\n\x19\x46\x65tchFilesFromGuestResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12#\n\x1b\x63ohesity_agent_log_file_dir\x18\x03 \x01(\t\x12\x63\n\x0f\x66ile_result_vec\x18\x02 \x03(\x0b\x32J.cohesity.magneto.agents.windows.stub.FetchFilesFromGuestResult.FileResult\x1aY\n\nFileResult\x12\x17\n\x0fguest_file_path\x18\x01 \x01(\t\x12\x32\n\x05\x65rror\x18\x02 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xeb\x01\n\x16StartProgramInGuestArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x14\n\x0chyperv_vm_id\x18\x02 \x01(\t\x12\x32\n\x0b\x63redentials\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.Credentials\x12\x18\n\x10program_fullpath\x18\x04 \x01(\t\x12\x11\n\targuments\x18\x05 \x01(\t\x12\x1e\n\x16working_directory_path\x18\x06 \x01(\t\"c\n\x19StartProgramInGuestResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x12\n\nprocess_id\x18\x02 \x01(\x03\"\xe6\x01\n\x17ListProcessesInGuestArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x16\n\nprocess_id\x18\x03 \x01(\x03:\x02-1\x12\x1b\n\x13process_name_prefix\x18\x04 \x01(\t\x12Z\n\x13guest_access_params\x18\x05 \x01(\x0b\x32=.cohesity.magneto.agents.windows.stub.HyperVGuestAccessParams\"\x9c\x02\n\x1aListProcessesInGuestResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x66\n\x10process_info_vec\x18\x02 \x03(\x0b\x32L.cohesity.magneto.agents.windows.stub.ListProcessesInGuestResult.ProcessInfo\x1a\x62\n\x0bProcessInfo\x12\x12\n\nprocess_id\x18\x01 \x01(\x03\x12\x14\n\x0cprocess_name\x18\x02 \x01(\t\x12\x16\n\x0eprocess_exited\x18\x03 \x01(\x08\x12\x11\n\texit_code\x18\x04 \x01(\x03\"\xd8\x02\n\x15\x44\x65leteFilesInGuestArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12[\n\rfile_info_vec\x18\x03 \x03(\x0b\x32\x44.cohesity.magneto.agents.windows.stub.DeleteFilesInGuestArg.FileInfo\x12Z\n\x13guest_access_params\x18\x04 \x01(\x0b\x32=.cohesity.magneto.agents.windows.stub.HyperVGuestAccessParams\x1aJ\n\x08\x46ileInfo\x12\x15\n\rfile_fullpath\x18\x01 \x01(\t\x12\x14\n\x0cis_directory\x18\x02 \x01(\x08\x12\x11\n\trecursive\x18\x03 \x01(\x08\"\x8b\x02\n\x18\x44\x65leteFilesInGuestResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x62\n\x0f\x66ile_result_vec\x18\x02 \x03(\x0b\x32I.cohesity.magneto.agents.windows.stub.DeleteFilesInGuestResult.FileResult\x1aW\n\nFileResult\x12\x15\n\rfile_fullpath\x18\x01 \x01(\t\x12\x32\n\x05\x65rror\x18\x02 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xc8\x01\n\x1aTerminateProcessInGuestArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x12\n\nprocess_id\x18\x03 \x01(\x03\x12Z\n\x13guest_access_params\x18\x04 \x01(\x0b\x32=.cohesity.magneto.agents.windows.stub.HyperVGuestAccessParams\"S\n\x1dTerminateProcessInGuestResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\x92\x03\n\x0e\x41ttachDisksArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x14\n\x0chyperv_vm_id\x18\x02 \x01(\x0c\x12_\n\x13\x64isk_chain_info_vec\x18\x03 \x03(\x0b\x32\x42.cohesity.magneto.agents.windows.stub.AttachDisksArg.DiskChainInfo\x12 \n\x11\x63ontinue_on_error\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0fupdate_disk_uid\x18\x05 \x01(\x08:\x04true\x1a\x8b\x01\n\rDiskChainInfo\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\x0c\x12\x11\n\tdisk_path\x18\x02 \x01(\t\x12V\n\x0e\x64isk_chain_vec\x18\x03 \x03(\x0b\x32>.cohesity.magneto.agents.windows.hyperv.RestoreVirtualDiskInfo\"\xe1\x02\n\x11\x41ttachDisksResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12h\n\x16\x61ttach_disk_result_vec\x18\x02 \x03(\x0b\x32H.cohesity.magneto.agents.windows.stub.AttachDisksResult.AttachDiskResult\x1a\xad\x01\n\x10\x41ttachDiskResult\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\x0c\x12\x11\n\tdisk_path\x18\x02 \x01(\t\x12\x32\n\x05\x65rror\x18\x03 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x41\n\x04\x64isk\x18\x04 \x01(\x0b\x32\x33.cohesity.magneto.agents.windows.hyperv.VirtualDisk\"\x9a\x01\n\x0e\x44\x65tachDisksArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12\x14\n\x0chyperv_vm_id\x18\x02 \x01(\x0c\x12\x15\n\rdisk_path_vec\x18\x03 \x03(\t\x12\x1f\n\x11\x63ontinue_on_error\x18\x04 \x01(\x08:\x04true\"\x89\x02\n\x11\x44\x65tachDisksResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x66\n\x15\x64\x65tach_disk_error_vec\x18\x02 \x03(\x0b\x32G.cohesity.magneto.agents.windows.stub.DetachDisksResult.DetachDiskError\x1aX\n\x0f\x44\x65tachDiskError\x12\x11\n\tdisk_path\x18\x01 \x01(\t\x12\x32\n\x05\x65rror\x18\x02 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xb7\x01\n\x1dValidateCredentialsInGuestArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12Z\n\x13guest_access_params\x18\x03 \x01(\x0b\x32=.cohesity.magneto.agents.windows.stub.HyperVGuestAccessParams\"\x84\x02\n\x19RestoreHyperVVmOnScvmmArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x32\n\tsource_vm\x18\x03 \x01(\x0b\x32\x1f.cohesity.magneto.hyperv.Entity\x12\x13\n\x0bhyperv_uuid\x18\x04 \x01(\t\x12\x11\n\thost_uuid\x18\x05 \x01(\t\"R\n\x1cRestoreHyperVVmOnScvmmResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xad\x01\n\rPowerOffVMArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x0f\n\x07vm_uuid\x18\x03 \x01(\t\"F\n\x10PowerOffVMResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"\xab\x01\n\x0bRemoveVMArg\x12:\n\x06header\x18\x01 \x01(\x0b\x32*.cohesity.magneto.agents.stub.AgentBaseArg\x12O\n\raccess_params\x18\x02 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.stub.HyperVAccessParams\x12\x0f\n\x07vm_uuid\x18\x03 \x01(\t\"D\n\x0eRemoveVMResult\x12\x32\n\x05\x65rror\x18\x01 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.agents.windows.stub.hyperv_param_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HYPERVACCESSPARAMS']._serialized_start=352
  _globals['_HYPERVACCESSPARAMS']._serialized_end=478
  _globals['_HYPERVGUESTACCESSPARAMS']._serialized_start=481
  _globals['_HYPERVGUESTACCESSPARAMS']._serialized_end=910
  _globals['_HYPERVGUESTACCESSPARAMS_GUESTOSTYPE']._serialized_start=857
  _globals['_HYPERVGUESTACCESSPARAMS_GUESTOSTYPE']._serialized_end=910
  _globals['_HYPERVACCESSSTATE']._serialized_start=912
  _globals['_HYPERVACCESSSTATE']._serialized_end=974
  _globals['_GETHYPERVHIERARCHYARG']._serialized_start=977
  _globals['_GETHYPERVHIERARCHYARG']._serialized_end=1204
  _globals['_GETHYPERVHIERARCHYRESULT']._serialized_start=1207
  _globals['_GETHYPERVHIERARCHYRESULT']._serialized_end=1351
  _globals['_CREATEVMCHECKPOINTARG']._serialized_start=1354
  _globals['_CREATEVMCHECKPOINTARG']._serialized_end=1656
  _globals['_CREATEVMCHECKPOINTRESULT']._serialized_start=1659
  _globals['_CREATEVMCHECKPOINTRESULT']._serialized_end=1796
  _globals['_DELETEVMCHECKPOINTARG']._serialized_start=1799
  _globals['_DELETEVMCHECKPOINTARG']._serialized_end=2017
  _globals['_DELETEVMCHECKPOINTRESULT']._serialized_start=2019
  _globals['_DELETEVMCHECKPOINTRESULT']._serialized_end=2097
  _globals['_GETCHECKPOINTINFOARG']._serialized_start=2100
  _globals['_GETCHECKPOINTINFOARG']._serialized_end=2471
  _globals['_GETCHECKPOINTINFORESULT']._serialized_start=2474
  _globals['_GETCHECKPOINTINFORESULT']._serialized_end=2703
  _globals['_GETCHECKPOINTVMCONFIGARG']._serialized_start=2706
  _globals['_GETCHECKPOINTVMCONFIGARG']._serialized_end=2915
  _globals['_GETCHECKPOINTVMCONFIGRESULT']._serialized_start=2918
  _globals['_GETCHECKPOINTVMCONFIGRESULT']._serialized_end=3096
  _globals['_LOCATEVMARG']._serialized_start=3099
  _globals['_LOCATEVMARG']._serialized_end=3270
  _globals['_LOCATEVMRESULT']._serialized_start=3273
  _globals['_LOCATEVMRESULT']._serialized_end=3412
  _globals['_GETVIRTUALDISKCHANGESARG']._serialized_start=3415
  _globals['_GETVIRTUALDISKCHANGESARG']._serialized_end=3582
  _globals['_GETVIRTUALDISKCHANGESRESULT']._serialized_start=3585
  _globals['_GETVIRTUALDISKCHANGESRESULT']._serialized_end=3769
  _globals['_READVIRTUALDISKARG']._serialized_start=3772
  _globals['_READVIRTUALDISKARG']._serialized_end=4005
  _globals['_READVIRTUALDISKRESULT']._serialized_start=4008
  _globals['_READVIRTUALDISKRESULT']._serialized_end=4229
  _globals['_DETACHVIRTUALDISKARG']._serialized_start=4231
  _globals['_DETACHVIRTUALDISKARG']._serialized_end=4344
  _globals['_DETACHVIRTUALDISKRESULT']._serialized_start=4346
  _globals['_DETACHVIRTUALDISKRESULT']._serialized_end=4423
  _globals['_CONVERTTOREFERENCEPOINTARG']._serialized_start=4426
  _globals['_CONVERTTOREFERENCEPOINTARG']._serialized_end=4765
  _globals['_CONVERTTOREFERENCEPOINTRESULT']._serialized_start=4768
  _globals['_CONVERTTOREFERENCEPOINTRESULT']._serialized_end=4937
  _globals['_GETHOSTCLUSTERINFOARG']._serialized_start=4940
  _globals['_GETHOSTCLUSTERINFOARG']._serialized_end=5157
  _globals['_GETHOSTCLUSTERINFORESULT']._serialized_start=5160
  _globals['_GETHOSTCLUSTERINFORESULT']._serialized_end=5324
  _globals['_IMPORTVMARG']._serialized_start=5327
  _globals['_IMPORTVMARG']._serialized_end=5484
  _globals['_IMPORTVMRESULT']._serialized_start=5487
  _globals['_IMPORTVMRESULT']._serialized_end=5639
  _globals['_MIGRATEVMSTORAGEARG']._serialized_start=5642
  _globals['_MIGRATEVMSTORAGEARG']._serialized_end=5807
  _globals['_MIGRATEVMSTORAGERESULT']._serialized_start=5810
  _globals['_MIGRATEVMSTORAGERESULT']._serialized_end=5970
  _globals['_REALIZEVMARG']._serialized_start=5973
  _globals['_REALIZEVMARG']._serialized_end=6131
  _globals['_REALIZEVMRESULT']._serialized_start=6134
  _globals['_REALIZEVMRESULT']._serialized_end=6419
  _globals['_GETCLONEDVMINFOARG']._serialized_start=6422
  _globals['_GETCLONEDVMINFOARG']._serialized_end=6624
  _globals['_GETCLONEDVMINFORESULT']._serialized_start=6627
  _globals['_GETCLONEDVMINFORESULT']._serialized_end=6773
  _globals['_GETVMSTORAGEMIGRATIONPROGRESSARG']._serialized_start=6776
  _globals['_GETVMSTORAGEMIGRATIONPROGRESSARG']._serialized_end=6998
  _globals['_GETVMSTORAGEMIGRATIONPROGRESSRESULT']._serialized_start=7001
  _globals['_GETVMSTORAGEMIGRATIONPROGRESSRESULT']._serialized_end=7174
  _globals['_FINALIZEVMARG']._serialized_start=7177
  _globals['_FINALIZEVMARG']._serialized_end=7365
  _globals['_GETVMVSSSNAPSHOTARG']._serialized_start=7368
  _globals['_GETVMVSSSNAPSHOTARG']._serialized_end=7650
  _globals['_GETVMVSSSNAPSHOTRESULT']._serialized_start=7653
  _globals['_GETVMVSSSNAPSHOTRESULT']._serialized_end=7804
  _globals['_CREATETEMPFILEINGUESTARG']._serialized_start=7807
  _globals['_CREATETEMPFILEINGUESTARG']._serialized_end=8063
  _globals['_CREATETEMPFILEINGUESTRESULT']._serialized_start=8065
  _globals['_CREATETEMPFILEINGUESTRESULT']._serialized_end=8169
  _globals['_PUSHFILETOGUESTARG']._serialized_start=8172
  _globals['_PUSHFILETOGUESTARG']._serialized_end=8626
  _globals['_PUSHFILETOGUESTARG_FILEINFO']._serialized_start=8367
  _globals['_PUSHFILETOGUESTARG_FILEINFO']._serialized_end=8571
  _globals['_PUSHFILETOGUESTARG_FILETYPE']._serialized_start=8573
  _globals['_PUSHFILETOGUESTARG_FILETYPE']._serialized_end=8626
  _globals['_PUSHFILETOGUESTRESULT']._serialized_start=8629
  _globals['_PUSHFILETOGUESTRESULT']._serialized_end=8893
  _globals['_PUSHFILETOGUESTRESULT_FILERESULT']._serialized_start=8803
  _globals['_PUSHFILETOGUESTRESULT_FILERESULT']._serialized_end=8893
  _globals['_FETCHVMDISKDEVICEINFOARG']._serialized_start=8895
  _globals['_FETCHVMDISKDEVICEINFOARG']._serialized_end=8981
  _globals['_FETCHVMDISKDEVICEINFORESULT']._serialized_start=8983
  _globals['_FETCHVMDISKDEVICEINFORESULT']._serialized_end=9064
  _globals['_FETCHFILESFROMGUESTARG']._serialized_start=9067
  _globals['_FETCHFILESFROMGUESTARG']._serialized_end=9416
  _globals['_FETCHFILESFROMGUESTARG_FILETYPE']._serialized_start=9364
  _globals['_FETCHFILESFROMGUESTARG_FILETYPE']._serialized_end=9416
  _globals['_FETCHFILESFROMGUESTRESULT']._serialized_start=9419
  _globals['_FETCHFILESFROMGUESTRESULT']._serialized_end=9727
  _globals['_FETCHFILESFROMGUESTRESULT_FILERESULT']._serialized_start=9638
  _globals['_FETCHFILESFROMGUESTRESULT_FILERESULT']._serialized_end=9727
  _globals['_STARTPROGRAMINGUESTARG']._serialized_start=9730
  _globals['_STARTPROGRAMINGUESTARG']._serialized_end=9965
  _globals['_STARTPROGRAMINGUESTRESULT']._serialized_start=9967
  _globals['_STARTPROGRAMINGUESTRESULT']._serialized_end=10066
  _globals['_LISTPROCESSESINGUESTARG']._serialized_start=10069
  _globals['_LISTPROCESSESINGUESTARG']._serialized_end=10299
  _globals['_LISTPROCESSESINGUESTRESULT']._serialized_start=10302
  _globals['_LISTPROCESSESINGUESTRESULT']._serialized_end=10586
  _globals['_LISTPROCESSESINGUESTRESULT_PROCESSINFO']._serialized_start=10488
  _globals['_LISTPROCESSESINGUESTRESULT_PROCESSINFO']._serialized_end=10586
  _globals['_DELETEFILESINGUESTARG']._serialized_start=10589
  _globals['_DELETEFILESINGUESTARG']._serialized_end=10933
  _globals['_DELETEFILESINGUESTARG_FILEINFO']._serialized_start=10859
  _globals['_DELETEFILESINGUESTARG_FILEINFO']._serialized_end=10933
  _globals['_DELETEFILESINGUESTRESULT']._serialized_start=10936
  _globals['_DELETEFILESINGUESTRESULT']._serialized_end=11203
  _globals['_DELETEFILESINGUESTRESULT_FILERESULT']._serialized_start=11116
  _globals['_DELETEFILESINGUESTRESULT_FILERESULT']._serialized_end=11203
  _globals['_TERMINATEPROCESSINGUESTARG']._serialized_start=11206
  _globals['_TERMINATEPROCESSINGUESTARG']._serialized_end=11406
  _globals['_TERMINATEPROCESSINGUESTRESULT']._serialized_start=11408
  _globals['_TERMINATEPROCESSINGUESTRESULT']._serialized_end=11491
  _globals['_ATTACHDISKSARG']._serialized_start=11494
  _globals['_ATTACHDISKSARG']._serialized_end=11896
  _globals['_ATTACHDISKSARG_DISKCHAININFO']._serialized_start=11757
  _globals['_ATTACHDISKSARG_DISKCHAININFO']._serialized_end=11896
  _globals['_ATTACHDISKSRESULT']._serialized_start=11899
  _globals['_ATTACHDISKSRESULT']._serialized_end=12252
  _globals['_ATTACHDISKSRESULT_ATTACHDISKRESULT']._serialized_start=12079
  _globals['_ATTACHDISKSRESULT_ATTACHDISKRESULT']._serialized_end=12252
  _globals['_DETACHDISKSARG']._serialized_start=12255
  _globals['_DETACHDISKSARG']._serialized_end=12409
  _globals['_DETACHDISKSRESULT']._serialized_start=12412
  _globals['_DETACHDISKSRESULT']._serialized_end=12677
  _globals['_DETACHDISKSRESULT_DETACHDISKERROR']._serialized_start=12589
  _globals['_DETACHDISKSRESULT_DETACHDISKERROR']._serialized_end=12677
  _globals['_VALIDATECREDENTIALSINGUESTARG']._serialized_start=12680
  _globals['_VALIDATECREDENTIALSINGUESTARG']._serialized_end=12863
  _globals['_RESTOREHYPERVVMONSCVMMARG']._serialized_start=12866
  _globals['_RESTOREHYPERVVMONSCVMMARG']._serialized_end=13126
  _globals['_RESTOREHYPERVVMONSCVMMRESULT']._serialized_start=13128
  _globals['_RESTOREHYPERVVMONSCVMMRESULT']._serialized_end=13210
  _globals['_POWEROFFVMARG']._serialized_start=13213
  _globals['_POWEROFFVMARG']._serialized_end=13386
  _globals['_POWEROFFVMRESULT']._serialized_start=13388
  _globals['_POWEROFFVMRESULT']._serialized_end=13458
  _globals['_REMOVEVMARG']._serialized_start=13461
  _globals['_REMOVEVMARG']._serialized_end=13632
  _globals['_REMOVEVMRESULT']._serialized_start=13634
  _globals['_REMOVEVMRESULT']._serialized_end=13702
# @@protoc_insertion_point(module_scope)
