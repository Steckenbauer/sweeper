# Backend Change Request

## User, system, or operational problem

Sweeper's login view needs a backend for password, passkey, and external identity-provider sign-in.

## Requested outcome

Build a FastAPI login service backed by PostgreSQL with password registration/login, browser WebAuthn passkeys, and OAuth/OIDC integrations for Google, Apple, Microsoft, GitHub, Facebook, and TARA.

## Known constraints

Use Python/FastAPI and PostgreSQL. Provider credentials and service URLs are deployment configuration. TARA uses standard OIDC discovery; its authentication context may be configured per deployment. Do not modify the existing in-progress frontend changes.

## References

The login component currently exposes password, passkey, Google, Facebook, and TARA methods. The requester confirmed the backend design and selected PostgreSQL.
