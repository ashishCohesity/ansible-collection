# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from magneto.v2.scheduler.api import api_pb2 as magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2

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
        + f' but the generated code in magneto/v2/scheduler/api/grpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GRpcServiceStub(object):
    """Magneto Scheduler gRPC service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddOrUpdateJob = channel.unary_unary(
                '/cohesity.magneto.sched.api.GRpcService/AddOrUpdateJob',
                request_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateJobArg.SerializeToString,
                response_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateJobResult.FromString,
                _registered_method=True)
        self.RemoveJob = channel.unary_unary(
                '/cohesity.magneto.sched.api.GRpcService/RemoveJob',
                request_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveJobArg.SerializeToString,
                response_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveJobResult.FromString,
                _registered_method=True)
        self.AddOrUpdateProtectionSpec = channel.unary_unary(
                '/cohesity.magneto.sched.api.GRpcService/AddOrUpdateProtectionSpec',
                request_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateProtectionSpecArg.SerializeToString,
                response_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateProtectionSpecResult.FromString,
                _registered_method=True)
        self.RemoveProtectionSpec = channel.unary_unary(
                '/cohesity.magneto.sched.api.GRpcService/RemoveProtectionSpec',
                request_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveProtectionSpecArg.SerializeToString,
                response_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveProtectionSpecResult.FromString,
                _registered_method=True)
        self.AddOrUpdatePolicy = channel.unary_unary(
                '/cohesity.magneto.sched.api.GRpcService/AddOrUpdatePolicy',
                request_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdatePolicyArg.SerializeToString,
                response_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdatePolicyResult.FromString,
                _registered_method=True)
        self.RemovePolicy = channel.unary_unary(
                '/cohesity.magneto.sched.api.GRpcService/RemovePolicy',
                request_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemovePolicyArg.SerializeToString,
                response_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemovePolicyResult.FromString,
                _registered_method=True)


class GRpcServiceServicer(object):
    """Magneto Scheduler gRPC service definition.
    """

    def AddOrUpdateJob(self, request, context):
        """AddOrUpdate the job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveJob(self, request, context):
        """Remove the job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddOrUpdateProtectionSpec(self, request, context):
        """AddOrUpdate the protection spec.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveProtectionSpec(self, request, context):
        """Remove the protection spec.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddOrUpdatePolicy(self, request, context):
        """AddOrUpdate the policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemovePolicy(self, request, context):
        """Remove the policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddOrUpdateJob': grpc.unary_unary_rpc_method_handler(
                    servicer.AddOrUpdateJob,
                    request_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateJobArg.FromString,
                    response_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateJobResult.SerializeToString,
            ),
            'RemoveJob': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveJob,
                    request_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveJobArg.FromString,
                    response_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveJobResult.SerializeToString,
            ),
            'AddOrUpdateProtectionSpec': grpc.unary_unary_rpc_method_handler(
                    servicer.AddOrUpdateProtectionSpec,
                    request_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateProtectionSpecArg.FromString,
                    response_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateProtectionSpecResult.SerializeToString,
            ),
            'RemoveProtectionSpec': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveProtectionSpec,
                    request_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveProtectionSpecArg.FromString,
                    response_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveProtectionSpecResult.SerializeToString,
            ),
            'AddOrUpdatePolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.AddOrUpdatePolicy,
                    request_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdatePolicyArg.FromString,
                    response_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdatePolicyResult.SerializeToString,
            ),
            'RemovePolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.RemovePolicy,
                    request_deserializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemovePolicyArg.FromString,
                    response_serializer=magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemovePolicyResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.magneto.sched.api.GRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.magneto.sched.api.GRpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GRpcService(object):
    """Magneto Scheduler gRPC service definition.
    """

    @staticmethod
    def AddOrUpdateJob(request,
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
            '/cohesity.magneto.sched.api.GRpcService/AddOrUpdateJob',
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateJobArg.SerializeToString,
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateJobResult.FromString,
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
    def RemoveJob(request,
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
            '/cohesity.magneto.sched.api.GRpcService/RemoveJob',
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveJobArg.SerializeToString,
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveJobResult.FromString,
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
    def AddOrUpdateProtectionSpec(request,
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
            '/cohesity.magneto.sched.api.GRpcService/AddOrUpdateProtectionSpec',
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateProtectionSpecArg.SerializeToString,
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdateProtectionSpecResult.FromString,
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
    def RemoveProtectionSpec(request,
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
            '/cohesity.magneto.sched.api.GRpcService/RemoveProtectionSpec',
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveProtectionSpecArg.SerializeToString,
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemoveProtectionSpecResult.FromString,
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
    def AddOrUpdatePolicy(request,
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
            '/cohesity.magneto.sched.api.GRpcService/AddOrUpdatePolicy',
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdatePolicyArg.SerializeToString,
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.AddOrUpdatePolicyResult.FromString,
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
    def RemovePolicy(request,
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
            '/cohesity.magneto.sched.api.GRpcService/RemovePolicy',
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemovePolicyArg.SerializeToString,
            magneto_dot_v2_dot_scheduler_dot_api_dot_api__pb2.RemovePolicyResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
