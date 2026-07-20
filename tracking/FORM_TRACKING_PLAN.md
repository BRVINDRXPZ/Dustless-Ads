# Form Tracking Plan

1. On first meaningful interaction emit `form_start` once per form session.
2. Emit `form_step_complete` only for defined groups, not each sensitive field.
3. Emit `form_error` with field category/error code—never entered value.
4. Emit `photo_upload` or `document_upload` only after production server acceptance; metadata is non-sensitive category/status.
5. Only the server-accepted, idempotent record emits the appropriate `*_submitted` event. Client validation success is not conversion.
6. Thank-you page emits `thank_you_view`, joined with server event ID; it is secondary and cannot substitute for submission.
7. Store consented click IDs/UTMs, landing path, minimized referrer, timestamps and consent version server-side. Derive device category without fingerprinting.
8. Test refresh, back, double-click, retries, multi-tab, disabled JS, invalid/oversized/spoofed files, blocked tags, denied consent and network failure.
