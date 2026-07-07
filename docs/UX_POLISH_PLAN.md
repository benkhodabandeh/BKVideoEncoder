# UX Polish Plan

## Visual design

- Use a consistent cinema-grade dark surface: `#0E1117`, `#151A22`, `#202837`.
- Use gold `#DAB45B` only for primary actions and selected states.
- Use muted slate `#3E5268` for secondary structure.
- Keep all destructive/cancel actions visually separate.

## Interaction design

- Do not block the main workflow with success popups.
- Use toast notifications for added-to-queue and completed actions.
- Use modal dialogs only for destructive choices and invalid states.
- Debounce previews and estimates while the user types.
- Keep progress information stable and readable rather than updating every raw FFmpeg event.

## Future premium features

- Queue drag/drop reorder.
- Per-job encode speed and ETA trend.
- Side-by-side before/after frame comparison.
- Preset favorite pins.
- Exportable encode report with command, source info, and VMAF score.
- First-run setup wizard for FFmpeg and output folders.
