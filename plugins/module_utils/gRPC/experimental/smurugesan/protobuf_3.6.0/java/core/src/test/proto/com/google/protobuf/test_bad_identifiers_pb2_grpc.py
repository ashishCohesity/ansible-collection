# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.smurugesan.protobuf_3.6.0.java.core.src.test.proto.com.google.protobuf import test_bad_identifiers_pb2 as experimental_dot_smurugesan_dot_protobuf__3_dot_6_dot_0_dot_java_dot_core_dot_src_dot_test_dot_proto_dot_com_dot_google_dot_protobuf_dot_test__bad__identifiers__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in experimental/smurugesan/protobuf_3.6.0/java/core/src/test/proto/com/google/protobuf/test_bad_identifiers_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TestConflictingMethodNamesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Override = channel.unary_unary(
                '/io_protocol_tests.TestConflictingMethodNames/Override',
                request_serializer=experimental_dot_smurugesan_dot_protobuf__3_dot_6_dot_0_dot_java_dot_core_dot_src_dot_test_dot_proto_dot_com_dot_google_dot_protobuf_dot_test__bad__identifiers__pb2.TestMessage.SerializeToString,
                response_deserializer=experimental_dot_smurugesan_dot_protobuf__3_dot_6_dot_0_dot_java_dot_core_dot_src_dot_test_dot_proto_dot_com_dot_google_dot_protobuf_dot_test__bad__identifiers__pb2.TestMessage.FromString,
                _registered_method=True)


class TestConflictingMethodNamesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Override(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestConflictingMethodNamesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Override': grpc.unary_unary_rpc_method_handler(
                    servicer.Override,
                    request_deserializer=experimental_dot_smurugesan_dot_protobuf__3_dot_6_dot_0_dot_java_dot_core_dot_src_dot_test_dot_proto_dot_com_dot_google_dot_protobuf_dot_test__bad__identifiers__pb2.TestMessage.FromString,
                    response_serializer=experimental_dot_smurugesan_dot_protobuf__3_dot_6_dot_0_dot_java_dot_core_dot_src_dot_test_dot_proto_dot_com_dot_google_dot_protobuf_dot_test__bad__identifiers__pb2.TestMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'io_protocol_tests.TestConflictingMethodNames', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('io_protocol_tests.TestConflictingMethodNames', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TestConflictingMethodNames(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Override(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/io_protocol_tests.TestConflictingMethodNames/Override',
            experimental_dot_smurugesan_dot_protobuf__3_dot_6_dot_0_dot_java_dot_core_dot_src_dot_test_dot_proto_dot_com_dot_google_dot_protobuf_dot_test__bad__identifiers__pb2.TestMessage.SerializeToString,
            experimental_dot_smurugesan_dot_protobuf__3_dot_6_dot_0_dot_java_dot_core_dot_src_dot_test_dot_proto_dot_com_dot_google_dot_protobuf_dot_test__bad__identifiers__pb2.TestMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
