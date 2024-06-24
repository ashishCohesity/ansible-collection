from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WrappersTestCases(_message.Message):
    __slots__ = ("double_wrapper", "float_wrapper", "int64_wrapper", "uint64_wrapper", "int32_wrapper", "uint32_wrapper", "bool_wrapper", "string_wrapper", "bytes_wrapper", "double_wrapper_default", "float_wrapper_default", "int64_wrapper_default", "uint64_wrapper_default", "int32_wrapper_default", "uint32_wrapper_default", "bool_wrapper_default", "string_wrapper_default", "bytes_wrapper_default")
    DOUBLE_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    FLOAT_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    INT64_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    UINT64_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    INT32_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    UINT32_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    BOOL_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    STRING_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    FLOAT_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    INT64_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    UINT64_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    INT32_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    UINT32_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    BOOL_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    STRING_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRAPPER_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    double_wrapper: DoubleWrapper
    float_wrapper: FloatWrapper
    int64_wrapper: Int64Wrapper
    uint64_wrapper: UInt64Wrapper
    int32_wrapper: Int32Wrapper
    uint32_wrapper: UInt32Wrapper
    bool_wrapper: BoolWrapper
    string_wrapper: StringWrapper
    bytes_wrapper: BytesWrapper
    double_wrapper_default: DoubleWrapper
    float_wrapper_default: FloatWrapper
    int64_wrapper_default: Int64Wrapper
    uint64_wrapper_default: UInt64Wrapper
    int32_wrapper_default: Int32Wrapper
    uint32_wrapper_default: UInt32Wrapper
    bool_wrapper_default: BoolWrapper
    string_wrapper_default: StringWrapper
    bytes_wrapper_default: BytesWrapper
    def __init__(self, double_wrapper: _Optional[_Union[DoubleWrapper, _Mapping]] = ..., float_wrapper: _Optional[_Union[FloatWrapper, _Mapping]] = ..., int64_wrapper: _Optional[_Union[Int64Wrapper, _Mapping]] = ..., uint64_wrapper: _Optional[_Union[UInt64Wrapper, _Mapping]] = ..., int32_wrapper: _Optional[_Union[Int32Wrapper, _Mapping]] = ..., uint32_wrapper: _Optional[_Union[UInt32Wrapper, _Mapping]] = ..., bool_wrapper: _Optional[_Union[BoolWrapper, _Mapping]] = ..., string_wrapper: _Optional[_Union[StringWrapper, _Mapping]] = ..., bytes_wrapper: _Optional[_Union[BytesWrapper, _Mapping]] = ..., double_wrapper_default: _Optional[_Union[DoubleWrapper, _Mapping]] = ..., float_wrapper_default: _Optional[_Union[FloatWrapper, _Mapping]] = ..., int64_wrapper_default: _Optional[_Union[Int64Wrapper, _Mapping]] = ..., uint64_wrapper_default: _Optional[_Union[UInt64Wrapper, _Mapping]] = ..., int32_wrapper_default: _Optional[_Union[Int32Wrapper, _Mapping]] = ..., uint32_wrapper_default: _Optional[_Union[UInt32Wrapper, _Mapping]] = ..., bool_wrapper_default: _Optional[_Union[BoolWrapper, _Mapping]] = ..., string_wrapper_default: _Optional[_Union[StringWrapper, _Mapping]] = ..., bytes_wrapper_default: _Optional[_Union[BytesWrapper, _Mapping]] = ...) -> None: ...

class DoubleWrapper(_message.Message):
    __slots__ = ("double",)
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    double: _wrappers_pb2.DoubleValue
    def __init__(self, double: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...

class FloatWrapper(_message.Message):
    __slots__ = ("float",)
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    float: _wrappers_pb2.FloatValue
    def __init__(self, float: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class Int64Wrapper(_message.Message):
    __slots__ = ("int64",)
    INT64_FIELD_NUMBER: _ClassVar[int]
    int64: _wrappers_pb2.Int64Value
    def __init__(self, int64: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class UInt64Wrapper(_message.Message):
    __slots__ = ("uint64",)
    UINT64_FIELD_NUMBER: _ClassVar[int]
    uint64: _wrappers_pb2.UInt64Value
    def __init__(self, uint64: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ...) -> None: ...

class Int32Wrapper(_message.Message):
    __slots__ = ("int32",)
    INT32_FIELD_NUMBER: _ClassVar[int]
    int32: _wrappers_pb2.Int32Value
    def __init__(self, int32: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class UInt32Wrapper(_message.Message):
    __slots__ = ("uint32",)
    UINT32_FIELD_NUMBER: _ClassVar[int]
    uint32: _wrappers_pb2.UInt32Value
    def __init__(self, uint32: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class BoolWrapper(_message.Message):
    __slots__ = ("bool",)
    BOOL_FIELD_NUMBER: _ClassVar[int]
    bool: _wrappers_pb2.BoolValue
    def __init__(self, bool: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class StringWrapper(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: _wrappers_pb2.StringValue
    def __init__(self, string: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class BytesWrapper(_message.Message):
    __slots__ = ("bytes",)
    BYTES_FIELD_NUMBER: _ClassVar[int]
    bytes: _wrappers_pb2.BytesValue
    def __init__(self, bytes: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...
