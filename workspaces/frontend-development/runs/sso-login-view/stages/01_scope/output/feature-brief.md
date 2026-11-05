# Feature Brief

## User and problem

Users of multiple SaaS applications need a consistent login interface that can present the sign-in methods enabled by each application.

## Desired outcome

Add a responsive, accessible, reusable login view in `frontend/catalog`. Host applications configure the app name and enabled methods, then handle password and provider sign-in callbacks themselves.

## In scope

- React + TypeScript + Vite frontend project.
- A reusable login view with email/password, passkey, common provider options (Google, Apple, Microsoft, GitHub, and Facebook), and Estonian TARA.
- Host-configurable methods, a typed password credential callback, loading and accessible error states.
- Keyboard-visible focus, semantic content, responsive layout.

## Out of scope

- Identity-provider SDKs, redirects, credential verification, session management, and backend integration.
- Claims of shared SSO/session behavior between SaaS applications; this is a UI component only.

## Acceptance criteria

- [x] A shared component renders app-specific copy and only the methods enabled by its host.
- [x] Email/password submits typed credentials to the host; other methods call the host with their method identifier.
- [x] Loading disables all sign-in actions and errors are announced accessibly.
- [x] Layout remains usable on narrow screens and the action is keyboard accessible with a visible focus indicator.
- [x] Frontend build and type-check pass.

## Assumptions and open questions

- The requester approved React + TypeScript + Vite.
- The requester clarified that this is a shared login UI, not an SSO-only view, and requested popular sign-in options plus Estonian TARA.
- Host applications own actual authentication and expose only their enabled methods.
- No existing frontend patterns or design system are present in the repository.

## Stage Check

pass — the requester clarified the reusable login UI outcome and requested method categories; authentication remains host-owned.
