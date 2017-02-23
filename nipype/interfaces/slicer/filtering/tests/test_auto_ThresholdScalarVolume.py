# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..thresholdscalarvolume import ThresholdScalarVolume


def test_ThresholdScalarVolume_inputs():
    input_map = dict(InputVolume=dict(argstr='%s',
    position=-2,
    ),
    OutputVolume=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    lower=dict(argstr='--lower %d',
    ),
    outsidevalue=dict(argstr='--outsidevalue %d',
    ),
    terminal_output=dict(nohash=True,
    ),
    threshold=dict(argstr='--threshold %d',
    ),
    thresholdtype=dict(argstr='--thresholdtype %s',
    ),
    upper=dict(argstr='--upper %d',
    ),
    )
    inputs = ThresholdScalarVolume.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ThresholdScalarVolume_outputs():
    output_map = dict(OutputVolume=dict(position=-1,
    ),
    )
    outputs = ThresholdScalarVolume.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
