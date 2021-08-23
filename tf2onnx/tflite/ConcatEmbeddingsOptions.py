# SPDX-License-Identifier: Apache-2.0

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConcatEmbeddingsOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConcatEmbeddingsOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConcatEmbeddingsOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ConcatEmbeddingsOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # ConcatEmbeddingsOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConcatEmbeddingsOptions
    def NumChannels(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConcatEmbeddingsOptions
    def NumColumnsPerChannel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConcatEmbeddingsOptions
    def NumColumnsPerChannelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ConcatEmbeddingsOptions
    def NumColumnsPerChannelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConcatEmbeddingsOptions
    def NumColumnsPerChannelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # ConcatEmbeddingsOptions
    def EmbeddingDimPerChannel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ConcatEmbeddingsOptions
    def EmbeddingDimPerChannelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ConcatEmbeddingsOptions
    def EmbeddingDimPerChannelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConcatEmbeddingsOptions
    def EmbeddingDimPerChannelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def Start(builder): builder.StartObject(3)
def ConcatEmbeddingsOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNumChannels(builder, numChannels): builder.PrependInt32Slot(0, numChannels, 0)
def ConcatEmbeddingsOptionsAddNumChannels(builder, numChannels):
    """This method is deprecated. Please switch to AddNumChannels."""
    return AddNumChannels(builder, numChannels)
def AddNumColumnsPerChannel(builder, numColumnsPerChannel): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(numColumnsPerChannel), 0)
def ConcatEmbeddingsOptionsAddNumColumnsPerChannel(builder, numColumnsPerChannel):
    """This method is deprecated. Please switch to AddNumColumnsPerChannel."""
    return AddNumColumnsPerChannel(builder, numColumnsPerChannel)
def StartNumColumnsPerChannelVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConcatEmbeddingsOptionsStartNumColumnsPerChannelVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartNumColumnsPerChannelVector(builder, numElems)
def AddEmbeddingDimPerChannel(builder, embeddingDimPerChannel): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(embeddingDimPerChannel), 0)
def ConcatEmbeddingsOptionsAddEmbeddingDimPerChannel(builder, embeddingDimPerChannel):
    """This method is deprecated. Please switch to AddEmbeddingDimPerChannel."""
    return AddEmbeddingDimPerChannel(builder, embeddingDimPerChannel)
def StartEmbeddingDimPerChannelVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ConcatEmbeddingsOptionsStartEmbeddingDimPerChannelVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartEmbeddingDimPerChannelVector(builder, numElems)
def End(builder): return builder.EndObject()
def ConcatEmbeddingsOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)