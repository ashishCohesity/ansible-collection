# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from groot.server.slave.stub import rpc_service_pb2 as groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2

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
        + f' but the generated code in groot/server/slave/stub/rpc_service_pb2_grpc.py depends on'
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
        self.UpdateServiceInfo = channel.unary_unary(
                '/cohesity.groot.server.slave.stub.RpcService/UpdateServiceInfo',
                request_serializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.UpdateServiceInfoArg.SerializeToString,
                response_deserializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.UpdateServiceInfoResult.FromString,
                _registered_method=True)
        self.StartMigration = channel.unary_unary(
                '/cohesity.groot.server.slave.stub.RpcService/StartMigration',
                request_serializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.StartMigrationArg.SerializeToString,
                response_deserializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.StartMigrationResult.FromString,
                _registered_method=True)
        self.CancelMigration = channel.unary_unary(
                '/cohesity.groot.server.slave.stub.RpcService/CancelMigration',
                request_serializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.CancelMigrationArg.SerializeToString,
                response_deserializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.CancelMigrationResult.FromString,
                _registered_method=True)
        self.QueryMigrationTasks = channel.unary_unary(
                '/cohesity.groot.server.slave.stub.RpcService/QueryMigrationTasks',
                request_serializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.QueryMigrationTasksArg.SerializeToString,
                response_deserializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.QueryMigrationTasksResult.FromString,
                _registered_method=True)


class RpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateServiceInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartMigration(self, request, context):
        """RPC to start migration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelMigration(self, request, context):
        """RPC to cancel an ongoing migration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryMigrationTasks(self, request, context):
        """RPC to query running migration tasks on a slave node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateServiceInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateServiceInfo,
                    request_deserializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.UpdateServiceInfoArg.FromString,
                    response_serializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.UpdateServiceInfoResult.SerializeToString,
            ),
            'StartMigration': grpc.unary_unary_rpc_method_handler(
                    servicer.StartMigration,
                    request_deserializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.StartMigrationArg.FromString,
                    response_serializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.StartMigrationResult.SerializeToString,
            ),
            'CancelMigration': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelMigration,
                    request_deserializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.CancelMigrationArg.FromString,
                    response_serializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.CancelMigrationResult.SerializeToString,
            ),
            'QueryMigrationTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryMigrationTasks,
                    request_deserializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.QueryMigrationTasksArg.FromString,
                    response_serializer=groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.QueryMigrationTasksResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.groot.server.slave.stub.RpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.groot.server.slave.stub.RpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateServiceInfo(request,
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
            '/cohesity.groot.server.slave.stub.RpcService/UpdateServiceInfo',
            groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.UpdateServiceInfoArg.SerializeToString,
            groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.UpdateServiceInfoResult.FromString,
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
    def StartMigration(request,
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
            '/cohesity.groot.server.slave.stub.RpcService/StartMigration',
            groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.StartMigrationArg.SerializeToString,
            groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.StartMigrationResult.FromString,
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
    def CancelMigration(request,
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
            '/cohesity.groot.server.slave.stub.RpcService/CancelMigration',
            groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.CancelMigrationArg.SerializeToString,
            groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.CancelMigrationResult.FromString,
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
    def QueryMigrationTasks(request,
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
            '/cohesity.groot.server.slave.stub.RpcService/QueryMigrationTasks',
            groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.QueryMigrationTasksArg.SerializeToString,
            groot_dot_server_dot_slave_dot_stub_dot_rpc__service__pb2.QueryMigrationTasksResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)