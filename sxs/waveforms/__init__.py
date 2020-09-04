"""Containers for various types of waveforms


"""


from .waveform_mixin import WaveformMixin
from .waveform_modes import WaveformModes
from .waveform_grid import WaveformGrid
from .waveform_signal import WaveformSignal

from . import nrar, corotating_paired_xor, rotating_paired_xor_multishuffle_bzip2

formats = {
    None: nrar,
    'nrar': nrar,
    'corotating_paired_xor': corotating_paired_xor,
    'rotating_paired_xor': rotating_paired_xor_multishuffle_bzip2,
}