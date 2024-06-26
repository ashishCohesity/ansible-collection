# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: util/cert/ssl_certificate.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1futil/cert/ssl_certificate.proto\x12\rcohesity.cert\"K\n\x10\x43lientServerCert\x12\x37\n\ncert_pairs\x18\x01 \x03(\x0b\x32#.cohesity.cert.ClientServerCertPair\"\x8e\x01\n\x14\x43lientServerCertPair\x12\n\n\x02id\x18\x01 \x02(\t\x12\x34\n\x0bserver_cert\x18\x02 \x01(\x0b\x32\x1f.cohesity.cert.CertificateProto\x12\x34\n\x0b\x63lient_cert\x18\x03 \x01(\x0b\x32\x1f.cohesity.cert.CertificateProto\"\x81\x01\n\x10\x43\x65rtificateProto\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12\x1e\n\x16last_import_time_msecs\x18\x03 \x01(\x03\x12\x1f\n\x03\x63sr\x18\x04 \x02(\x0b\x32\x12.cohesity.cert.Csr\x12\x17\n\x0f\x63\x61_certificates\x18\x05 \x01(\x0c\"\xda\x05\n\x13SslCertificateProto\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x02(\x0c\x12\x13\n\x0bprivate_key\x18\x02 \x02(\x0c\x12\x1e\n\x16last_update_time_msecs\x18\x03 \x01(\x03\x12\"\n\x1aweb_server_ca_certificates\x18\x04 \x03(\t\x12\"\n\x1aweb_client_ca_certificates\x18\x05 \x03(\t\x12\x12\n\x07version\x18\x06 \x01(\x05:\x01\x31\x12[\n\x18helios_certificate_store\x18\x07 \x01(\x0b\x32\x39.cohesity.cert.SslCertificateProto.HeliosCertificateStore\x12\x16\n\x0e\x61pi_public_key\x18\x08 \x01(\x0c\x12\x17\n\x0f\x61pi_private_key\x18\t \x01(\x0c\x12#\n\x07\x63sr_vec\x18\n \x03(\x0b\x32\x12.cohesity.cert.Csr\x1a\xe9\x02\n\x16HeliosCertificateStore\x12P\n\x18\x63luster_certificate_path\x18\x01 \x01(\t:./home/cohesity/data/iris/heliosClient/cert.pem\x12O\n\x18\x63luster_private_key_path\x18\x02 \x01(\t:-/home/cohesity/data/iris/heliosClient/key.pem\x12V\n\x17helios_certificate_path\x18\x03 \x01(\t:5/home/cohesity/data/iris/heliosClient/helios_cert.pem\x12\x1b\n\x13\x63luster_certificate\x18\x04 \x01(\t\x12\x1b\n\x13\x63luster_private_key\x18\x05 \x01(\t\x12\x1a\n\x12helios_certificate\x18\x06 \x01(\t\"\xdb\x03\n\x03\x43sr\x12\n\n\x02id\x18\x01 \x01(\t\x12\x33\n\x08key_type\x18\x02 \x01(\x0e\x32\x1c.cohesity.cert.Csr.Algorithm:\x03rsa\x12\x15\n\rkey_size_bits\x18\x03 \x01(\x03\x12\x13\n\x0b\x63ommon_name\x18\x04 \x01(\t\x12\x14\n\x0corganization\x18\x05 \x01(\t\x12\x19\n\x11organization_unit\x18\x06 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12\x0c\n\x04\x63ity\x18\t \x01(\t\x12\x11\n\tdns_names\x18\n \x03(\t\x12\x10\n\x08host_ips\x18\x0b \x03(\t\x12\x15\n\remail_address\x18\x0c \x01(\t\x12\x36\n\x0cservice_name\x18\r \x01(\x0e\x32\x1a.cohesity.cert.Csr.Service:\x04iris\x12\x1d\n\x15\x65ncrypted_private_key\x18\x0e \x01(\t\x12\x12\n\npublic_key\x18\x0f \x01(\t\x12\x0b\n\x03\x63sr\x18\x10 \x01(\t\x12\x19\n\x11\x63reationTimeUsecs\x18\x11 \x01(\x03\"\x1f\n\tAlgorithm\x12\x07\n\x03rsa\x10\x01\x12\t\n\x05\x65\x63\x64sa\x10\x02\"\x13\n\x07Service\x12\x08\n\x04iris\x10\x01\"r\n\x10\x41gentCertificate\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x02(\x0c\x12\x1d\n\x15\x65ncrypted_private_key\x18\x02 \x02(\x0c\x12\n\n\x02id\x18\x04 \x01(\t\x12\x1e\n\x16\x61\x64\x64itional_ca_to_trust\x18\x05 \x01(\x0c\x42\x18\n\x16\x63om.cohesity.util.cert')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'util.cert.ssl_certificate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.cohesity.util.cert'
  _globals['_CLIENTSERVERCERT']._serialized_start=50
  _globals['_CLIENTSERVERCERT']._serialized_end=125
  _globals['_CLIENTSERVERCERTPAIR']._serialized_start=128
  _globals['_CLIENTSERVERCERTPAIR']._serialized_end=270
  _globals['_CERTIFICATEPROTO']._serialized_start=273
  _globals['_CERTIFICATEPROTO']._serialized_end=402
  _globals['_SSLCERTIFICATEPROTO']._serialized_start=405
  _globals['_SSLCERTIFICATEPROTO']._serialized_end=1135
  _globals['_SSLCERTIFICATEPROTO_HELIOSCERTIFICATESTORE']._serialized_start=774
  _globals['_SSLCERTIFICATEPROTO_HELIOSCERTIFICATESTORE']._serialized_end=1135
  _globals['_CSR']._serialized_start=1138
  _globals['_CSR']._serialized_end=1613
  _globals['_CSR_ALGORITHM']._serialized_start=1561
  _globals['_CSR_ALGORITHM']._serialized_end=1592
  _globals['_CSR_SERVICE']._serialized_start=1594
  _globals['_CSR_SERVICE']._serialized_end=1613
  _globals['_AGENTCERTIFICATE']._serialized_start=1615
  _globals['_AGENTCERTIFICATE']._serialized_end=1729
# @@protoc_insertion_point(module_scope)
