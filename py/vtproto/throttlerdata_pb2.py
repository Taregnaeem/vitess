# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: throttlerdata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='throttlerdata.proto',
  package='throttlerdata',
  syntax='proto3',
  serialized_pb=_b('\n\x13throttlerdata.proto\x12\rthrottlerdata\"\x11\n\x0fMaxRatesRequest\"{\n\x10MaxRatesResponse\x12\x39\n\x05rates\x18\x01 \x03(\x0b\x32*.throttlerdata.MaxRatesResponse.RatesEntry\x1a,\n\nRatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"!\n\x11SetMaxRateRequest\x12\x0c\n\x04rate\x18\x01 \x01(\x03\"#\n\x12SetMaxRateResponse\x12\r\n\x05names\x18\x01 \x03(\t\"\xc3\x03\n\rConfiguration\x12\"\n\x1atarget_replication_lag_sec\x18\x01 \x01(\x03\x12\x1f\n\x17max_replication_lag_sec\x18\x02 \x01(\x03\x12\x14\n\x0cinitial_rate\x18\x03 \x01(\x03\x12\x14\n\x0cmax_increase\x18\x04 \x01(\x01\x12\x1a\n\x12\x65mergency_decrease\x18\x05 \x01(\x01\x12*\n\"min_duration_between_increases_sec\x18\x06 \x01(\x03\x12*\n\"max_duration_between_increases_sec\x18\x07 \x01(\x03\x12*\n\"min_duration_between_decreases_sec\x18\x08 \x01(\x03\x12!\n\x19spread_backlog_across_sec\x18\t \x01(\x03\x12!\n\x19ignore_n_slowest_replicas\x18\n \x01(\x05\x12 \n\x18ignore_n_slowest_rdonlys\x18\x0b \x01(\x05\x12\x1e\n\x16\x61ge_bad_rate_after_sec\x18\x0c \x01(\x03\x12\x19\n\x11\x62\x61\x64_rate_increase\x18\r \x01(\x01\"1\n\x17GetConfigurationRequest\x12\x16\n\x0ethrottler_name\x18\x01 \x01(\t\"\xc4\x01\n\x18GetConfigurationResponse\x12S\n\x0e\x63onfigurations\x18\x01 \x03(\x0b\x32;.throttlerdata.GetConfigurationResponse.ConfigurationsEntry\x1aS\n\x13\x43onfigurationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.throttlerdata.Configuration:\x02\x38\x01\"\x83\x01\n\x1aUpdateConfigurationRequest\x12\x16\n\x0ethrottler_name\x18\x01 \x01(\t\x12\x33\n\rconfiguration\x18\x02 \x01(\x0b\x32\x1c.throttlerdata.Configuration\x12\x18\n\x10\x63opy_zero_values\x18\x03 \x01(\x08\",\n\x1bUpdateConfigurationResponse\x12\r\n\x05names\x18\x01 \x03(\t\"3\n\x19ResetConfigurationRequest\x12\x16\n\x0ethrottler_name\x18\x01 \x01(\t\"+\n\x1aResetConfigurationResponse\x12\r\n\x05names\x18\x01 \x03(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAXRATESREQUEST = _descriptor.Descriptor(
  name='MaxRatesRequest',
  full_name='throttlerdata.MaxRatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=38,
  serialized_end=55,
)


_MAXRATESRESPONSE_RATESENTRY = _descriptor.Descriptor(
  name='RatesEntry',
  full_name='throttlerdata.MaxRatesResponse.RatesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='throttlerdata.MaxRatesResponse.RatesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='throttlerdata.MaxRatesResponse.RatesEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=136,
  serialized_end=180,
)

_MAXRATESRESPONSE = _descriptor.Descriptor(
  name='MaxRatesResponse',
  full_name='throttlerdata.MaxRatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rates', full_name='throttlerdata.MaxRatesResponse.rates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAXRATESRESPONSE_RATESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=180,
)


_SETMAXRATEREQUEST = _descriptor.Descriptor(
  name='SetMaxRateRequest',
  full_name='throttlerdata.SetMaxRateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rate', full_name='throttlerdata.SetMaxRateRequest.rate', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=182,
  serialized_end=215,
)


_SETMAXRATERESPONSE = _descriptor.Descriptor(
  name='SetMaxRateResponse',
  full_name='throttlerdata.SetMaxRateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='throttlerdata.SetMaxRateResponse.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=217,
  serialized_end=252,
)


_CONFIGURATION = _descriptor.Descriptor(
  name='Configuration',
  full_name='throttlerdata.Configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_replication_lag_sec', full_name='throttlerdata.Configuration.target_replication_lag_sec', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_replication_lag_sec', full_name='throttlerdata.Configuration.max_replication_lag_sec', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial_rate', full_name='throttlerdata.Configuration.initial_rate', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_increase', full_name='throttlerdata.Configuration.max_increase', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emergency_decrease', full_name='throttlerdata.Configuration.emergency_decrease', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_duration_between_increases_sec', full_name='throttlerdata.Configuration.min_duration_between_increases_sec', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_duration_between_increases_sec', full_name='throttlerdata.Configuration.max_duration_between_increases_sec', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_duration_between_decreases_sec', full_name='throttlerdata.Configuration.min_duration_between_decreases_sec', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spread_backlog_across_sec', full_name='throttlerdata.Configuration.spread_backlog_across_sec', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_n_slowest_replicas', full_name='throttlerdata.Configuration.ignore_n_slowest_replicas', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_n_slowest_rdonlys', full_name='throttlerdata.Configuration.ignore_n_slowest_rdonlys', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='age_bad_rate_after_sec', full_name='throttlerdata.Configuration.age_bad_rate_after_sec', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bad_rate_increase', full_name='throttlerdata.Configuration.bad_rate_increase', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=255,
  serialized_end=706,
)


_GETCONFIGURATIONREQUEST = _descriptor.Descriptor(
  name='GetConfigurationRequest',
  full_name='throttlerdata.GetConfigurationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='throttler_name', full_name='throttlerdata.GetConfigurationRequest.throttler_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=708,
  serialized_end=757,
)


_GETCONFIGURATIONRESPONSE_CONFIGURATIONSENTRY = _descriptor.Descriptor(
  name='ConfigurationsEntry',
  full_name='throttlerdata.GetConfigurationResponse.ConfigurationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='throttlerdata.GetConfigurationResponse.ConfigurationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='throttlerdata.GetConfigurationResponse.ConfigurationsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=873,
  serialized_end=956,
)

_GETCONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='GetConfigurationResponse',
  full_name='throttlerdata.GetConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configurations', full_name='throttlerdata.GetConfigurationResponse.configurations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETCONFIGURATIONRESPONSE_CONFIGURATIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=760,
  serialized_end=956,
)


_UPDATECONFIGURATIONREQUEST = _descriptor.Descriptor(
  name='UpdateConfigurationRequest',
  full_name='throttlerdata.UpdateConfigurationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='throttler_name', full_name='throttlerdata.UpdateConfigurationRequest.throttler_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='configuration', full_name='throttlerdata.UpdateConfigurationRequest.configuration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='copy_zero_values', full_name='throttlerdata.UpdateConfigurationRequest.copy_zero_values', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=959,
  serialized_end=1090,
)


_UPDATECONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='UpdateConfigurationResponse',
  full_name='throttlerdata.UpdateConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='throttlerdata.UpdateConfigurationResponse.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1092,
  serialized_end=1136,
)


_RESETCONFIGURATIONREQUEST = _descriptor.Descriptor(
  name='ResetConfigurationRequest',
  full_name='throttlerdata.ResetConfigurationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='throttler_name', full_name='throttlerdata.ResetConfigurationRequest.throttler_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1138,
  serialized_end=1189,
)


_RESETCONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='ResetConfigurationResponse',
  full_name='throttlerdata.ResetConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='throttlerdata.ResetConfigurationResponse.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1191,
  serialized_end=1234,
)

_MAXRATESRESPONSE_RATESENTRY.containing_type = _MAXRATESRESPONSE
_MAXRATESRESPONSE.fields_by_name['rates'].message_type = _MAXRATESRESPONSE_RATESENTRY
_GETCONFIGURATIONRESPONSE_CONFIGURATIONSENTRY.fields_by_name['value'].message_type = _CONFIGURATION
_GETCONFIGURATIONRESPONSE_CONFIGURATIONSENTRY.containing_type = _GETCONFIGURATIONRESPONSE
_GETCONFIGURATIONRESPONSE.fields_by_name['configurations'].message_type = _GETCONFIGURATIONRESPONSE_CONFIGURATIONSENTRY
_UPDATECONFIGURATIONREQUEST.fields_by_name['configuration'].message_type = _CONFIGURATION
DESCRIPTOR.message_types_by_name['MaxRatesRequest'] = _MAXRATESREQUEST
DESCRIPTOR.message_types_by_name['MaxRatesResponse'] = _MAXRATESRESPONSE
DESCRIPTOR.message_types_by_name['SetMaxRateRequest'] = _SETMAXRATEREQUEST
DESCRIPTOR.message_types_by_name['SetMaxRateResponse'] = _SETMAXRATERESPONSE
DESCRIPTOR.message_types_by_name['Configuration'] = _CONFIGURATION
DESCRIPTOR.message_types_by_name['GetConfigurationRequest'] = _GETCONFIGURATIONREQUEST
DESCRIPTOR.message_types_by_name['GetConfigurationResponse'] = _GETCONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['UpdateConfigurationRequest'] = _UPDATECONFIGURATIONREQUEST
DESCRIPTOR.message_types_by_name['UpdateConfigurationResponse'] = _UPDATECONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['ResetConfigurationRequest'] = _RESETCONFIGURATIONREQUEST
DESCRIPTOR.message_types_by_name['ResetConfigurationResponse'] = _RESETCONFIGURATIONRESPONSE

MaxRatesRequest = _reflection.GeneratedProtocolMessageType('MaxRatesRequest', (_message.Message,), dict(
  DESCRIPTOR = _MAXRATESREQUEST,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.MaxRatesRequest)
  ))
_sym_db.RegisterMessage(MaxRatesRequest)

MaxRatesResponse = _reflection.GeneratedProtocolMessageType('MaxRatesResponse', (_message.Message,), dict(

  RatesEntry = _reflection.GeneratedProtocolMessageType('RatesEntry', (_message.Message,), dict(
    DESCRIPTOR = _MAXRATESRESPONSE_RATESENTRY,
    __module__ = 'throttlerdata_pb2'
    # @@protoc_insertion_point(class_scope:throttlerdata.MaxRatesResponse.RatesEntry)
    ))
  ,
  DESCRIPTOR = _MAXRATESRESPONSE,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.MaxRatesResponse)
  ))
_sym_db.RegisterMessage(MaxRatesResponse)
_sym_db.RegisterMessage(MaxRatesResponse.RatesEntry)

SetMaxRateRequest = _reflection.GeneratedProtocolMessageType('SetMaxRateRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETMAXRATEREQUEST,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.SetMaxRateRequest)
  ))
_sym_db.RegisterMessage(SetMaxRateRequest)

SetMaxRateResponse = _reflection.GeneratedProtocolMessageType('SetMaxRateResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETMAXRATERESPONSE,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.SetMaxRateResponse)
  ))
_sym_db.RegisterMessage(SetMaxRateResponse)

Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATION,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.Configuration)
  ))
_sym_db.RegisterMessage(Configuration)

GetConfigurationRequest = _reflection.GeneratedProtocolMessageType('GetConfigurationRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGURATIONREQUEST,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.GetConfigurationRequest)
  ))
_sym_db.RegisterMessage(GetConfigurationRequest)

GetConfigurationResponse = _reflection.GeneratedProtocolMessageType('GetConfigurationResponse', (_message.Message,), dict(

  ConfigurationsEntry = _reflection.GeneratedProtocolMessageType('ConfigurationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _GETCONFIGURATIONRESPONSE_CONFIGURATIONSENTRY,
    __module__ = 'throttlerdata_pb2'
    # @@protoc_insertion_point(class_scope:throttlerdata.GetConfigurationResponse.ConfigurationsEntry)
    ))
  ,
  DESCRIPTOR = _GETCONFIGURATIONRESPONSE,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.GetConfigurationResponse)
  ))
_sym_db.RegisterMessage(GetConfigurationResponse)
_sym_db.RegisterMessage(GetConfigurationResponse.ConfigurationsEntry)

UpdateConfigurationRequest = _reflection.GeneratedProtocolMessageType('UpdateConfigurationRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECONFIGURATIONREQUEST,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.UpdateConfigurationRequest)
  ))
_sym_db.RegisterMessage(UpdateConfigurationRequest)

UpdateConfigurationResponse = _reflection.GeneratedProtocolMessageType('UpdateConfigurationResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECONFIGURATIONRESPONSE,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.UpdateConfigurationResponse)
  ))
_sym_db.RegisterMessage(UpdateConfigurationResponse)

ResetConfigurationRequest = _reflection.GeneratedProtocolMessageType('ResetConfigurationRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESETCONFIGURATIONREQUEST,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.ResetConfigurationRequest)
  ))
_sym_db.RegisterMessage(ResetConfigurationRequest)

ResetConfigurationResponse = _reflection.GeneratedProtocolMessageType('ResetConfigurationResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESETCONFIGURATIONRESPONSE,
  __module__ = 'throttlerdata_pb2'
  # @@protoc_insertion_point(class_scope:throttlerdata.ResetConfigurationResponse)
  ))
_sym_db.RegisterMessage(ResetConfigurationResponse)


_MAXRATESRESPONSE_RATESENTRY.has_options = True
_MAXRATESRESPONSE_RATESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_GETCONFIGURATIONRESPONSE_CONFIGURATIONSENTRY.has_options = True
_GETCONFIGURATIONRESPONSE_CONFIGURATIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
