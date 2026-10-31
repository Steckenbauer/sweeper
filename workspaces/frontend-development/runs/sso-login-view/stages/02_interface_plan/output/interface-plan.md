# Interface Plan

## Screens and entry points

One reusable `SsoLoginView` in `frontend/catalog/src/components/SsoLoginView.tsx`; the host provides `applicationName`, `onSignIn`, and optional loading/error state.

## Acceptance-criteria mapping

| Criterion | UI location/state | User interaction | Verification |
|---|---|---|---|
| Reusable, provider-neutral app copy | Login card and component props | Host configures app name and callback | Build/type-check; inspect component contract |
| Callback, loading, accessible error | SSO button, busy state, role=alert | Activate button; host controls pending/error | Build/type-check; inspect semantic attributes |
| Responsive and keyboard accessible | Card layout and button focus state | Tab and activate button at narrow/desktop widths | Review CSS and browser viewport behavior |
| Build and type-check pass | Frontend project | Run npm scripts | Record exact command results |

## Relevant states

- Loading: button text changes to “Connecting…”, disabled and `aria-busy`.
- Empty: Not applicable; no list or data-dependent content.
- Error: Optional host-provided message in an alert region.
- Success: Not applicable; host SSO redirect owns success handling.
- Disabled/validation: Button disabled during host-provided loading; no user input to validate.

## Responsive behavior

Centered card with constrained width, mobile padding adjustments, and no fixed horizontal dimensions below viewport width.

## Keyboard and accessibility

Use main/section landmarks, a labelled heading, a native button, visible focus, `aria-busy`, `role=alert`. Respect reduced-motion preference.

## Existing patterns/components to reuse

None; the repository has no existing application source or UI system.

## Decisions and open questions

Provider-neutral appearance and callback boundary approved by requester. The preview callback will report that no provider is configured rather than simulate authentication.

## Stage Check

pass — plan matches the requester-approved view-only scope.
