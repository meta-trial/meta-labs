from edc_lab import LabProfile

from .panels import fbc_panel


subject_lab_profile = LabProfile(
    name="subject_lab_profile", requisition_model="ambition_subject.subjectrequisition"
)

subject_lab_profile.add_panel(fbc_panel)
