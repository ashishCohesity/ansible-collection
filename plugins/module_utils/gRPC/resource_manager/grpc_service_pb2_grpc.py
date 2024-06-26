# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from resource_manager import api_pb2 as resource__manager_dot_api__pb2

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
        + f' but the generated code in resource_manager/grpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GRpcServiceStub(object):
    """Resource Manager gRPC service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Acquire = channel.unary_unary(
                '/cohesity.resource_manager.api.GRpcService/Acquire',
                request_serializer=resource__manager_dot_api__pb2.AcquireArg.SerializeToString,
                response_deserializer=resource__manager_dot_api__pb2.AcquireResult.FromString,
                _registered_method=True)
        self.Release = channel.unary_unary(
                '/cohesity.resource_manager.api.GRpcService/Release',
                request_serializer=resource__manager_dot_api__pb2.ReleaseArg.SerializeToString,
                response_deserializer=resource__manager_dot_api__pb2.ReleaseResult.FromString,
                _registered_method=True)
        self.AddOrUpdateProviders = channel.unary_unary(
                '/cohesity.resource_manager.api.GRpcService/AddOrUpdateProviders',
                request_serializer=resource__manager_dot_api__pb2.AddOrUpdateProvidersArg.SerializeToString,
                response_deserializer=resource__manager_dot_api__pb2.AddOrUpdateProvidersResult.FromString,
                _registered_method=True)
        self.LookupProviders = channel.unary_unary(
                '/cohesity.resource_manager.api.GRpcService/LookupProviders',
                request_serializer=resource__manager_dot_api__pb2.LookupProvidersArg.SerializeToString,
                response_deserializer=resource__manager_dot_api__pb2.LookupProvidersResult.FromString,
                _registered_method=True)
        self.ForceGc = channel.unary_unary(
                '/cohesity.resource_manager.api.GRpcService/ForceGc',
                request_serializer=resource__manager_dot_api__pb2.ForceGcArg.SerializeToString,
                response_deserializer=resource__manager_dot_api__pb2.ForceGcResult.FromString,
                _registered_method=True)
        self.LookupRequestors = channel.unary_unary(
                '/cohesity.resource_manager.api.GRpcService/LookupRequestors',
                request_serializer=resource__manager_dot_api__pb2.LookupRequestorsArg.SerializeToString,
                response_deserializer=resource__manager_dot_api__pb2.LookupRequestorsResult.FromString,
                _registered_method=True)
        self.SendHeartbeat = channel.unary_unary(
                '/cohesity.resource_manager.api.GRpcService/SendHeartbeat',
                request_serializer=resource__manager_dot_api__pb2.SendHeartbeatArg.SerializeToString,
                response_deserializer=resource__manager_dot_api__pb2.SendHeartbeatResult.FromString,
                _registered_method=True)


class GRpcServiceServicer(object):
    """Resource Manager gRPC service definition.
    """

    def Acquire(self, request, context):
        """Acquire resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Release(self, request, context):
        """Release resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddOrUpdateProviders(self, request, context):
        """Add new providers, update existing one, and delete them.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupProviders(self, request, context):
        """Look up providers known to the resource manager.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ForceGc(self, request, context):
        """Trigger a force gc of resource manager state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupRequestors(self, request, context):
        """Look up Requestors and their state known to resource manager.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendHeartbeat(self, request, context):
        """Send heartbeats periodically to indicate liveness of resource requestors.
        Refer to api.proto for detailed comments on the semantics of this API.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Acquire': grpc.unary_unary_rpc_method_handler(
                    servicer.Acquire,
                    request_deserializer=resource__manager_dot_api__pb2.AcquireArg.FromString,
                    response_serializer=resource__manager_dot_api__pb2.AcquireResult.SerializeToString,
            ),
            'Release': grpc.unary_unary_rpc_method_handler(
                    servicer.Release,
                    request_deserializer=resource__manager_dot_api__pb2.ReleaseArg.FromString,
                    response_serializer=resource__manager_dot_api__pb2.ReleaseResult.SerializeToString,
            ),
            'AddOrUpdateProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.AddOrUpdateProviders,
                    request_deserializer=resource__manager_dot_api__pb2.AddOrUpdateProvidersArg.FromString,
                    response_serializer=resource__manager_dot_api__pb2.AddOrUpdateProvidersResult.SerializeToString,
            ),
            'LookupProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupProviders,
                    request_deserializer=resource__manager_dot_api__pb2.LookupProvidersArg.FromString,
                    response_serializer=resource__manager_dot_api__pb2.LookupProvidersResult.SerializeToString,
            ),
            'ForceGc': grpc.unary_unary_rpc_method_handler(
                    servicer.ForceGc,
                    request_deserializer=resource__manager_dot_api__pb2.ForceGcArg.FromString,
                    response_serializer=resource__manager_dot_api__pb2.ForceGcResult.SerializeToString,
            ),
            'LookupRequestors': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupRequestors,
                    request_deserializer=resource__manager_dot_api__pb2.LookupRequestorsArg.FromString,
                    response_serializer=resource__manager_dot_api__pb2.LookupRequestorsResult.SerializeToString,
            ),
            'SendHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.SendHeartbeat,
                    request_deserializer=resource__manager_dot_api__pb2.SendHeartbeatArg.FromString,
                    response_serializer=resource__manager_dot_api__pb2.SendHeartbeatResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.resource_manager.api.GRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.resource_manager.api.GRpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GRpcService(object):
    """Resource Manager gRPC service definition.
    """

    @staticmethod
    def Acquire(request,
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
            '/cohesity.resource_manager.api.GRpcService/Acquire',
            resource__manager_dot_api__pb2.AcquireArg.SerializeToString,
            resource__manager_dot_api__pb2.AcquireResult.FromString,
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
    def Release(request,
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
            '/cohesity.resource_manager.api.GRpcService/Release',
            resource__manager_dot_api__pb2.ReleaseArg.SerializeToString,
            resource__manager_dot_api__pb2.ReleaseResult.FromString,
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
    def AddOrUpdateProviders(request,
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
            '/cohesity.resource_manager.api.GRpcService/AddOrUpdateProviders',
            resource__manager_dot_api__pb2.AddOrUpdateProvidersArg.SerializeToString,
            resource__manager_dot_api__pb2.AddOrUpdateProvidersResult.FromString,
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
    def LookupProviders(request,
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
            '/cohesity.resource_manager.api.GRpcService/LookupProviders',
            resource__manager_dot_api__pb2.LookupProvidersArg.SerializeToString,
            resource__manager_dot_api__pb2.LookupProvidersResult.FromString,
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
    def ForceGc(request,
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
            '/cohesity.resource_manager.api.GRpcService/ForceGc',
            resource__manager_dot_api__pb2.ForceGcArg.SerializeToString,
            resource__manager_dot_api__pb2.ForceGcResult.FromString,
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
    def LookupRequestors(request,
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
            '/cohesity.resource_manager.api.GRpcService/LookupRequestors',
            resource__manager_dot_api__pb2.LookupRequestorsArg.SerializeToString,
            resource__manager_dot_api__pb2.LookupRequestorsResult.FromString,
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
    def SendHeartbeat(request,
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
            '/cohesity.resource_manager.api.GRpcService/SendHeartbeat',
            resource__manager_dot_api__pb2.SendHeartbeatArg.SerializeToString,
            resource__manager_dot_api__pb2.SendHeartbeatResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
