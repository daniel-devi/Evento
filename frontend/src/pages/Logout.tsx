import { Navigate } from "react-router-dom";

// Logout component to handle user logout
function Logout() {
    // Clear all items from local storage
    localStorage.clear();

    // Redirect the user to the home page after logout
    return <Navigate to="/" />;
}

export default Logout;