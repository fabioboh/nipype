# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import ApplyDeformations

def test_ApplyDeformations_inputs():
    input_map = dict(deformation_field=dict(field='comp{1}.def',
    mandatory=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_files=dict(field='fnames',
    mandatory=True,
    ),
    interp=dict(field='interp',
    ),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    paths=dict(),
    reference_volume=dict(field='comp{2}.id.space',
    mandatory=True,
    ),
    use_mcr=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    )
    inputs = ApplyDeformations.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ApplyDeformations_outputs():
    output_map = dict(out_files=dict(),
    )
    outputs = ApplyDeformations.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

