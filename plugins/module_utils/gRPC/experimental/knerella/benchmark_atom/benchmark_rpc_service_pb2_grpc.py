# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from atom.stub import rpc_service_args_pb2 as atom_dot_stub_dot_rpc__service__args__pb2

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
        + f' but the generated code in experimental/knerella/benchmark_atom/benchmark_rpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AllocateNode = channel.unary_unary(
                '/cohesity.experimental.knerella.benchmark_atom.RpcService/AllocateNode',
                request_serializer=atom_dot_stub_dot_rpc__service__args__pb2.AllocateNodeArg.SerializeToString,
                response_deserializer=atom_dot_stub_dot_rpc__service__args__pb2.AllocateNodeResult.FromString,
                _registered_method=True)
        self.WriteData = channel.unary_unary(
                '/cohesity.experimental.knerella.benchmark_atom.RpcService/WriteData',
                request_serializer=atom_dot_stub_dot_rpc__service__args__pb2.WriteDataArg.SerializeToString,
                response_deserializer=atom_dot_stub_dot_rpc__service__args__pb2.WriteDataResult.FromString,
                _registered_method=True)
        self.WriteDataStream = channel.stream_unary(
                '/cohesity.experimental.knerella.benchmark_atom.RpcService/WriteDataStream',
                request_serializer=atom_dot_stub_dot_rpc__service__args__pb2.WriteDataArg.SerializeToString,
                response_deserializer=atom_dot_stub_dot_rpc__service__args__pb2.WriteDataResult.FromString,
                _registered_method=True)
        self.GetLatestDataEvent = channel.unary_unary(
                '/cohesity.experimental.knerella.benchmark_atom.RpcService/GetLatestDataEvent',
                request_serializer=atom_dot_stub_dot_rpc__service__args__pb2.GetLatestDataEventArg.SerializeToString,
                response_deserializer=atom_dot_stub_dot_rpc__service__args__pb2.GetLatestDataEventResult.FromString,
                _registered_method=True)


class RpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AllocateNode(self, request, context):
        """Call to allocate a node for data transfer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteData(self, request, context):
        """Call to write data to a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteDataStream(self, request_iterator, context):
        """Call to write data to a file using streaming RPCs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLatestDataEvent(self, request, context):
        """Call to get latest data event for an entity.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AllocateNode': grpc.unary_unary_rpc_method_handler(
                    servicer.AllocateNode,
                    request_deserializer=atom_dot_stub_dot_rpc__service__args__pb2.AllocateNodeArg.FromString,
                    response_serializer=atom_dot_stub_dot_rpc__service__args__pb2.AllocateNodeResult.SerializeToString,
            ),
            'WriteData': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteData,
                    request_deserializer=atom_dot_stub_dot_rpc__service__args__pb2.WriteDataArg.FromString,
                    response_serializer=atom_dot_stub_dot_rpc__service__args__pb2.WriteDataResult.SerializeToString,
            ),
            'WriteDataStream': grpc.stream_unary_rpc_method_handler(
                    servicer.WriteDataStream,
                    request_deserializer=atom_dot_stub_dot_rpc__service__args__pb2.WriteDataArg.FromString,
                    response_serializer=atom_dot_stub_dot_rpc__service__args__pb2.WriteDataResult.SerializeToString,
            ),
            'GetLatestDataEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLatestDataEvent,
                    request_deserializer=atom_dot_stub_dot_rpc__service__args__pb2.GetLatestDataEventArg.FromString,
                    response_serializer=atom_dot_stub_dot_rpc__service__args__pb2.GetLatestDataEventResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.experimental.knerella.benchmark_atom.RpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.experimental.knerella.benchmark_atom.RpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AllocateNode(request,
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
            '/cohesity.experimental.knerella.benchmark_atom.RpcService/AllocateNode',
            atom_dot_stub_dot_rpc__service__args__pb2.AllocateNodeArg.SerializeToString,
            atom_dot_stub_dot_rpc__service__args__pb2.AllocateNodeResult.FromString,
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
    def WriteData(request,
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
            '/cohesity.experimental.knerella.benchmark_atom.RpcService/WriteData',
            atom_dot_stub_dot_rpc__service__args__pb2.WriteDataArg.SerializeToString,
            atom_dot_stub_dot_rpc__service__args__pb2.WriteDataResult.FromString,
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
    def WriteDataStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/cohesity.experimental.knerella.benchmark_atom.RpcService/WriteDataStream',
            atom_dot_stub_dot_rpc__service__args__pb2.WriteDataArg.SerializeToString,
            atom_dot_stub_dot_rpc__service__args__pb2.WriteDataResult.FromString,
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
    def GetLatestDataEvent(request,
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
            '/cohesity.experimental.knerella.benchmark_atom.RpcService/GetLatestDataEvent',
            atom_dot_stub_dot_rpc__service__args__pb2.GetLatestDataEventArg.SerializeToString,
            atom_dot_stub_dot_rpc__service__args__pb2.GetLatestDataEventResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
