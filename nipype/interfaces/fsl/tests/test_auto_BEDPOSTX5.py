# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..dti import BEDPOSTX5

def test_BEDPOSTX5_inputs():
    input_map = dict(all_ard=dict(argstr='--allard',
    xor=('no_ard', 'all_ard'),
    ),
    args=dict(argstr='%s',
    ),
    burn_in=dict(argstr='-b %d',
    ),
    burn_in_no_ard=dict(argstr='--burninnoard=%d',
    ),
    bvals=dict(mandatory=True,
    ),
    bvecs=dict(mandatory=True,
    ),
    cnlinear=dict(argstr='--cnonlinear',
    xor=('no_spat', 'non_linear', 'cnlinear'),
    ),
    dwi=dict(mandatory=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    f0_ard=dict(argstr='--f0 --ardf0',
    xor=['f0_noard', 'f0_ard', 'all_ard'],
    ),
    f0_noard=dict(argstr='--f0',
    xor=['f0_noard', 'f0_ard'],
    ),
    force_dir=dict(argstr='--forcedir',
    usedefault=True,
    ),
    fudge=dict(argstr='-w %d',
    ),
    gradnonlin=dict(argstr='-g',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    logdir=dict(argstr='--logdir=%s',
    ),
    mask=dict(mandatory=True,
    ),
    model=dict(argstr='-model %d',
    ),
    n_fibres=dict(argstr='-n %d',
    mandatory=True,
    usedefault=True,
    ),
    n_jumps=dict(argstr='-j %d',
    ),
    no_ard=dict(argstr='--noard',
    xor=('no_ard', 'all_ard'),
    ),
    no_spat=dict(argstr='--nospat',
    xor=('no_spat', 'non_linear', 'cnlinear'),
    ),
    non_linear=dict(argstr='--nonlinear',
    xor=('no_spat', 'non_linear', 'cnlinear'),
    ),
    out_dir=dict(argstr='%s',
    mandatory=True,
    position=1,
    usedefault=True,
    ),
    output_type=dict(),
    rician=dict(argstr='--rician',
    ),
    sample_every=dict(argstr='-s %d',
    ),
    seed=dict(argstr='--seed=%d',
    ),
    terminal_output=dict(nohash=True,
    ),
    update_proposal_every=dict(argstr='--updateproposalevery=%d',
    ),
    use_gpu=dict(),
    )
    inputs = BEDPOSTX5.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_BEDPOSTX5_outputs():
    output_map = dict(dyads=dict(),
    dyads_dispersion=dict(),
    mean_S0samples=dict(),
    mean_dsamples=dict(),
    mean_fsamples=dict(),
    mean_phsamples=dict(),
    mean_thsamples=dict(),
    merged_fsamples=dict(),
    merged_phsamples=dict(),
    merged_thsamples=dict(),
    )
    outputs = BEDPOSTX5.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

