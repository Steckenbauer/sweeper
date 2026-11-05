import { useState } from "react";
import {
  LoginView,
  type LoginMethod,
} from "../components/LoginView/LoginView";

export default function App() {
  const [errorMessage, setErrorMessage] = useState<string>();

  return (
    <LoginView
      applicationName="Sweeper"
      methods={[
        "password",
        "passkey",
        "google",
        // "apple",
        // "microsoft",
        // "github",
        "facebook",
        "tara",
      ]}
      errorMessage={errorMessage}
      onSignIn={(method: LoginMethod) =>
        setErrorMessage(`${method} sign-in is not configured in this preview.`)
      }
    />
  );
}
