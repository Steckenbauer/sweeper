# Feature Request

## User or problem

Users need one reusable login interface that can present the sign-in methods enabled by different SaaS applications.

## Requested outcome

Create a polished, responsive login view in the project-root frontend catalog. It should support email/password, passkeys, common identity providers, and Estonian TARA, with each host application choosing which methods to show and handling authentication through callbacks.

## Known constraints

Use React, TypeScript, and Vite. This change provides a reusable frontend view only; identity-provider redirects, credential verification, and session management remain in each host application.

## References

None
