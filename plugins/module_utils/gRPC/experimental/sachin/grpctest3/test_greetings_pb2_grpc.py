# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.sachin.grpctest3 import test_greetings_pb2 as experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2

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
        + f' but the generated code in experimental/sachin/grpctest3/test_greetings_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GreetingsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/howdy.Greetings/SayHello',
                request_serializer=experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.HelloArg.SerializeToString,
                response_deserializer=experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.HelloResult.FromString,
                _registered_method=True)
        self.SayGoodMorning = channel.unary_unary(
                '/howdy.Greetings/SayGoodMorning',
                request_serializer=experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.GoodMorningArg.SerializeToString,
                response_deserializer=experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.GoodMorningResult.FromString,
                _registered_method=True)


class GreetingsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Sends a Hello greeting back.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayGoodMorning(self, request, context):
        """Sends a Good Morning greeting back.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetingsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.HelloArg.FromString,
                    response_serializer=experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.HelloResult.SerializeToString,
            ),
            'SayGoodMorning': grpc.unary_unary_rpc_method_handler(
                    servicer.SayGoodMorning,
                    request_deserializer=experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.GoodMorningArg.FromString,
                    response_serializer=experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.GoodMorningResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'howdy.Greetings', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('howdy.Greetings', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Greetings(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
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
            '/howdy.Greetings/SayHello',
            experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.HelloArg.SerializeToString,
            experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.HelloResult.FromString,
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
    def SayGoodMorning(request,
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
            '/howdy.Greetings/SayGoodMorning',
            experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.GoodMorningArg.SerializeToString,
            experimental_dot_sachin_dot_grpctest3_dot_test__greetings__pb2.GoodMorningResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)