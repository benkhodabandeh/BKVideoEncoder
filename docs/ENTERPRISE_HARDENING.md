# Enterprise Hardening Roadmap

BK Video Encoder is feature-rich but should be hardened before being called enterprise-grade.

## Immediate reliability work

- Bounded UI queue processing.
- Debounced estimate and preview refreshes.
- Limited still-extraction worker count.
- `-nostdin` for FFmpeg process calls.
- Windows-aware process cancellation.
- Non-blocking routine success notifications.

## Build/release work

- Pin runtime dependencies.
- Verify FFmpeg archives by SHA256 before extraction.
- Publish release checksums.
- Sign Windows binaries.
- Generate SBOM and third-party notices.
- Add CI gates for compile, lint, tests, and dependency audit.

## Architecture work

- Split GUI, controller, encoding service, and process runner.
- Add typed job models.
- Make FFmpeg command generation pure and testable.
- Add tiny sample-media integration tests.
- Add structured job result reports.

## UX polish work

- Replace routine modal popups with toasts/status cards.
- Add queue drag/drop and per-job status chips.
- Add exportable diagnostic bundle.
- Add in-app onboarding for first run.
- Add accessible keyboard navigation.
