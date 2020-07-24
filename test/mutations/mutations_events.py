import pytest_mutagen as mg
import h2
from h2.events import RequestReceived, ResponseReceived, TrailersReceived, InformationalResponseReceived, DataReceived, WindowUpdated, RemoteSettingsChanged, PingReceived, PingAcknowledged, StreamEnded, StreamReset, PushedStreamReceived, SettingsAcknowledged, PriorityUpdated, ConnectionTerminated, AlternativeServiceAvailable, UnknownFrameReceived, _bytes_representation

mg.link_to_file(mg.APPLY_TO_ALL)

#hash=8fad55ef41298a38
@mg.mutant_of("InformationalResponseReceived.__init__", "INFORMATIONALRESPONSERECEIVED.__INIT___0")
def __init__(self):
    #: The Stream ID for the stream this informational response was made
    #: on.
    self.stream_id = None

    #: The headers for this informational response.
    self.headers = None

    #: If this response also had associated priority information, the
    #: associated :class:`PriorityUpdated <h2.events.PriorityUpdated>`
    #: event will be available here.
    #:
    #: .. versionadded:: 2.4.0
    self.priority_updated = None
