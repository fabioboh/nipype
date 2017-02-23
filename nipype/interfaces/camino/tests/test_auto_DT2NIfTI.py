# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..convert import DT2NIfTI


def test_DT2NIfTI_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    header_file=dict(argstr='-header %s',
    mandatory=True,
    position=3,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-inputfile %s',
    mandatory=True,
    position=1,
    ),
    output_root=dict(argstr='-outputroot %s',
    genfile=True,
    position=2,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = DT2NIfTI.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DT2NIfTI_outputs():
    output_map = dict(dt=dict(),
    exitcode=dict(),
    lns0=dict(),
    )
    outputs = DT2NIfTI.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
