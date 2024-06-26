# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/base/entities/kubernetes.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.base import common_pb2 as magneto_dot_base_dot_common__pb2
from magneto.connectors.kubernetes import kubernetes_api_pb2 as magneto_dot_connectors_dot_kubernetes_dot_kubernetes__api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&magneto/base/entities/kubernetes.proto\x12\x1b\x63ohesity.magneto.kubernetes\x1a\x19magneto/base/common.proto\x1a\x32magneto/connectors/kubernetes/kubernetes_api.proto\"D\n\x13LabelAttributesInfo\x12\x11\n\tentity_id\x18\x01 \x01(\x03\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xa8\x01\n\x06IPMode\x12S\n\x10ip_family_policy\x18\x01 \x01(\x0e\x32+.cohesity.magneto.kubernetes.IPFamilyPolicy:\x0ckSingleStack\x12I\n\x13preferred_ip_family\x18\x02 \x01(\x0e\x32%.cohesity.magneto.kubernetes.IPFamily:\x05kIPV4\"\x95\x0e\n\x06\x45ntity\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.cohesity.magneto.kubernetes.Entity.Type\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0f\n\x07version\x18\x07 \x01(\t\x12N\n\x14label_attributes_vec\x18\t \x03(\x0b\x32\x30.cohesity.magneto.kubernetes.LabelAttributesInfo\x12\x11\n\tnamespace\x18\n \x01(\t\x12i\n\x1dservices_to_connector_ids_map\x18\x0b \x03(\x0b\x32\x42.cohesity.magneto.kubernetes.Entity.ServicesToConnectorIdsMapEntry\x12\x10\n\x08pvc_name\x18\x0c \x01(\t\x12 \n\x18\x64\x61tamover_image_location\x18\r \x01(\t\x12\x1d\n\x15velero_image_location\x18\x0e \x01(\t\x12(\n velero_aws_plugin_image_location\x18\x0f \x01(\t\x12%\n\x1dinit_container_image_location\x18\x10 \x01(\t\x12.\n&velero_openshift_plugin_image_location\x18\x11 \x01(\t\x12Q\n\x0c\x64istribution\x18\x12 \x01(\x0e\x32\x30.cohesity.magneto.kubernetes.Entity.Distribution:\tkMainline\x12\x16\n\x0evelero_version\x18\x13 \x01(\t\x12M\n\x14velero_upgradability\x18\x14 \x01(\x0e\x32%.cohesity.magneto.Upgradability.State:\x08kCurrent\x12\x1f\n\x17\x64\x61tamover_agent_version\x18\x15 \x01(\t\x12P\n\x17\x64\x61tamover_upgradability\x18\x16 \x01(\x0e\x32%.cohesity.magneto.Upgradability.State:\x08kCurrent\x12S\n\x16\x64\x61tamover_service_type\x18\x17 \x01(\x0e\x32(.cohesity.magneto.kubernetes.ServiceType:\tkNodePort\x12\x39\n\x13\x64\x65\x66\x61ult_vlan_params\x18\x19 \x01(\x0b\x32\x1c.cohesity.magneto.VlanParams\x12<\n\rvlan_info_vec\x18\x1a \x03(\x0b\x32%.cohesity.magneto.kubernetes.VlanInfo\x12X\n\x13service_annotations\x18\x1b \x03(\x0b\x32;.cohesity.magneto.kubernetes.Entity.ServiceAnnotationsEntry\x12P\n\x0ftolerations_vec\x18\x1c \x03(\x0b\x32\x37.cohesity.magneto.kubernetes.PodInfo.PodSpec.Toleration\x12\x34\n\x07ip_mode\x18\x1d \x01(\x0b\x32#.cohesity.magneto.kubernetes.IPMode\x12O\n\x11storage_class_vec\x18\x1e \x03(\x0b\x32\x34.cohesity.magneto.kubernetes.Entity.StorageClassInfo\x12\x11\n\tlabel_vec\x18\x1f \x03(\t\x1a@\n\x1eServicesToConnectorIdsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x39\n\x17ServiceAnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x10StorageClassInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bprovisioner\x18\x02 \x01(\t\"{\n\x04Type\x12\x0c\n\x08kCluster\x10\x00\x12\x0e\n\nkNamespace\x10\x01\x12\x0c\n\x08kService\x10\x02\x12\x08\n\x04kPVC\x10\x03\x12\n\n\x06kLabel\x10\x04\x12\x15\n\x11kPersistentVolume\x10\x05\x12\x1a\n\x16kPersistentVolumeClaim\x10\x06\"k\n\x0c\x44istribution\x12\r\n\tkMainline\x10\x00\x12\x0e\n\nkOpenshift\x10\x01\x12\x0c\n\x08kRancher\x10\x02\x12\x08\n\x04kEKS\x10\x03\x12\x08\n\x04kGKE\x10\x04\x12\x08\n\x04kAKS\x10\x05\x12\x10\n\x0ckVMwareTanzu\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x08\x10\tJ\x04\x08\x18\x10\x19\"\x99\x02\n\x0bPodMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x11\n\tnode_name\x18\x03 \x01(\t\x12G\n\nvolume_vec\x18\x04 \x03(\x0b\x32\x33.cohesity.magneto.kubernetes.PodMetadata.VolumeInfo\x1a\x92\x01\n\nVolumeInfo\x12G\n\x06volume\x18\x01 \x01(\x0b\x32\x37.cohesity.magneto.kubernetes.PodInfo.PodSpec.VolumeInfo\x12\x0f\n\x07pv_name\x18\x02 \x01(\t\x12\x13\n\x0bvolume_path\x18\x03 \x01(\t\x12\x15\n\rstorage_class\x18\x04 \x01(\t\"\xd4\x01\n\x08VlanInfo\x12\x31\n\x0bvlan_params\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.VlanParams\x12Z\n\x13service_annotations\x18\x02 \x03(\x0b\x32=.cohesity.magneto.kubernetes.VlanInfo.ServiceAnnotationsEntry\x1a\x39\n\x17ServiceAnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01* \n\x08IPFamily\x12\t\n\x05kIPV4\x10\x00\x12\t\n\x05kIPV6\x10\x01*2\n\x0eIPFamilyPolicy\x12\x10\n\x0ckSingleStack\x10\x00\x12\x0e\n\nkDualStack\x10\x01*?\n\x0bServiceType\x12\x0e\n\nkClusterIp\x10\x00\x12\r\n\tkNodePort\x10\x01\x12\x11\n\rkLoadBalancer\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.base.entities.kubernetes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENTITY_SERVICESTOCONNECTORIDSMAPENTRY']._loaded_options = None
  _globals['_ENTITY_SERVICESTOCONNECTORIDSMAPENTRY']._serialized_options = b'8\001'
  _globals['_ENTITY_SERVICEANNOTATIONSENTRY']._loaded_options = None
  _globals['_ENTITY_SERVICEANNOTATIONSENTRY']._serialized_options = b'8\001'
  _globals['_VLANINFO_SERVICEANNOTATIONSENTRY']._loaded_options = None
  _globals['_VLANINFO_SERVICEANNOTATIONSENTRY']._serialized_options = b'8\001'
  _globals['_IPFAMILY']._serialized_start=2706
  _globals['_IPFAMILY']._serialized_end=2738
  _globals['_IPFAMILYPOLICY']._serialized_start=2740
  _globals['_IPFAMILYPOLICY']._serialized_end=2790
  _globals['_SERVICETYPE']._serialized_start=2792
  _globals['_SERVICETYPE']._serialized_end=2855
  _globals['_LABELATTRIBUTESINFO']._serialized_start=150
  _globals['_LABELATTRIBUTESINFO']._serialized_end=218
  _globals['_IPMODE']._serialized_start=221
  _globals['_IPMODE']._serialized_end=389
  _globals['_ENTITY']._serialized_start=392
  _globals['_ENTITY']._serialized_end=2205
  _globals['_ENTITY_SERVICESTOCONNECTORIDSMAPENTRY']._serialized_start=1775
  _globals['_ENTITY_SERVICESTOCONNECTORIDSMAPENTRY']._serialized_end=1839
  _globals['_ENTITY_SERVICEANNOTATIONSENTRY']._serialized_start=1841
  _globals['_ENTITY_SERVICEANNOTATIONSENTRY']._serialized_end=1898
  _globals['_ENTITY_STORAGECLASSINFO']._serialized_start=1900
  _globals['_ENTITY_STORAGECLASSINFO']._serialized_end=1953
  _globals['_ENTITY_TYPE']._serialized_start=1955
  _globals['_ENTITY_TYPE']._serialized_end=2078
  _globals['_ENTITY_DISTRIBUTION']._serialized_start=2080
  _globals['_ENTITY_DISTRIBUTION']._serialized_end=2187
  _globals['_PODMETADATA']._serialized_start=2208
  _globals['_PODMETADATA']._serialized_end=2489
  _globals['_PODMETADATA_VOLUMEINFO']._serialized_start=2343
  _globals['_PODMETADATA_VOLUMEINFO']._serialized_end=2489
  _globals['_VLANINFO']._serialized_start=2492
  _globals['_VLANINFO']._serialized_end=2704
  _globals['_VLANINFO_SERVICEANNOTATIONSENTRY']._serialized_start=1841
  _globals['_VLANINFO_SERVICEANNOTATIONSENTRY']._serialized_end=1898
# @@protoc_insertion_point(module_scope)
