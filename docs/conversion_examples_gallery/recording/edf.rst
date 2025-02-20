European Data Format (EDF) conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Convert edf data to NWB using :py:class:`~neuroconv.datainterfaces.ecephys.edf.edfdatainterface.EDFRecordingInterface`.

.. code-block:: python

    >>> from datetime import datetime
    >>> from dateutil import tz
    >>> from pathlib import Path
    >>> from neuroconv import EDFRecordingInterface
    >>>
    >>> # For this interface we need to pass the specific path to the files.
    >>> file_path = f"{ECEPHY_DATA_PATH}/edf/edf+C.edf"
    >>> # Change the file_path to the location in your system
    >>> interface = EDFRecordingInterface(file_path=file_path, verbose=False)
    >>>
    >>> # Extract what metadata we can from the source files
    >>> metadata = interface.get_metadata()
    >>> # For data provenance we add the time zone information to the conversion
    >>> session_start_time = datetime(2020, 1, 1, 12, 30, 0, tzinfo=tz.gettz("US/Pacific")).isoformat()
    >>> metadata["NWBFile"].update(session_start_time=session_start_time)
    >>>
    >>> # Choose a path for saving the nwb file and run the conversion
    >>> nwbfile_path = f"{path_to_save_nwbfile}"
    >>> interface.run_conversion(nwbfile_path=nwbfile_path, metadata=metadata)
    >>>
    >>> # If the conversion was successful this should evaluate to ``True`` as the file was created.
    >>> Path(nwbfile_path).is_file()
    True
