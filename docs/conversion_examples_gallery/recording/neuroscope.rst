Neuroscope data conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^

Convert Neuroscope data to NWB using :py:class:`~neuroconv.datainterfaces.ecephys.neuroscope.neuroscopedatainterface.NeuroscopeRecordingInterface`.

.. code-block:: python

    >>> from datetime import datetime
    >>> from dateutil import tz
    >>> from pathlib import Path
    >>> from neuroconv import NeuroscopeRecordingInterface
    >>>
    >>> # For Neuroscope we need to pass the location of the `.dat` file
    >>> file_path = f"{ECEPHY_DATA_PATH}/neuroscope/test1/test1.dat"
    >>> # Change the file_path to the location in your system
    >>> interface = NeuroscopeRecordingInterface(file_path=file_path, verbose=False)
    >>>
    >>> # Extract what metadata we can from the source files
    >>> metadata = interface.get_metadata()
    >>> # session_start_time is required for conversion. If it cannot be inferred
    >>> # automatically from the source files you must supply one.
    >>> session_start_time = datetime(2020, 1, 1, 12, 30, 0, tzinfo=tz.gettz("US/Pacific"))
    >>> metadata["NWBFile"].update(session_start_time=session_start_time)
    >>>
    >>>  # Choose a path for saving the nwb file and run the conversion
    >>> nwbfile_path = f"{path_to_save_nwbfile}"  # This should be something like: "./saved_file.nwb"
    >>> interface.run_conversion(nwbfile_path=nwbfile_path, metadata=metadata)
    >>>
    >>> # If the conversion was successful this should evaluate to ``True`` as the file was created.
    >>> Path(nwbfile_path).is_file()
    True
