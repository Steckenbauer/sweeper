# Implementation Record

## Changed files

- `frontend/catalog/src/components/LoginView/`: reusable login view and isolated CSS module.
- `frontend/catalog/src/app/App.tsx`: preview host configures the available methods and displays a host-owned not-configured message.
- `frontend/catalog/src/main.tsx`: imports the app shell from its folder after the component reorganization.
- `workspaces/frontend-development/runs/sso-login-view/`: updated scope, interface plan, and verification evidence.

## Implementation decisions

- `LoginView` accepts the app name, enabled methods, loading/error state, and a typed callback. Password sign-in calls the host with email/password; each provider/passkey/TARA button passes its method identifier.
- The view supports password, passkey, Google, Apple, Microsoft, GitHub, Facebook, and Estonian TARA. Hosts choose which methods to expose.
- Authentication, provider SDKs, redirects, credential verification, and sessions remain host-owned. No external dependencies were added.
- Empty methods produce a clear status message; input values are local to the view and are not persisted.

## Checks run

| Check | Exact command or method | Result |
|---|---|---|
| Production build | `Push-Location frontend\catalog; npm.cmd run build` | Pass |
| Type-check | `Push-Location frontend\catalog; npm.cmd run typecheck` | Pass |
| Rendered UI | Inline Node ESM using Vite `ssrLoadModule` and React `renderToStaticMarkup`; assertions for all configured methods, email/password fields, error alert, and empty-method notice | Pass |

## Checks not run and why

Browser viewport, keyboard, and screen-reader testing were not run for this revision; no browser test suite or assistive-technology workflow is configured.

## Remaining risks or follow-up

The preview host deliberately does not authenticate. Each SaaS host must configure only methods it supports and securely implement the callback, credential handling, provider integration, and session behavior.

## Stage Check

pass — build, type-check, and rendered-markup assertions passed; host-owned authentication limitations are documented.
