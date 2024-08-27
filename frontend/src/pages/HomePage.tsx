import { ColorModeProvider } from "../Hooks/ColorModeProvider";
import Header from "../components/Header";
import Home from "../components/HomePage/Home";

function HomePage() {
  return (
    <ColorModeProvider>
    <Header />
    <div>HomePage</div>
    <Home/>
    </ColorModeProvider>
  )

}

export default HomePage;
