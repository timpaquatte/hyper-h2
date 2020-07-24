import pytest_mutagen as mg

mg.link_to_file(mg.APPLY_TO_ALL)

# Mutations on H2Connection

from h2.connection import H2Connection

@mg.mutant_of("H2Connection._prepare_for_sending", "PREPARE_FOR_SENDING_NONE")
def _prepare_for_sending_none(self, frames):
    pass

@mg.mutant_of("H2Connection._open_streams", "OPEN_STREAMS_NONE")
def _open_streams_none(self, remainder):
    pass

@mg.mutant_of("H2Connection._get_stream_by_id", "GET_STREAM_BY_ID_NO_CHECK")
def _get_stream_by_id_none(self, stream_id):
    return self.streams[stream_id]

@mg.mutant_of("H2Connection.get_next_available_stream_id", "GET_NEXT_AVAILABLE_STREAM_ID_NO_EXHAUSTION_CHECK")
def get_next_available_stream_id_no_exhaustion_check(self):
    # No streams have been opened yet, so return the lowest allowed stream
    # ID.
    if not self.highest_outbound_stream_id:
        next_stream_id = 1 if self.config.client_side else 2
    else:
        next_stream_id = self.highest_outbound_stream_id + 2
    self.config.logger.debug(
        "Next available stream ID %d", next_stream_id
    )

    return next_stream_id

@mg.mutant_of("H2Connection.end_stream", "END_STREAM_NONE")
def end_stream_none(self, stream_id):
    pass

@mg.mutant_of("H2Connection.update_settings", "UPDATE_SETTINGS_NONE")
def update_settings_none(self, new_settings):
    pass

@mg.mutant_of("H2Connection.data_to_send", "DATA_TO_SEND_NO_LIMIT")
def data_to_send_no_limit(self, amount=None):
    data = bytes(self._data_to_send)
    self._data_to_send = bytearray()
    return data

@mg.mutant_of("H2Connection.clear_outbound_data_buffer", "CLEAR_OUTBOUND_NOTHING")
def clear_outbound_data_buffer_nothing(self):
    pass

@mg.mutant_of("H2Connection._acknowledge_settings", "_ACKNOWLEDGE_SETTINGS_NOTHING")
def _acknowledge_settings_nothing(self):
    pass