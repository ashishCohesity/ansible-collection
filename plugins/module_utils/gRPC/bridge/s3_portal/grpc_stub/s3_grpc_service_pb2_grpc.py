# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from bridge.s3_portal.grpc_stub import s3_grpc_service_pb2 as bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2

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
        + f' but the generated code in bridge/s3_portal/grpc_stub/s3_grpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class S3PrivateRpcServiceStub(object):
    """-----------------------------------------------------------------------------

    Set of APIs exposed by S3 portal for internal consumption
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateObject = channel.unary_unary(
                '/cohesity.bridge.s3_portal.stub.S3PrivateRpcService/CreateObject',
                request_serializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.CreateObjectArg.SerializeToString,
                response_deserializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.CreateObjectResult.FromString,
                _registered_method=True)
        self.FinalizeObject = channel.unary_unary(
                '/cohesity.bridge.s3_portal.stub.S3PrivateRpcService/FinalizeObject',
                request_serializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.FinalizeObjectArg.SerializeToString,
                response_deserializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.FinalizeObjectResult.FromString,
                _registered_method=True)
        self.GetObjectVersions = channel.unary_unary(
                '/cohesity.bridge.s3_portal.stub.S3PrivateRpcService/GetObjectVersions',
                request_serializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.GetObjectVersionsArg.SerializeToString,
                response_deserializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.GetObjectVersionsResult.FromString,
                _registered_method=True)
        self.DeleteObjectVersion = channel.unary_unary(
                '/cohesity.bridge.s3_portal.stub.S3PrivateRpcService/DeleteObjectVersion',
                request_serializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.DeleteObjectVersionArg.SerializeToString,
                response_deserializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.DeleteObjectVersionResult.FromString,
                _registered_method=True)


class S3PrivateRpcServiceServicer(object):
    """-----------------------------------------------------------------------------

    Set of APIs exposed by S3 portal for internal consumption
    """

    def CreateObject(self, request, context):
        """Create a new object in cohesity s3 and return eh for dedup_write.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinalizeObject(self, request, context):
        """Finalize the object in cohesity s3 after dedup write.
        This method will also update etag and other object metadata.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectVersions(self, request, context):
        """Get an object and its versions for the given key.
        This api supports paging using markers.
        This api returns a tuple of [key, version, entity handles].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteObjectVersion(self, request, context):
        """Delete the object version in cohesity s3 bucket.
        This method will also delete object metadata.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_S3PrivateRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateObject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateObject,
                    request_deserializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.CreateObjectArg.FromString,
                    response_serializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.CreateObjectResult.SerializeToString,
            ),
            'FinalizeObject': grpc.unary_unary_rpc_method_handler(
                    servicer.FinalizeObject,
                    request_deserializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.FinalizeObjectArg.FromString,
                    response_serializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.FinalizeObjectResult.SerializeToString,
            ),
            'GetObjectVersions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectVersions,
                    request_deserializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.GetObjectVersionsArg.FromString,
                    response_serializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.GetObjectVersionsResult.SerializeToString,
            ),
            'DeleteObjectVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteObjectVersion,
                    request_deserializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.DeleteObjectVersionArg.FromString,
                    response_serializer=bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.DeleteObjectVersionResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.bridge.s3_portal.stub.S3PrivateRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.bridge.s3_portal.stub.S3PrivateRpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class S3PrivateRpcService(object):
    """-----------------------------------------------------------------------------

    Set of APIs exposed by S3 portal for internal consumption
    """

    @staticmethod
    def CreateObject(request,
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
            '/cohesity.bridge.s3_portal.stub.S3PrivateRpcService/CreateObject',
            bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.CreateObjectArg.SerializeToString,
            bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.CreateObjectResult.FromString,
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
    def FinalizeObject(request,
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
            '/cohesity.bridge.s3_portal.stub.S3PrivateRpcService/FinalizeObject',
            bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.FinalizeObjectArg.SerializeToString,
            bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.FinalizeObjectResult.FromString,
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
    def GetObjectVersions(request,
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
            '/cohesity.bridge.s3_portal.stub.S3PrivateRpcService/GetObjectVersions',
            bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.GetObjectVersionsArg.SerializeToString,
            bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.GetObjectVersionsResult.FromString,
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
    def DeleteObjectVersion(request,
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
            '/cohesity.bridge.s3_portal.stub.S3PrivateRpcService/DeleteObjectVersion',
            bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.DeleteObjectVersionArg.SerializeToString,
            bridge_dot_s3__portal_dot_grpc__stub_dot_s3__grpc__service__pb2.DeleteObjectVersionResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
