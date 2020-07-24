import pytest_mutagen as mg
import h2
from h2.utilities import _secure_headers, extract_method_header, is_informational_response, guard_increment_window, authority_from_headers, validate_headers, _reject_uppercase_header_fields, _reject_surrounding_whitespace, _reject_te, _reject_connection_header, _custom_startswith, _assert_header_in_set, _reject_pseudo_header_fields, _check_pseudo_header_field_acceptability, _validate_host_authority_header, _check_host_authority_header, _check_path_header, _lowercase_header_names, _strip_surrounding_whitespace, _strip_connection_headers, _check_sent_host_authority_header, _combine_cookie_fields, normalize_outbound_headers, normalize_inbound_headers, validate_outbound_headers, SizeLimitDict

mg.link_to_file(mg.APPLY_TO_ALL)


#hash=41c1ed98d24f208c
@mg.mutant_of("is_informational_response", "IS_INFORMATIONAL_RESPONSE_8")
def is_informational_response_8(headers):
    """
    Searches a header block for a :status header to confirm that a given
    collection of headers are an informational response. Assumes the header
    block is well formed: that is, that the HTTP/2 special headers are first
    in the block, and so that it can stop looking when it finds the first
    header field whose name does not begin with a colon.

    :param headers: The HTTP/2 header block.
    :returns: A boolean indicating if this is an informational response.
    """
    for n, v in headers:
        if isinstance(n, bytes):
            sigil = b':'
            status = b':status'
            informational_start = b'1'
        else:
            sigil = u':'
            status = u':status'
            informational_start = u'1'

        # If we find a non-special header, we're done here: stop looping.
        if not n.startswith(sigil):
            pass

        # This isn't the status header, bail.
        if n != status:
            continue

        # If the first digit is a 1, we've got informational headers.
        return v.startswith(informational_start)
