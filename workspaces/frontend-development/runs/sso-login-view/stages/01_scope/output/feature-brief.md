# Feature Brief

## User and problem

Users need a clear, trustworthy sign-in entry point that can be reused wherever Sweeper exposes access.

## Desired outcome

Add a responsive, accessible, provider-neutral SSO login view in `frontend/catalog` that host applications can configure with their app name and authentication callback.

## In scope

- React + TypeScript + Vite frontend project.
- A reusable SSO view with a single sign-in action, loading and error states.
- Keyboard-visible focus, semantic content, responsive layout.

## Out of scope

- Identity provider SDK, redirect URL, authentication/session management, backend integration.
- Username/password login or provider-specific branding.

## Acceptance criteria

- [x] A shared component renders app-specific sign-in copy without depending on an identity provider.
- [x] The primary action calls the host-provided callback; loading disables it and errors are announced accessibly.
- [x] Layout remains usable on narrow screens and the action is keyboard accessible with a visible focus indicator.
- [x] Frontend build and type-check pass.

## Assumptions and open questions

- The requester approved React + TypeScript + Vite.
- The requester approved a provider-neutral component with host-owned sign-in callback and states.
- No existing frontend patterns or design system are present in the repository.

## Stage Check

pass — outcome, scope, and acceptance criteria were confirmed with the requester.
