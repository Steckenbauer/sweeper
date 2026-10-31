import { useState } from "react";
import { SsoLoginView } from "../components/SsoLoginView/SsoLoginView";

export default function App() {
  const [errorMessage, setErrorMessage] = useState<string>();

  return (
    <SsoLoginView
      applicationName="Sweeper"
      errorMessage={errorMessage}
      onSignIn={() =>
        setErrorMessage("Single sign-on is not configured in this preview.")
      }
    />
  );
}
