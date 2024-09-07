import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN } from "../components/Constants";
import { useState, useEffect, useCallback } from "react";

type AuthenticationRequiredProps = {
  page: () => React.ReactElement;
};

function AuthenticatedAlready({ page }: AuthenticationRequiredProps) {
  const [isAuthenticated, setIsAuthenticated] = useState(false); // State to track authorization status
  const navigate = useNavigate(); // Hook to navigate pages


  // Function to check the authentication status asynchronously
  const auth = useCallback(async () => {
    const token = localStorage.getItem(ACCESS_TOKEN); // Get the access token from local storage
    if (token) {
      setIsAuthenticated(true);
      return;
    }
  }, []);

  useEffect(() => {
    // Call the auth function when the component mounts
    auth().catch(() => setIsAuthenticated(false));
  }, [auth]); // Added auth as a dependency

  return isAuthenticated ? navigate("/") : page; // Render the page if not authorized, otherwise navigate to home
}

export default AuthenticatedAlready;
