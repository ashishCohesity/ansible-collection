# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from cohesion.master.stub import grpc_service_pb2 as cohesion_dot_master_dot_stub_dot_grpc__service__pb2

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
        + f' but the generated code in cohesion/master/stub/grpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class GRpcServiceStub(object):
    """-----------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ActivateAppliance = channel.unary_unary(
                '/cohesity.cohesion.master.stub.GRpcService/ActivateAppliance',
                request_serializer=cohesion_dot_master_dot_stub_dot_grpc__service__pb2.ActivateApplianceArg.SerializeToString,
                response_deserializer=cohesion_dot_master_dot_stub_dot_grpc__service__pb2.ActivateApplianceResult.FromString,
                _registered_method=True)
        self.CheckActivation = channel.unary_unary(
                '/cohesity.cohesion.master.stub.GRpcService/CheckActivation',
                request_serializer=cohesion_dot_master_dot_stub_dot_grpc__service__pb2.CheckActivationArg.SerializeToString,
                response_deserializer=cohesion_dot_master_dot_stub_dot_grpc__service__pb2.CheckActivationResult.FromString,
                _registered_method=True)


class GRpcServiceServicer(object):
    """-----------------------------------------------------------------------------

    """

    def ActivateAppliance(self, request, context):
        """Activate the appliance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckActivation(self, request, context):
        """Check appliacnce activation status.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ActivateAppliance': grpc.unary_unary_rpc_method_handler(
                    servicer.ActivateAppliance,
                    request_deserializer=cohesion_dot_master_dot_stub_dot_grpc__service__pb2.ActivateApplianceArg.FromString,
                    response_serializer=cohesion_dot_master_dot_stub_dot_grpc__service__pb2.ActivateApplianceResult.SerializeToString,
            ),
            'CheckActivation': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckActivation,
                    request_deserializer=cohesion_dot_master_dot_stub_dot_grpc__service__pb2.CheckActivationArg.FromString,
                    response_serializer=cohesion_dot_master_dot_stub_dot_grpc__service__pb2.CheckActivationResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.cohesion.master.stub.GRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.cohesion.master.stub.GRpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GRpcService(object):
    """-----------------------------------------------------------------------------

    """

    @staticmethod
    def ActivateAppliance(request,
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
            '/cohesity.cohesion.master.stub.GRpcService/ActivateAppliance',
            cohesion_dot_master_dot_stub_dot_grpc__service__pb2.ActivateApplianceArg.SerializeToString,
            cohesion_dot_master_dot_stub_dot_grpc__service__pb2.ActivateApplianceResult.FromString,
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
    def CheckActivation(request,
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
            '/cohesity.cohesion.master.stub.GRpcService/CheckActivation',
            cohesion_dot_master_dot_stub_dot_grpc__service__pb2.CheckActivationArg.SerializeToString,
            cohesion_dot_master_dot_stub_dot_grpc__service__pb2.CheckActivationResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
