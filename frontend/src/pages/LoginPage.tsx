import { ColorModeProvider } from "../Hooks/ColorModeProvider";
import LoginForm from "../components/LoginPage/LoginForm";

function LoginPage() {
  return (
    // Wrap the login components with ColorModeProvider for theme consistency
    <ColorModeProvider>
      <LoginForm />
    </ColorModeProvider>
  );
}

export default LoginPage;
