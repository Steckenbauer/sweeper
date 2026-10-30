# Frontend Quality Principles - reusable constraints

Apply these principles to every feature. Follow the repository's existing patterns and the project-specific settings in [`project-profile.md`](project-profile.md); this file does not prescribe a framework or component architecture.

## Interface and behavior

- Tie each UI change to the feature brief's user outcome and acceptance criteria.
- Consider relevant loading, empty, error, success, and disabled states; do not add irrelevant states just to fill a checklist.
- Preserve existing navigation, data, and interaction behavior unless the brief explicitly changes it.
- Make layouts usable at the project's supported viewport sizes and avoid introducing horizontal overflow.

## Accessibility

- Prefer semantic HTML and native controls; provide accessible names and meaningful heading order.
- Ensure keyboard operation and visible focus for interactive controls.
- Communicate validation errors and state changes in a way assistive technology can perceive.
- Do not use color as the only way to convey meaning.

## Implementation and verification

- Make the smallest coherent change and reuse established project components and tokens.
- Keep behavior, visual states, and accessibility requirements traceable to acceptance criteria.
- Run the checks configured in the project profile that apply to the change; record exact commands and outcomes.
- Do not report unrun checks as passing. Record unavailable checks and unresolved risks in the handoff.
