from edc_lab import RequisitionPanel

from .processing_profiles import fbc_processing


fbc_panel = RequisitionPanel(
    name="fbc", verbose_name="Full Blood Count", processing_profile=fbc_processing
)
