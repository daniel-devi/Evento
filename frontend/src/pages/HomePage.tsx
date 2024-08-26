import { ColorModeProvider } from "../Hooks/ColorModeProvider";
import Header from "../components/Header";

function HomePage() {
  return (
    <ColorModeProvider>
    <Header />
    <div>HomePage</div>
    </ColorModeProvider>
  )

}

export default HomePage;
