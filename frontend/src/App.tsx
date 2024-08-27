import { BrowserRouter, Routes, Route } from "react-router-dom";
// PAGES
import HomePage from "./pages/HomePage";
import NotFoundPage from "./pages/NotFoundPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";

function App() {
  return (
    <>
      {/* BrowserRouter component for handling routing */}
      <BrowserRouter>
        {/* Routes component to define application routes */}
        <Routes>
          {/* Route for the home page */}
          <Route path="/" element={<HomePage />} />

          {/** */}
          <Route path="login" element={<LoginPage/>} />

          <Route path="register" element={<RegisterPage/>} />

          {/* Catch-all route for handling 404 Not Found pages */}
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
