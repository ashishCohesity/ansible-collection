# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from magneto.failover.stub import rpc_service_pb2 as magneto_dot_failover_dot_stub_dot_rpc__service__pb2

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
        + f' but the generated code in magneto/failover/stub/rpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RpcServiceStub(object):
    """-----------------------------------------------------------------------------

    Rpc service used by Magneto Failover Service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FetchFailoverCommand = channel.unary_unary(
                '/cohesity.magneto.failover.stub.RpcService/FetchFailoverCommand',
                request_serializer=magneto_dot_failover_dot_stub_dot_rpc__service__pb2.FetchFailoverCommandArg.SerializeToString,
                response_deserializer=magneto_dot_failover_dot_stub_dot_rpc__service__pb2.FetchFailoverCommandResult.FromString,
                _registered_method=True)
        self.DeliverFailoverCommandResponse = channel.unary_unary(
                '/cohesity.magneto.failover.stub.RpcService/DeliverFailoverCommandResponse',
                request_serializer=magneto_dot_failover_dot_stub_dot_rpc__service__pb2.DeliverFailoverCommandResponseArg.SerializeToString,
                response_deserializer=magneto_dot_failover_dot_stub_dot_rpc__service__pb2.DeliverFailoverCommandResponseResult.FromString,
                _registered_method=True)


class RpcServiceServicer(object):
    """-----------------------------------------------------------------------------

    Rpc service used by Magneto Failover Service.
    """

    def FetchFailoverCommand(self, request, context):
        """RPC to get the FailoverCommand arguments from the Rx cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeliverFailoverCommandResponse(self, request, context):
        """RPC to deliver the FailoverCommand results to the Rx cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FetchFailoverCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchFailoverCommand,
                    request_deserializer=magneto_dot_failover_dot_stub_dot_rpc__service__pb2.FetchFailoverCommandArg.FromString,
                    response_serializer=magneto_dot_failover_dot_stub_dot_rpc__service__pb2.FetchFailoverCommandResult.SerializeToString,
            ),
            'DeliverFailoverCommandResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.DeliverFailoverCommandResponse,
                    request_deserializer=magneto_dot_failover_dot_stub_dot_rpc__service__pb2.DeliverFailoverCommandResponseArg.FromString,
                    response_serializer=magneto_dot_failover_dot_stub_dot_rpc__service__pb2.DeliverFailoverCommandResponseResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.magneto.failover.stub.RpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.magneto.failover.stub.RpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RpcService(object):
    """-----------------------------------------------------------------------------

    Rpc service used by Magneto Failover Service.
    """

    @staticmethod
    def FetchFailoverCommand(request,
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
            '/cohesity.magneto.failover.stub.RpcService/FetchFailoverCommand',
            magneto_dot_failover_dot_stub_dot_rpc__service__pb2.FetchFailoverCommandArg.SerializeToString,
            magneto_dot_failover_dot_stub_dot_rpc__service__pb2.FetchFailoverCommandResult.FromString,
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
    def DeliverFailoverCommandResponse(request,
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
            '/cohesity.magneto.failover.stub.RpcService/DeliverFailoverCommandResponse',
            magneto_dot_failover_dot_stub_dot_rpc__service__pb2.DeliverFailoverCommandResponseArg.SerializeToString,
            magneto_dot_failover_dot_stub_dot_rpc__service__pb2.DeliverFailoverCommandResponseResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
