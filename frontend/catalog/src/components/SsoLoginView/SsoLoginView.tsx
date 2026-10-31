import { useId } from "react";
import styles from "./SsoLoginView.module.css";

export interface SsoLoginViewProps {
  applicationName: string;
  onSignIn: () => void;
  isLoading?: boolean;
  errorMessage?: string;
}

export function SsoLoginView({
  applicationName,
  onSignIn,
  isLoading = false,
  errorMessage,
}: SsoLoginViewProps) {
  const titleId = useId();

  return (
    <main className={styles.loginPage}>
      <section className={styles.loginCard} aria-labelledby={titleId}>
        <div className={styles.brandMark} aria-hidden="true">
          <span />
          <span />
          <span />
          <span />
        </div>

        <p className={styles.eyebrow}>SECURE ACCESS</p>
        <h1 id={titleId}>Welcome to {applicationName}</h1>
        <p className={styles.loginDescription}>
          Sign in with your organization account to continue.
        </p>

        {errorMessage && (
          <p className={styles.loginError} role="alert">
            {errorMessage}
          </p>
        )}

        <button
          className={styles.ssoButton}
          type="button"
          onClick={onSignIn}
          disabled={isLoading}
          aria-busy={isLoading}
        >
          <span>{isLoading ? "Connecting…" : "Continue with SSO"}</span>
          {!isLoading && (
            <svg
              aria-hidden="true"
              viewBox="0 0 20 20"
              className={styles.buttonArrow}
            >
              <path d="M4.25 10h11.5m-4.75-4.75L15.75 10 11 14.75" />
            </svg>
          )}
        </button>

        <p className={styles.loginFootnote}>
          Your organization manages sign-in and account security.
        </p>
      </section>
      <p className={styles.pageFooter}>Single sign-on · Secure by design</p>
    </main>
  );
}
