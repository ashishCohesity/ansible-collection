# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gaia/dataplane/api/api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gaia.dataplane.base import error_pb2 as gaia_dot_dataplane_dot_base_dot_error__pb2
from gaia.dataplane.api import base_pb2 as gaia_dot_dataplane_dot_api_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgaia/dataplane/api/api.proto\x12\x1b\x63ohesity.gaia.dataplane.api\x1a\x1fgaia/dataplane/base/error.proto\x1a\x1dgaia/dataplane/api/base.proto\"\xc2\x11\n\x06\x46ilter\x12P\n\x15mailbox_accept_filter\x18\x01 \x01(\x0b\x32\x31.cohesity.gaia.dataplane.api.Filter.MailboxFilter\x12P\n\x15mailbox_reject_filter\x18\x02 \x01(\x0b\x32\x31.cohesity.gaia.dataplane.api.Filter.MailboxFilter\x12N\n\x16onedrive_accept_filter\x18\x03 \x01(\x0b\x32..cohesity.gaia.dataplane.api.Filter.FileFilter\x12N\n\x16onedrive_reject_filter\x18\x04 \x01(\x0b\x32..cohesity.gaia.dataplane.api.Filter.FileFilter\x12H\n\x10vm_accept_filter\x18\x05 \x01(\x0b\x32..cohesity.gaia.dataplane.api.Filter.FileFilter\x12H\n\x10vm_reject_filter\x18\x06 \x01(\x0b\x32..cohesity.gaia.dataplane.api.Filter.FileFilter\x12S\n\x1b\x63ohesity_view_accept_filter\x18\x07 \x01(\x0b\x32..cohesity.gaia.dataplane.api.Filter.FileFilter\x12S\n\x1b\x63ohesity_view_reject_filter\x18\x08 \x01(\x0b\x32..cohesity.gaia.dataplane.api.Filter.FileFilter\x1a\xad\x05\n\rMailboxFilter\x12M\n\x10\x64\x61ta_sensitivity\x18\x01 \x03(\x0e\x32\x33.cohesity.gaia.dataplane.api.Filter.DataSensitivity\x12P\n\nexpression\x18\x02 \x01(\x0b\x32<.cohesity.gaia.dataplane.api.Filter.MailboxFilter.Expression\x1a\xfa\x03\n\nExpression\x12\x0f\n\x05owner\x18\x01 \x01(\tH\x00\x12\x14\n\nfrom_regex\x18\x02 \x01(\tH\x00\x12\x12\n\x08to_regex\x18\x03 \x01(\tH\x00\x12\x19\n\x0f\x64\x61te_secs_floor\x18\x04 \x01(\x03H\x00\x12\x1b\n\x11\x64\x61te_secs_ceiling\x18\x05 \x01(\x03H\x00\x12q\n\x16repeated_expression_or\x18\x06 \x01(\x0b\x32O.cohesity.gaia.dataplane.api.Filter.MailboxFilter.Expression.RepeatedExpressionH\x00\x12r\n\x17repeated_expression_and\x18\x07 \x01(\x0b\x32O.cohesity.gaia.dataplane.api.Filter.MailboxFilter.Expression.RepeatedExpressionH\x00\x12\x18\n\x10\x63\x61se_insensitive\x18\x08 \x01(\x08\x1aj\n\x12RepeatedExpression\x12T\n\x0e\x65xpression_vec\x18\x01 \x03(\x0b\x32<.cohesity.gaia.dataplane.api.Filter.MailboxFilter.ExpressionB\x0c\n\noneof_type\x1a\xd0\x06\n\nFileFilter\x12M\n\x10\x64\x61ta_sensitivity\x18\x01 \x03(\x0e\x32\x33.cohesity.gaia.dataplane.api.Filter.DataSensitivity\x12M\n\nexpression\x18\x02 \x01(\x0b\x32\x39.cohesity.gaia.dataplane.api.Filter.FileFilter.Expression\x1a\xa3\x05\n\nExpression\x12\x0f\n\x05owner\x18\x01 \x01(\tH\x00\x12\x1c\n\x12modtime_secs_floor\x18\x02 \x01(\x03H\x00\x12\x1e\n\x14modtime_secs_ceiling\x18\x03 \x01(\x03H\x00\x12\x18\n\x0e\x66ilename_regex\x18\x04 \x01(\tH\x00\x12\x1b\n\x11path_prefix_regex\x18\x05 \x01(\tH\x00\x12G\n\rdocument_type\x18\x06 \x01(\x0e\x32..cohesity.gaia.dataplane.api.DocumentType.TypeH\x00\x12T\n\x15\x66ile_data_sensitivity\x18\x07 \x01(\x0e\x32\x33.cohesity.gaia.dataplane.api.Filter.DataSensitivityH\x00\x12n\n\x16repeated_expression_or\x18\x08 \x01(\x0b\x32L.cohesity.gaia.dataplane.api.Filter.FileFilter.Expression.RepeatedExpressionH\x00\x12o\n\x17repeated_expression_and\x18\t \x01(\x0b\x32L.cohesity.gaia.dataplane.api.Filter.FileFilter.Expression.RepeatedExpressionH\x00\x12\x18\n\x10\x63\x61se_insensitive\x18\n \x01(\x08\x1ag\n\x12RepeatedExpression\x12Q\n\x0e\x65xpression_vec\x18\x01 \x03(\x0b\x32\x39.cohesity.gaia.dataplane.api.Filter.FileFilter.ExpressionB\x0c\n\noneof_type\"3\n\x0f\x44\x61taSensitivity\x12\x08\n\x04kLow\x10\x00\x12\x0b\n\x07kMedium\x10\x01\x12\t\n\x05kHigh\x10\x02\"\x81\x02\n\rGetObjectsArg\x12\x44\n\x0cobject_types\x18\x01 \x03(\x0e\x32..cohesity.gaia.dataplane.api.Object.ObjectType\x12\x33\n\x06\x66ilter\x18\x02 \x01(\x0b\x32#.cohesity.gaia.dataplane.api.Filter\x12\x1f\n\x17need_all_snapshots_info\x18\x03 \x01(\x08\x12\x0e\n\x06\x63ookie\x18\x04 \x01(\x0c\x12\x1d\n\x15\x66orwarding_disallowed\x18\x05 \x01(\x08\x12\x12\n\naccount_id\x18\x06 \x01(\x0c\x12\x11\n\ttenant_id\x18\x07 \x01(\x0c\"]\n\x10GetObjectsResult\x12\x13\n\x0bnext_cookie\x18\x01 \x01(\x0c\x12\x34\n\x07objects\x18\x02 \x03(\x0b\x32#.cohesity.gaia.dataplane.api.Object\"\xa4\x02\n\x10GetSubObjectsArg\x12\x12\n\naccount_id\x18\x01 \x01(\x0c\x12\x11\n\ttenant_id\x18\x02 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\x0c\x12<\n\x04type\x18\x04 \x01(\x0e\x32..cohesity.gaia.dataplane.api.Object.ObjectType\x12\x44\n\x0fsnapshot_handle\x18\x05 \x01(\x0b\x32+.cohesity.gaia.dataplane.api.SnapshotHandle\x12\x33\n\x06\x66ilter\x18\x06 \x01(\x0b\x32#.cohesity.gaia.dataplane.api.Filter\x12\x1d\n\x15\x66orwarding_disallowed\x18\x07 \x01(\x08\"X\n\x13GetSubObjectsResult\x12\x41\n\x0bsub_objects\x18\x01 \x03(\x0b\x32,.cohesity.gaia.dataplane.api.SubObjectHandle\"\xff\x03\n\x10ListDocumentsArg\x12\x12\n\naccount_id\x18\x01 \x01(\x0c\x12\x11\n\ttenant_id\x18\x02 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\x0c\x12<\n\x04type\x18\x04 \x01(\x0e\x32..cohesity.gaia.dataplane.api.Object.ObjectType\x12\x44\n\x0fsnapshot_handle\x18\x05 \x01(\x0b\x32+.cohesity.gaia.dataplane.api.SnapshotHandle\x12I\n\x14\x62\x61se_snapshot_handle\x18\x06 \x01(\x0b\x32+.cohesity.gaia.dataplane.api.SnapshotHandle\x12G\n\x11sub_object_handle\x18\x07 \x01(\x0b\x32,.cohesity.gaia.dataplane.api.SubObjectHandle\x12\x33\n\x06\x66ilter\x18\x08 \x01(\x0b\x32#.cohesity.gaia.dataplane.api.Filter\x12\x0e\n\x06\x63ookie\x18\t \x01(\x0c\x12\x1d\n\x15\x66orwarding_disallowed\x18\n \x01(\x08\x12\x19\n\x11max_document_size\x18\x0b \x01(\x03\x12\x1a\n\x12\x63ontent_disallowed\x18\x0c \x01(\x08\"^\n\x11\x44ocumentDataRange\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\x12\n\x08\x63ontents\x18\x02 \x01(\x0cH\x00\x12\x17\n\rcontents_size\x18\x03 \x01(\x05H\x00\x42\x0c\n\noneof_type\"\xba\x01\n\x08\x44ocument\x12\n\n\x02id\x18\x01 \x01(\x0c\x12@\n\rdocument_type\x18\x02 \x01(\x0b\x32).cohesity.gaia.dataplane.api.DocumentType\x12\x41\n\trange_vec\x18\x03 \x03(\x0b\x32..cohesity.gaia.dataplane.api.DocumentDataRange\x12\x1d\n\x15total_original_length\x18\x04 \x01(\x03\"d\n\x13ListDocumentsResult\x12\x13\n\x0bnext_cookie\x18\x01 \x01(\x0c\x12\x38\n\tdocuments\x18\x02 \x03(\x0b\x32%.cohesity.gaia.dataplane.api.Document\"\xae\x04\n\x0fGetDocumentsArg\x12\x12\n\naccount_id\x18\x01 \x01(\x0c\x12\x11\n\ttenant_id\x18\x02 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\x0c\x12<\n\x04type\x18\x04 \x01(\x0e\x32..cohesity.gaia.dataplane.api.Object.ObjectType\x12\x44\n\x0fsnapshot_handle\x18\x05 \x01(\x0b\x32+.cohesity.gaia.dataplane.api.SnapshotHandle\x12G\n\x11sub_object_handle\x18\x06 \x01(\x0b\x32,.cohesity.gaia.dataplane.api.SubObjectHandle\x12T\n\x11\x64ocument_spec_vec\x18\x07 \x03(\x0b\x32\x39.cohesity.gaia.dataplane.api.GetDocumentsArg.DocumentSpec\x12\x1d\n\x15\x66orwarding_disallowed\x18\x08 \x01(\x08\x12\x33\n\x06\x66ilter\x18\t \x01(\x0b\x32#.cohesity.gaia.dataplane.api.Filter\x12\"\n\x1a\x64ocument_metadata_required\x18\n \x01(\x08\x1a\x46\n\x0c\x44ocumentSpec\x12\x0e\n\x06\x64oc_id\x18\x01 \x01(\x0c\x12\x12\n\noffset_vec\x18\x02 \x03(\x03\x12\x12\n\nlength_vec\x18\x03 \x03(\x05\"\xf7\x01\n\x12GetDocumentsResult\x12[\n\x13\x64ocument_result_vec\x18\x01 \x03(\x0b\x32>.cohesity.gaia.dataplane.api.GetDocumentsResult.DocumentResult\x1a\x83\x01\n\x0e\x44ocumentResult\x12\x37\n\x08\x64ocument\x18\x01 \x01(\x0b\x32%.cohesity.gaia.dataplane.api.Document\x12\x38\n\x0b\x65rror_proto\x18\x02 \x01(\x0b\x32#.cohesity.gaia.dataplane.ErrorProto\"\xb6\x02\n\x18GetConvertedDocumentsArg\x12\x12\n\naccount_id\x18\x01 \x01(\x0c\x12\x11\n\ttenant_id\x18\x02 \x01(\x0c\x12\x1b\n\x13\x65mblem_service_info\x18\x03 \x01(\x0c\x12]\n\x11\x64ocument_spec_vec\x18\x04 \x03(\x0b\x32\x42.cohesity.gaia.dataplane.api.GetConvertedDocumentsArg.DocumentSpec\x12%\n\x1dmax_unconverted_document_size\x18\x05 \x01(\x03\x1aP\n\x0c\x44ocumentSpec\x12\x18\n\x10\x64ocument_locator\x18\x01 \x01(\x0c\x12\x12\n\noffset_vec\x18\x02 \x03(\x03\x12\x12\n\nlength_vec\x18\x03 \x03(\x05\"\x93\x02\n\x1bGetConvertedDocumentsResult\x12\x64\n\x13\x64ocument_result_vec\x18\x01 \x03(\x0b\x32G.cohesity.gaia.dataplane.api.GetConvertedDocumentsResult.DocumentResult\x1a\x8d\x01\n\x0e\x44ocumentResult\x12\x41\n\trange_vec\x18\x01 \x03(\x0b\x32..cohesity.gaia.dataplane.api.DocumentDataRange\x12\x38\n\x0b\x65rror_proto\x18\x02 \x01(\x0b\x32#.cohesity.gaia.dataplane.ErrorProto\"\xc7\x01\n\x15UpdateCleanupStateArg\x12\x12\n\nsession_id\x18\x01 \x01(\x03\x12\x19\n\x11logical_timestamp\x18\x02 \x01(\x03\x12V\n\rcleanup_state\x18\x03 \x01(\x0b\x32?.cohesity.gaia.dataplane.api.UpdateCleanupStateArg.CleanupState\x1a\'\n\x0c\x43leanupState\x12\x17\n\x0f\x63loned_view_vec\x18\x01 \x03(\t\"\x1a\n\x18UpdateCleanupStateResult\"\x8e\x03\n\rIndexingStats\x12\x13\n\x0bnum_objects\x18\x01 \x01(\x03\x12\x15\n\rnum_snapshots\x18\x02 \x01(\x03\x12\x1c\n\x14num_finished_objects\x18\x03 \x01(\x03\x12\x1e\n\x16num_finished_snapshots\x18\x04 \x01(\x03\x12 \n\x18num_finished_sub_objects\x18\x05 \x01(\x03\x12\x19\n\x11num_finished_docs\x18\x06 \x01(\x03\x12\x1a\n\x12num_converted_docs\x18\x07 \x01(\x03\x12\x17\n\x0fnum_errors_seen\x18\x08 \x01(\x03\x12\x18\n\x10num_indexed_docs\x18\t \x01(\x03\x12\x1a\n\x12num_indexed_chunks\x18\n \x01(\x03\x12\x18\n\x10num_total_chunks\x18\r \x01(\x03\x12\x19\n\x11num_indexed_bytes\x18\x0b \x01(\x03\x12\x1c\n\x14num_vectorized_bytes\x18\x0e \x01(\x03\x12\x18\n\x10outofspace_error\x18\x0c \x01(\x08\"\x91\x04\n\x11IndexDocumentsArg\x12\x12\n\naccount_id\x18\x01 \x01(\x0c\x12\x11\n\ttenant_id\x18\x02 \x01(\x0c\x12\x34\n\x07objects\x18\x03 \x03(\x0b\x32#.cohesity.gaia.dataplane.api.Object\x12\x33\n\x06\x66ilter\x18\x04 \x01(\x0b\x32#.cohesity.gaia.dataplane.api.Filter\x12\x1b\n\x13\x65mblem_service_info\x18\x05 \x01(\x0c\x12\x15\n\rcollection_id\x18\x06 \x01(\x0c\x12\x1d\n\x15\x66orwarding_disallowed\x18\x07 \x01(\x08\x12\x12\n\njob_handle\x18\x08 \x01(\x0c\x12L\n\nslave_data\x18\t \x01(\x0b\x32\x38.cohesity.gaia.dataplane.api.IndexDocumentsArg.SlaveData\x12!\n\x19max_indexed_document_size\x18\n \x01(\x03\x1a\x91\x01\n\tSlaveData\x12\x13\n\x0btask_handle\x18\x01 \x01(\x03\x12\x1b\n\x13\x65xpected_session_id\x18\x02 \x01(\x03\x12\x17\n\x0findexing_cookie\x18\x03 \x01(\x0c\x12\x39\n\x05stats\x18\x04 \x01(\x0b\x32*.cohesity.gaia.dataplane.api.IndexingStats\"\x16\n\x14IndexDocumentsResult\"I\n\x14GetIndexingStatusArg\x12\x12\n\njob_handle\x18\x01 \x01(\x0c\x12\x1d\n\x15\x66orwarding_disallowed\x18\x02 \x01(\x08\"\xbb\x01\n\x17GetIndexingStatusResult\x12\x10\n\x08\x66inished\x18\x01 \x01(\x08\x12\x1e\n\x16\x63\x61ncellation_scheduled\x18\x02 \x01(\x08\x12\x39\n\x05stats\x18\x03 \x01(\x0b\x32*.cohesity.gaia.dataplane.api.IndexingStats\x12\x18\n\x10start_time_usecs\x18\x04 \x01(\x03\x12\x19\n\x11\x66inish_time_usecs\x18\x05 \x01(\x03\"\xf7\x02\n\x17ReportIndexingStatusArg\x12\x18\n\x10slave_session_id\x18\x01 \x01(\x03\x12\x19\n\x11logical_timestamp\x18\x02 \x01(\x03\x12\x1d\n\x15\x66orwarding_disallowed\x18\x03 \x01(\x08\x12X\n\x0ftask_status_vec\x18\x04 \x03(\x0b\x32?.cohesity.gaia.dataplane.api.ReportIndexingStatusArg.TaskStatus\x1a\xad\x01\n\nTaskStatus\x12\x12\n\njob_handle\x18\x01 \x01(\x0c\x12\x13\n\x0btask_handle\x18\x02 \x01(\x03\x12\x10\n\x08\x66inished\x18\x03 \x01(\x08\x12\x10\n\x08\x63\x61nceled\x18\x04 \x01(\x08\x12\x17\n\x0findexing_cookie\x18\x05 \x01(\x0c\x12\x39\n\x05stats\x18\x06 \x01(\x0b\x32*.cohesity.gaia.dataplane.api.IndexingStats\"Z\n\x1aReportIndexingStatusResult\x12<\n\x0f\x65rror_proto_vec\x18\x01 \x03(\x0b\x32#.cohesity.gaia.dataplane.ErrorProto\"[\n\x11\x43\x61ncelIndexingArg\x12\x12\n\njob_handle\x18\x01 \x01(\x0c\x12\x13\n\x0btask_handle\x18\x02 \x01(\x03\x12\x1d\n\x15\x66orwarding_disallowed\x18\x03 \x01(\x08\"(\n\x14\x43\x61ncelIndexingResult\x12\x10\n\x08\x63\x61nceled\x18\x01 \x01(\x08\x42\x1dZ\x1b\x63ohesity/gaia/dataplane/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gaia.dataplane.api.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\033cohesity/gaia/dataplane/api'
  _globals['_FILTER']._serialized_start=126
  _globals['_FILTER']._serialized_end=2368
  _globals['_FILTER_MAILBOXFILTER']._serialized_start=779
  _globals['_FILTER_MAILBOXFILTER']._serialized_end=1464
  _globals['_FILTER_MAILBOXFILTER_EXPRESSION']._serialized_start=958
  _globals['_FILTER_MAILBOXFILTER_EXPRESSION']._serialized_end=1464
  _globals['_FILTER_MAILBOXFILTER_EXPRESSION_REPEATEDEXPRESSION']._serialized_start=1344
  _globals['_FILTER_MAILBOXFILTER_EXPRESSION_REPEATEDEXPRESSION']._serialized_end=1450
  _globals['_FILTER_FILEFILTER']._serialized_start=1467
  _globals['_FILTER_FILEFILTER']._serialized_end=2315
  _globals['_FILTER_FILEFILTER_EXPRESSION']._serialized_start=1640
  _globals['_FILTER_FILEFILTER_EXPRESSION']._serialized_end=2315
  _globals['_FILTER_FILEFILTER_EXPRESSION_REPEATEDEXPRESSION']._serialized_start=2198
  _globals['_FILTER_FILEFILTER_EXPRESSION_REPEATEDEXPRESSION']._serialized_end=2301
  _globals['_FILTER_DATASENSITIVITY']._serialized_start=2317
  _globals['_FILTER_DATASENSITIVITY']._serialized_end=2368
  _globals['_GETOBJECTSARG']._serialized_start=2371
  _globals['_GETOBJECTSARG']._serialized_end=2628
  _globals['_GETOBJECTSRESULT']._serialized_start=2630
  _globals['_GETOBJECTSRESULT']._serialized_end=2723
  _globals['_GETSUBOBJECTSARG']._serialized_start=2726
  _globals['_GETSUBOBJECTSARG']._serialized_end=3018
  _globals['_GETSUBOBJECTSRESULT']._serialized_start=3020
  _globals['_GETSUBOBJECTSRESULT']._serialized_end=3108
  _globals['_LISTDOCUMENTSARG']._serialized_start=3111
  _globals['_LISTDOCUMENTSARG']._serialized_end=3622
  _globals['_DOCUMENTDATARANGE']._serialized_start=3624
  _globals['_DOCUMENTDATARANGE']._serialized_end=3718
  _globals['_DOCUMENT']._serialized_start=3721
  _globals['_DOCUMENT']._serialized_end=3907
  _globals['_LISTDOCUMENTSRESULT']._serialized_start=3909
  _globals['_LISTDOCUMENTSRESULT']._serialized_end=4009
  _globals['_GETDOCUMENTSARG']._serialized_start=4012
  _globals['_GETDOCUMENTSARG']._serialized_end=4570
  _globals['_GETDOCUMENTSARG_DOCUMENTSPEC']._serialized_start=4500
  _globals['_GETDOCUMENTSARG_DOCUMENTSPEC']._serialized_end=4570
  _globals['_GETDOCUMENTSRESULT']._serialized_start=4573
  _globals['_GETDOCUMENTSRESULT']._serialized_end=4820
  _globals['_GETDOCUMENTSRESULT_DOCUMENTRESULT']._serialized_start=4689
  _globals['_GETDOCUMENTSRESULT_DOCUMENTRESULT']._serialized_end=4820
  _globals['_GETCONVERTEDDOCUMENTSARG']._serialized_start=4823
  _globals['_GETCONVERTEDDOCUMENTSARG']._serialized_end=5133
  _globals['_GETCONVERTEDDOCUMENTSARG_DOCUMENTSPEC']._serialized_start=5053
  _globals['_GETCONVERTEDDOCUMENTSARG_DOCUMENTSPEC']._serialized_end=5133
  _globals['_GETCONVERTEDDOCUMENTSRESULT']._serialized_start=5136
  _globals['_GETCONVERTEDDOCUMENTSRESULT']._serialized_end=5411
  _globals['_GETCONVERTEDDOCUMENTSRESULT_DOCUMENTRESULT']._serialized_start=5270
  _globals['_GETCONVERTEDDOCUMENTSRESULT_DOCUMENTRESULT']._serialized_end=5411
  _globals['_UPDATECLEANUPSTATEARG']._serialized_start=5414
  _globals['_UPDATECLEANUPSTATEARG']._serialized_end=5613
  _globals['_UPDATECLEANUPSTATEARG_CLEANUPSTATE']._serialized_start=5574
  _globals['_UPDATECLEANUPSTATEARG_CLEANUPSTATE']._serialized_end=5613
  _globals['_UPDATECLEANUPSTATERESULT']._serialized_start=5615
  _globals['_UPDATECLEANUPSTATERESULT']._serialized_end=5641
  _globals['_INDEXINGSTATS']._serialized_start=5644
  _globals['_INDEXINGSTATS']._serialized_end=6042
  _globals['_INDEXDOCUMENTSARG']._serialized_start=6045
  _globals['_INDEXDOCUMENTSARG']._serialized_end=6574
  _globals['_INDEXDOCUMENTSARG_SLAVEDATA']._serialized_start=6429
  _globals['_INDEXDOCUMENTSARG_SLAVEDATA']._serialized_end=6574
  _globals['_INDEXDOCUMENTSRESULT']._serialized_start=6576
  _globals['_INDEXDOCUMENTSRESULT']._serialized_end=6598
  _globals['_GETINDEXINGSTATUSARG']._serialized_start=6600
  _globals['_GETINDEXINGSTATUSARG']._serialized_end=6673
  _globals['_GETINDEXINGSTATUSRESULT']._serialized_start=6676
  _globals['_GETINDEXINGSTATUSRESULT']._serialized_end=6863
  _globals['_REPORTINDEXINGSTATUSARG']._serialized_start=6866
  _globals['_REPORTINDEXINGSTATUSARG']._serialized_end=7241
  _globals['_REPORTINDEXINGSTATUSARG_TASKSTATUS']._serialized_start=7068
  _globals['_REPORTINDEXINGSTATUSARG_TASKSTATUS']._serialized_end=7241
  _globals['_REPORTINDEXINGSTATUSRESULT']._serialized_start=7243
  _globals['_REPORTINDEXINGSTATUSRESULT']._serialized_end=7333
  _globals['_CANCELINDEXINGARG']._serialized_start=7335
  _globals['_CANCELINDEXINGARG']._serialized_end=7426
  _globals['_CANCELINDEXINGRESULT']._serialized_start=7428
  _globals['_CANCELINDEXINGRESULT']._serialized_end=7468
# @@protoc_insertion_point(module_scope)