# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import FitMSParams

def test_FitMSParams_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    flip_list=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_files=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    out_dir=dict(argstr='%s',
    genfile=True,
    position=-1,
    ),
    subjects_dir=dict(),
    te_list=dict(),
    terminal_output=dict(nohash=True,
    ),
    tr_list=dict(),
    xfm_list=dict(),
    )
    inputs = FitMSParams.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_FitMSParams_outputs():
    output_map = dict(pd_image=dict(),
    t1_image=dict(),
    t2star_image=dict(),
    )
    outputs = FitMSParams.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

