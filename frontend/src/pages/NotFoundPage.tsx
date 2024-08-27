import { ColorModeProvider } from "../Hooks/ColorModeProvider";
import NotFound from "../components/NotFound";

function NotFoundPage() {
  return (
    // Wrap the NotFound component with ColorModeProvider to ensure consistent theming
    <ColorModeProvider>
      <NotFound />
    </ColorModeProvider>
  );
}

export default NotFoundPage;
