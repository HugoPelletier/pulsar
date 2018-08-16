#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Function.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Function.proto',
  package='proto',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x46unction.proto\x12\x05proto\"3\n\tResources\x12\x0b\n\x03\x63pu\x18\x01 \x01(\x01\x12\x0b\n\x03ram\x18\x02 \x01(\x03\x12\x0c\n\x04\x64isk\x18\x03 \x01(\x03\"\xa9\x03\n\x0f\x46unctionDetails\x12\x0e\n\x06tenant\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tclassName\x18\x04 \x01(\t\x12\x10\n\x08logTopic\x18\x05 \x01(\t\x12\x39\n\x14processingGuarantees\x18\x06 \x01(\x0e\x32\x1b.proto.ProcessingGuarantees\x12\x12\n\nuserConfig\x18\x07 \x01(\t\x12/\n\x07runtime\x18\x08 \x01(\x0e\x32\x1e.proto.FunctionDetails.Runtime\x12\x0f\n\x07\x61utoAck\x18\t \x01(\x08\x12\x13\n\x0bparallelism\x18\n \x01(\x05\x12!\n\x06source\x18\x0b \x01(\x0b\x32\x11.proto.SourceSpec\x12\x1d\n\x04sink\x18\x0c \x01(\x0b\x32\x0f.proto.SinkSpec\x12#\n\tresources\x18\r \x01(\x0b\x32\x10.proto.Resources\x12\x12\n\npackageUrl\x18\x0e \x01(\t\"\x1f\n\x07Runtime\x12\x08\n\x04JAVA\x10\x00\x12\n\n\x06PYTHON\x10\x01\"\xdd\x02\n\nSourceSpec\x12\x11\n\tclassName\x18\x01 \x01(\t\x12\x0f\n\x07\x63onfigs\x18\x02 \x01(\t\x12\x15\n\rtypeClassName\x18\x05 \x01(\t\x12\x31\n\x10subscriptionType\x18\x03 \x01(\x0e\x32\x17.proto.SubscriptionType\x12M\n\x16topicsToSerDeClassName\x18\x04 \x03(\x0b\x32-.proto.SourceSpec.TopicsToSerDeClassNameEntry\x12\x11\n\ttimeoutMs\x18\x06 \x01(\x04\x12\x15\n\rtopicsPattern\x18\x07 \x01(\t\x12\x0f\n\x07\x62uiltin\x18\x08 \x01(\t\x12\x18\n\x10subscriptionName\x18\t \x01(\t\x1a=\n\x1bTopicsToSerDeClassNameEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"}\n\x08SinkSpec\x12\x11\n\tclassName\x18\x01 \x01(\t\x12\x0f\n\x07\x63onfigs\x18\x02 \x01(\t\x12\x15\n\rtypeClassName\x18\x05 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\x12\x16\n\x0eserDeClassName\x18\x04 \x01(\t\x12\x0f\n\x07\x62uiltin\x18\x06 \x01(\t\".\n\x17PackageLocationMetaData\x12\x13\n\x0bpackagePath\x18\x01 \x01(\t\"\xa1\x01\n\x10\x46unctionMetaData\x12/\n\x0f\x66unctionDetails\x18\x01 \x01(\x0b\x32\x16.proto.FunctionDetails\x12\x37\n\x0fpackageLocation\x18\x02 \x01(\x0b\x32\x1e.proto.PackageLocationMetaData\x12\x0f\n\x07version\x18\x03 \x01(\x04\x12\x12\n\ncreateTime\x18\x04 \x01(\x04\"Q\n\x08Instance\x12\x31\n\x10\x66unctionMetaData\x18\x01 \x01(\x0b\x32\x17.proto.FunctionMetaData\x12\x12\n\ninstanceId\x18\x02 \x01(\x05\"A\n\nAssignment\x12!\n\x08instance\x18\x01 \x01(\x0b\x32\x0f.proto.Instance\x12\x10\n\x08workerId\x18\x02 \x01(\t*O\n\x14ProcessingGuarantees\x12\x10\n\x0c\x41TLEAST_ONCE\x10\x00\x12\x0f\n\x0b\x41TMOST_ONCE\x10\x01\x12\x14\n\x10\x45\x46\x46\x45\x43TIVELY_ONCE\x10\x02*,\n\x10SubscriptionType\x12\n\n\x06SHARED\x10\x00\x12\x0c\n\x08\x46\x41ILOVER\x10\x01\x42-\n!org.apache.pulsar.functions.protoB\x08\x46unctionb\x06proto3')
)

_PROCESSINGGUARANTEES = _descriptor.EnumDescriptor(
  name='ProcessingGuarantees',
  full_name='proto.ProcessingGuarantees',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ATLEAST_ONCE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATMOST_ONCE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EFFECTIVELY_ONCE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1347,
  serialized_end=1426,
)
_sym_db.RegisterEnumDescriptor(_PROCESSINGGUARANTEES)

ProcessingGuarantees = enum_type_wrapper.EnumTypeWrapper(_PROCESSINGGUARANTEES)
_SUBSCRIPTIONTYPE = _descriptor.EnumDescriptor(
  name='SubscriptionType',
  full_name='proto.SubscriptionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SHARED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILOVER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1428,
  serialized_end=1472,
)
_sym_db.RegisterEnumDescriptor(_SUBSCRIPTIONTYPE)

SubscriptionType = enum_type_wrapper.EnumTypeWrapper(_SUBSCRIPTIONTYPE)
ATLEAST_ONCE = 0
ATMOST_ONCE = 1
EFFECTIVELY_ONCE = 2
SHARED = 0
FAILOVER = 1


_FUNCTIONDETAILS_RUNTIME = _descriptor.EnumDescriptor(
  name='Runtime',
  full_name='proto.FunctionDetails.Runtime',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JAVA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PYTHON', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=473,
  serialized_end=504,
)
_sym_db.RegisterEnumDescriptor(_FUNCTIONDETAILS_RUNTIME)


_RESOURCES = _descriptor.Descriptor(
  name='Resources',
  full_name='proto.Resources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='proto.Resources.cpu', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ram', full_name='proto.Resources.ram', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk', full_name='proto.Resources.disk', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=76,
)


_FUNCTIONDETAILS = _descriptor.Descriptor(
  name='FunctionDetails',
  full_name='proto.FunctionDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tenant', full_name='proto.FunctionDetails.tenant', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='proto.FunctionDetails.namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.FunctionDetails.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='className', full_name='proto.FunctionDetails.className', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logTopic', full_name='proto.FunctionDetails.logTopic', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processingGuarantees', full_name='proto.FunctionDetails.processingGuarantees', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userConfig', full_name='proto.FunctionDetails.userConfig', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='proto.FunctionDetails.runtime', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autoAck', full_name='proto.FunctionDetails.autoAck', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parallelism', full_name='proto.FunctionDetails.parallelism', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='proto.FunctionDetails.source', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sink', full_name='proto.FunctionDetails.sink', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resources', full_name='proto.FunctionDetails.resources', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageUrl', full_name='proto.FunctionDetails.packageUrl', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FUNCTIONDETAILS_RUNTIME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=504,
)


_SOURCESPEC_TOPICSTOSERDECLASSNAMEENTRY = _descriptor.Descriptor(
  name='TopicsToSerDeClassNameEntry',
  full_name='proto.SourceSpec.TopicsToSerDeClassNameEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.SourceSpec.TopicsToSerDeClassNameEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.SourceSpec.TopicsToSerDeClassNameEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=795,
  serialized_end=856,
)

_SOURCESPEC = _descriptor.Descriptor(
  name='SourceSpec',
  full_name='proto.SourceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='className', full_name='proto.SourceSpec.className', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configs', full_name='proto.SourceSpec.configs', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typeClassName', full_name='proto.SourceSpec.typeClassName', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptionType', full_name='proto.SourceSpec.subscriptionType', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topicsToSerDeClassName', full_name='proto.SourceSpec.topicsToSerDeClassName', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeoutMs', full_name='proto.SourceSpec.timeoutMs', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topicsPattern', full_name='proto.SourceSpec.topicsPattern', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='builtin', full_name='proto.SourceSpec.builtin', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptionName', full_name='proto.SourceSpec.subscriptionName', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SOURCESPEC_TOPICSTOSERDECLASSNAMEENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=856,
)


_SINKSPEC = _descriptor.Descriptor(
  name='SinkSpec',
  full_name='proto.SinkSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='className', full_name='proto.SinkSpec.className', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configs', full_name='proto.SinkSpec.configs', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typeClassName', full_name='proto.SinkSpec.typeClassName', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic', full_name='proto.SinkSpec.topic', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serDeClassName', full_name='proto.SinkSpec.serDeClassName', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='builtin', full_name='proto.SinkSpec.builtin', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=858,
  serialized_end=983,
)


_PACKAGELOCATIONMETADATA = _descriptor.Descriptor(
  name='PackageLocationMetaData',
  full_name='proto.PackageLocationMetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packagePath', full_name='proto.PackageLocationMetaData.packagePath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=985,
  serialized_end=1031,
)


_FUNCTIONMETADATA = _descriptor.Descriptor(
  name='FunctionMetaData',
  full_name='proto.FunctionMetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='functionDetails', full_name='proto.FunctionMetaData.functionDetails', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageLocation', full_name='proto.FunctionMetaData.packageLocation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='proto.FunctionMetaData.version', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='proto.FunctionMetaData.createTime', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1034,
  serialized_end=1195,
)


_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='proto.Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='functionMetaData', full_name='proto.Instance.functionMetaData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='proto.Instance.instanceId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1197,
  serialized_end=1278,
)


_ASSIGNMENT = _descriptor.Descriptor(
  name='Assignment',
  full_name='proto.Assignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='proto.Assignment.instance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workerId', full_name='proto.Assignment.workerId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1280,
  serialized_end=1345,
)

_FUNCTIONDETAILS.fields_by_name['processingGuarantees'].enum_type = _PROCESSINGGUARANTEES
_FUNCTIONDETAILS.fields_by_name['runtime'].enum_type = _FUNCTIONDETAILS_RUNTIME
_FUNCTIONDETAILS.fields_by_name['source'].message_type = _SOURCESPEC
_FUNCTIONDETAILS.fields_by_name['sink'].message_type = _SINKSPEC
_FUNCTIONDETAILS.fields_by_name['resources'].message_type = _RESOURCES
_FUNCTIONDETAILS_RUNTIME.containing_type = _FUNCTIONDETAILS
_SOURCESPEC_TOPICSTOSERDECLASSNAMEENTRY.containing_type = _SOURCESPEC
_SOURCESPEC.fields_by_name['subscriptionType'].enum_type = _SUBSCRIPTIONTYPE
_SOURCESPEC.fields_by_name['topicsToSerDeClassName'].message_type = _SOURCESPEC_TOPICSTOSERDECLASSNAMEENTRY
_FUNCTIONMETADATA.fields_by_name['functionDetails'].message_type = _FUNCTIONDETAILS
_FUNCTIONMETADATA.fields_by_name['packageLocation'].message_type = _PACKAGELOCATIONMETADATA
_INSTANCE.fields_by_name['functionMetaData'].message_type = _FUNCTIONMETADATA
_ASSIGNMENT.fields_by_name['instance'].message_type = _INSTANCE
DESCRIPTOR.message_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.message_types_by_name['FunctionDetails'] = _FUNCTIONDETAILS
DESCRIPTOR.message_types_by_name['SourceSpec'] = _SOURCESPEC
DESCRIPTOR.message_types_by_name['SinkSpec'] = _SINKSPEC
DESCRIPTOR.message_types_by_name['PackageLocationMetaData'] = _PACKAGELOCATIONMETADATA
DESCRIPTOR.message_types_by_name['FunctionMetaData'] = _FUNCTIONMETADATA
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['Assignment'] = _ASSIGNMENT
DESCRIPTOR.enum_types_by_name['ProcessingGuarantees'] = _PROCESSINGGUARANTEES
DESCRIPTOR.enum_types_by_name['SubscriptionType'] = _SUBSCRIPTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCES,
  __module__ = 'Function_pb2'
  # @@protoc_insertion_point(class_scope:proto.Resources)
  ))
_sym_db.RegisterMessage(Resources)

FunctionDetails = _reflection.GeneratedProtocolMessageType('FunctionDetails', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONDETAILS,
  __module__ = 'Function_pb2'
  # @@protoc_insertion_point(class_scope:proto.FunctionDetails)
  ))
_sym_db.RegisterMessage(FunctionDetails)

SourceSpec = _reflection.GeneratedProtocolMessageType('SourceSpec', (_message.Message,), dict(

  TopicsToSerDeClassNameEntry = _reflection.GeneratedProtocolMessageType('TopicsToSerDeClassNameEntry', (_message.Message,), dict(
    DESCRIPTOR = _SOURCESPEC_TOPICSTOSERDECLASSNAMEENTRY,
    __module__ = 'Function_pb2'
    # @@protoc_insertion_point(class_scope:proto.SourceSpec.TopicsToSerDeClassNameEntry)
    ))
  ,
  DESCRIPTOR = _SOURCESPEC,
  __module__ = 'Function_pb2'
  # @@protoc_insertion_point(class_scope:proto.SourceSpec)
  ))
_sym_db.RegisterMessage(SourceSpec)
_sym_db.RegisterMessage(SourceSpec.TopicsToSerDeClassNameEntry)

SinkSpec = _reflection.GeneratedProtocolMessageType('SinkSpec', (_message.Message,), dict(
  DESCRIPTOR = _SINKSPEC,
  __module__ = 'Function_pb2'
  # @@protoc_insertion_point(class_scope:proto.SinkSpec)
  ))
_sym_db.RegisterMessage(SinkSpec)

PackageLocationMetaData = _reflection.GeneratedProtocolMessageType('PackageLocationMetaData', (_message.Message,), dict(
  DESCRIPTOR = _PACKAGELOCATIONMETADATA,
  __module__ = 'Function_pb2'
  # @@protoc_insertion_point(class_scope:proto.PackageLocationMetaData)
  ))
_sym_db.RegisterMessage(PackageLocationMetaData)

FunctionMetaData = _reflection.GeneratedProtocolMessageType('FunctionMetaData', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONMETADATA,
  __module__ = 'Function_pb2'
  # @@protoc_insertion_point(class_scope:proto.FunctionMetaData)
  ))
_sym_db.RegisterMessage(FunctionMetaData)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCE,
  __module__ = 'Function_pb2'
  # @@protoc_insertion_point(class_scope:proto.Instance)
  ))
_sym_db.RegisterMessage(Instance)

Assignment = _reflection.GeneratedProtocolMessageType('Assignment', (_message.Message,), dict(
  DESCRIPTOR = _ASSIGNMENT,
  __module__ = 'Function_pb2'
  # @@protoc_insertion_point(class_scope:proto.Assignment)
  ))
_sym_db.RegisterMessage(Assignment)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!org.apache.pulsar.functions.protoB\010Function'))
_SOURCESPEC_TOPICSTOSERDECLASSNAMEENTRY.has_options = True
_SOURCESPEC_TOPICSTOSERDECLASSNAMEENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
