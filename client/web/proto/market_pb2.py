# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: market.proto
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
    'market.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmarket.proto\x12\x06market\"9\n\nInstrument\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x01\"F\n\x05Order\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x01\x12\x10\n\x08quantity\x18\x04 \x01(\x05\"\x18\n\x06Symbol\x12\x0e\n\x06symbol\x18\x01 \x01(\t\"b\n\tOrderBook\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12!\n\nbuy_orders\x18\x02 \x03(\x0b\x32\r.market.Order\x12\"\n\x0bsell_orders\x18\x03 \x03(\x0b\x32\r.market.Order\",\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"9\n\x0eInstrumentList\x12\'\n\x0binstruments\x18\x01 \x03(\x0b\x32\x12.market.Instrument\"\x07\n\x05\x45mpty2\xe4\x01\n\rMarketService\x12\x35\n\rAddInstrument\x12\x12.market.Instrument\x1a\x10.market.Response\x12\x38\n\x0fListInstruments\x12\r.market.Empty\x1a\x16.market.InstrumentList\x12-\n\nPlaceOrder\x12\r.market.Order\x1a\x10.market.Response\x12\x33\n\x0eQueryOrderBook\x12\x0e.market.Symbol\x1a\x11.market.OrderBookb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'market_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_INSTRUMENT']._serialized_start=24
  _globals['_INSTRUMENT']._serialized_end=81
  _globals['_ORDER']._serialized_start=83
  _globals['_ORDER']._serialized_end=153
  _globals['_SYMBOL']._serialized_start=155
  _globals['_SYMBOL']._serialized_end=179
  _globals['_ORDERBOOK']._serialized_start=181
  _globals['_ORDERBOOK']._serialized_end=279
  _globals['_RESPONSE']._serialized_start=281
  _globals['_RESPONSE']._serialized_end=325
  _globals['_INSTRUMENTLIST']._serialized_start=327
  _globals['_INSTRUMENTLIST']._serialized_end=384
  _globals['_EMPTY']._serialized_start=386
  _globals['_EMPTY']._serialized_end=393
  _globals['_MARKETSERVICE']._serialized_start=396
  _globals['_MARKETSERVICE']._serialized_end=624
# @@protoc_insertion_point(module_scope)
