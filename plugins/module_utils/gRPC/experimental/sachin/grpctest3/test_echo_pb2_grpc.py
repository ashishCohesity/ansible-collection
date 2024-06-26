# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.sachin.grpctest3 import test_echo_pb2 as experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2

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
        + f' but the generated code in experimental/sachin/grpctest3/test_echo_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class EchoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EchoMessage = channel.unary_unary(
                '/echoservice.Echo/EchoMessage',
                request_serializer=experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoMessageArg.SerializeToString,
                response_deserializer=experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoMessageResult.FromString,
                _registered_method=True)
        self.EchoWithName = channel.unary_unary(
                '/echoservice.Echo/EchoWithName',
                request_serializer=experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoWithNameArg.SerializeToString,
                response_deserializer=experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoWithNameResult.FromString,
                _registered_method=True)


class EchoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EchoMessage(self, request, context):
        """Sends a message to server and gets it back.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EchoWithName(self, request, context):
        """Sends a message to server and name. Server sends back concatenated form of
        message and name: separated by a space.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EchoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EchoMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.EchoMessage,
                    request_deserializer=experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoMessageArg.FromString,
                    response_serializer=experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoMessageResult.SerializeToString,
            ),
            'EchoWithName': grpc.unary_unary_rpc_method_handler(
                    servicer.EchoWithName,
                    request_deserializer=experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoWithNameArg.FromString,
                    response_serializer=experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoWithNameResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'echoservice.Echo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('echoservice.Echo', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Echo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EchoMessage(request,
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
            '/echoservice.Echo/EchoMessage',
            experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoMessageArg.SerializeToString,
            experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoMessageResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EchoWithName(request,
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
            '/echoservice.Echo/EchoWithName',
            experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoWithNameArg.SerializeToString,
            experimental_dot_sachin_dot_grpctest3_dot_test__echo__pb2.EchoWithNameResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
