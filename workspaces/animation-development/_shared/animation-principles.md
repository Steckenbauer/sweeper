# Animation Principles - shared quality constraints

Use these principles for both web/UI and standalone animation. Apply only those relevant to the requested deliverable.

## Intent and clarity

- Start from the intended message, action, or feeling; every motion should support it.
- Make timing, easing, staging, and visual hierarchy deliberate and consistent.
- Preserve legibility and the user's ability to understand or control the experience.
- Match rhythm, character, and visual style across related motion.

## Quality and delivery

- Define acceptance criteria before production, including the target platform and deliverable format when relevant.
- Review the motion in context and over its full duration, not only as a still or isolated frame.
- Check timing, transitions, clipping, visual artifacts, and continuity at the target playback conditions.
- Keep source and editable project files where the project expects them; do not treat a rendered preview as the only source of truth when editable sources are required.
- Report the exact tools, commands, playback conditions, and exports actually checked. Never claim an unrun check passed.

## Web and interactive motion

- Respect `prefers-reduced-motion`; provide a reduced or static alternative where motion could distract or cause discomfort.
- Preserve semantic content, keyboard operation, focus visibility, and readable contrast while elements move.
- Avoid unnecessary layout shifts and work that harms responsiveness or smooth playback. Prefer existing project conventions and dependencies.
- Check supported viewports and browsers from the project profile; do not invent support targets.

## Standalone 2D/3D motion

- Confirm frame rate, duration, dimensions/aspect ratio, color/background, alpha, audio, and export format as applicable before production.
- Check representative frames and the complete playback for continuity, composition, timing, and render defects.
- Confirm exported files open and play in the agreed target environment; preserve editable project/source assets when requested.
