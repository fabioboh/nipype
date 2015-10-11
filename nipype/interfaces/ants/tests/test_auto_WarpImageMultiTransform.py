# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..resampling import WarpImageMultiTransform

def test_WarpImageMultiTransform_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    dimension=dict(argstr='%d',
    position=1,
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    input_image=dict(argstr='%s',
    mandatory=True,
    position=2,
    ),
    invert_affine=dict(),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    out_postfix=dict(hash_files=False,
    usedefault=True,
    xor=['output_image'],
    ),
    output_image=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    position=3,
    xor=['out_postfix'],
    ),
    reference_image=dict(argstr='-R %s',
    xor=['tightest_box'],
    ),
    reslice_by_header=dict(argstr='--reslice-by-header',
    ),
    terminal_output=dict(nohash=True,
    ),
    tightest_box=dict(argstr='--tightest-bounding-box',
    xor=['reference_image'],
    ),
    transformation_series=dict(argstr='%s',
    mandatory=True,
    position=-1,
    ),
    use_bspline=dict(argstr='--use-BSpline',
    ),
    use_nearest=dict(argstr='--use-NN',
    ),
    )
    inputs = WarpImageMultiTransform.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_WarpImageMultiTransform_outputs():
    output_map = dict(output_image=dict(),
    )
    outputs = WarpImageMultiTransform.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

