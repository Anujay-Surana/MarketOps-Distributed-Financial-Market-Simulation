# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: analytics.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'analytics.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61nalytics.proto\x12\tanalytics\"\x18\n\x06Symbol\x12\x0e\n\x06symbol\x18\x01 \x01(\t\"b\n\x0cPriceSummary\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x15\n\raverage_price\x18\x02 \x01(\x01\x12\x15\n\rhighest_price\x18\x03 \x01(\x01\x12\x14\n\x0clowest_price\x18\x04 \x01(\x01\"/\n\x0cVolumeTrends\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0f\n\x07volumes\x18\x02 \x03(\x01\x32\x90\x01\n\x10\x41nalyticsService\x12=\n\x0fGetPriceSummary\x12\x11.analytics.Symbol\x1a\x17.analytics.PriceSummary\x12=\n\x0fGetVolumeTrends\x12\x11.analytics.Symbol\x1a\x17.analytics.VolumeTrendsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analytics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SYMBOL']._serialized_start=30
  _globals['_SYMBOL']._serialized_end=54
  _globals['_PRICESUMMARY']._serialized_start=56
  _globals['_PRICESUMMARY']._serialized_end=154
  _globals['_VOLUMETRENDS']._serialized_start=156
  _globals['_VOLUMETRENDS']._serialized_end=203
  _globals['_ANALYTICSSERVICE']._serialized_start=206
  _globals['_ANALYTICSSERVICE']._serialized_end=350
# @@protoc_insertion_point(module_scope)
