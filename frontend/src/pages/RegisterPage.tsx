import { ColorModeProvider } from "../Hooks/ColorModeProvider";
import RegisterForm from "../components/RegisterPage/RegisterForm";

function RegisterPage() {
  return (
    // Wrap the login components with ColorModeProvider for theme consistency
    <ColorModeProvider>
      <RegisterForm />
    </ColorModeProvider>
  );
}

export default RegisterPage;
