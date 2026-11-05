# Interface Plan

## Screens and entry points

One reusable `LoginView` in `frontend/catalog/src/components/LoginView/`; the host provides `applicationName`, the enabled `methods`, a typed `onSignIn` callback, and optional loading/error state.

## Acceptance-criteria mapping

| Criterion | UI location/state | User interaction | Verification |
|---|---|---|---|
| Reusable app copy and configurable options | Login card, password form, provider buttons | Host configures app name and enabled methods | Build/type-check; inspect component contract |
| Password and provider callbacks | Native form and provider buttons | Submit validated email/password or choose a provider | Build/type-check; inspect callback data |
| Loading and accessible errors | Disabled controls, busy state, role=alert | Host controls pending/error state | Build/type-check; inspect semantic attributes |
| Responsive and keyboard accessible | Card, form, provider grid, visible focus | Tab and activate controls at narrow/desktop widths | Review CSS and browser viewport behavior |
| Build and type-check pass | Frontend project | Run npm scripts | Record exact command results |

## Relevant states

- Loading: sign-in button text changes to “Signing in…”, all login methods and fields are disabled.
- Empty methods: host passes an empty list; render no sign-in controls and leave an explicit configuration limitation to the host.
- Error: Optional host-provided message in an alert region.
- Success: host callback owns authentication and navigation.
- Validation: native required email/password controls validate the password form; provider choices do not require local credentials.

## Responsive behavior

Centered card with constrained width, mobile padding adjustments, and no fixed horizontal dimensions below viewport width.

## Keyboard and accessibility

Use main/section landmarks, a labelled heading, a native button, visible focus, `aria-busy`, `role=alert`. Respect reduced-motion preference.

## Existing patterns/components to reuse

None; the repository has no existing application source or UI system.

## Decisions and open questions

The host selects enabled methods and owns authentication. The preview displays common methods and reports that the selected method is not configured rather than simulating authentication.

## Stage Check

pass — plan reflects the clarified shared login view and host-owned authentication boundary.
