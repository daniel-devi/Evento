import { BrowserRouter, Routes, Route } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
// Importing the AuthenticationRequired component
import AuthenticationRequired from "./Hooks/AuthenticationRequired";
import AuthenticatedAlready from "./Hooks/AuthenticationAlready";
// PAGES
import HomePage from "./pages/HomePage";
import NotFoundPage from "./pages/NotFoundPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import Logout from "./pages/Logout";

function App() {
  return (
    <QueryClientProvider client={new QueryClient()}>
      {/* BrowserRouter component for handling routing */}
      <BrowserRouter>
        {/* Routes component to define application routes */}
        <Routes>
          {/* Route for the home page */}
          <Route path="/" element={<HomePage />} />

          {/** */}
          <Route
            path="login"
            element={<AuthenticatedAlready page={<LoginPage />} />}
          />

          <Route
            path="register"
            element={<AuthenticatedAlready page={<RegisterPage />} />}
          />

          <Route
            path="logout"
            element={<AuthenticationRequired page={() => <Logout />} />}
          />

          {/* Catch-all route for handling 404 Not Found pages */}
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  );
}
export default App;
