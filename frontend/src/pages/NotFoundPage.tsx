import { ColorModeProvider } from "../Hooks/ColorModeProvider";
import NotFound from "../components/NotFound";

function NotFoundPage() {
  return (
   <ColorModeProvider>
   <NotFound />
   </ColorModeProvider>
  );
}

export default NotFoundPage;
