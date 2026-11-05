import { useId, useState, type FormEvent } from "react";
import styles from "./LoginView.module.css";

export type LoginMethod =
  | "password"
  | "passkey"
  | "google"
  // | "apple"
  // | "microsoft"
  // | "github"
  | "facebook"
  | "tara";

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface LoginViewProps {
  applicationName: string;
  methods: LoginMethod[];
  onSignIn: (method: LoginMethod, credentials?: LoginCredentials) => void;
  isLoading?: boolean;
  errorMessage?: string;
}

const providerMethods: { id: LoginMethod; label: string }[] = [
  { id: "passkey", label: "Passkey" },
  { id: "google", label: "Google" },
  // { id: "apple", label: "Apple" },
  // { id: "microsoft", label: "Microsoft" },
  // { id: "github", label: "GitHub" },
  { id: "facebook", label: "Facebook" },
  { id: "tara", label: "Estonian TARA" },
];

export function LoginView({
  applicationName,
  methods,
  onSignIn,
  isLoading = false,
  errorMessage,
}: LoginViewProps) {
  const titleId = useId();
  const emailId = useId();
  const passwordId = useId();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const enabledProviderMethods = providerMethods.filter(({ id }) =>
    methods.includes(id),
  );
  const hasPasswordLogin = methods.includes("password");

  function handlePasswordSignIn(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    onSignIn("password", { email, password });
  }

  return (
    <main className={styles.loginPage}>
      <section className={styles.loginCard} aria-labelledby={titleId}>
        <div className={styles.brandMark} aria-hidden="true">
          <span />
          <span />
          <span />
          <span />
        </div>

        <p className={styles.eyebrow}>WELCOME BACK</p>
        <h1 id={titleId}>Welcome to {applicationName}</h1>
        <p className={styles.loginDescription}>
          Sign in to continue to your account.
        </p>

        {errorMessage && (
          <p className={styles.loginError} role="alert">
            {errorMessage}
          </p>
        )}

        {hasPasswordLogin && (
          <form className={styles.passwordForm} onSubmit={handlePasswordSignIn}>
            <label className={styles.fieldLabel} htmlFor={emailId}>
              Email
            </label>
            <input
              className={styles.input}
              id={emailId}
              type="email"
              name="email"
              autoComplete="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
              disabled={isLoading}
            />
            <label className={styles.fieldLabel} htmlFor={passwordId}>
              Password
            </label>
            <input
              className={styles.input}
              id={passwordId}
              type="password"
              name="password"
              autoComplete="current-password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              required
              disabled={isLoading}
            />
            <button
              className={styles.primaryButton}
              type="submit"
              disabled={isLoading}
              aria-busy={isLoading}
            >
              {isLoading ? "Signing in…" : "Sign in"}
            </button>
          </form>
        )}

        {hasPasswordLogin && enabledProviderMethods.length > 0 && (
          <div className={styles.divider} aria-hidden="true">
            <span>or continue with</span>
          </div>
        )}

        {enabledProviderMethods.length > 0 && (
          <div className={styles.providerList}>
            {enabledProviderMethods.map(({ id, label }) => (
              <button
                className={styles.providerButton}
                data-method={id}
                key={id}
                type="button"
                onClick={() => onSignIn(id)}
                disabled={isLoading}
                aria-busy={isLoading}
              >
                {label}
              </button>
            ))}
          </div>
        )}

        {methods.length === 0 ? (
          <p className={styles.loginNotice} role="status">
            No sign-in methods are available. Contact your administrator.
          </p>
        ) : (
          <p className={styles.loginFootnote}>
            Your sign-in options are managed by {applicationName}.
          </p>
        )}
      </section>
      <p className={styles.pageFooter}>One secure place to sign in</p>
    </main>
  );
}
