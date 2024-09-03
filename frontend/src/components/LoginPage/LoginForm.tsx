import { useState } from "react";
import { AxiosResponse } from "axios";
import { useQuery } from "@tanstack/react-query";
import { Box, TextField } from "@mui/material";
import api from "../../utils/Api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../Constants";
import getObjectValues from "../../utils/GetObjectValue";
import AlertMessage from "../AlertMessage";
import Copyright from "../Copyright";

function LoginForm() {
  const [userList, setUserList] = useState([]);
  const [open, setOpen] = useState(false);
  const [error, setError] = useState(false);
  const [usernameErrorMessage, setUsernameErrorMessage] = useState("");
  const [passwordErrorMessage, setPasswordErrorMessage] = useState("");
  const [userUsername, setUserUsername] = useState("");
  let userID: number;



  // Fetch the list of usernames when the component mounts
  const fetchUsernames = async () => {
    const response = await api.get("Accounts-Api/get-usernames");
    // Set the user list state with the fetched data
    const newUserList = getObjectValues(response.data);
    setUserList(newUserList);
    if (newUserList.length === 0) {
      usernameApiCall.refetch(); 
    }
  };

  // Use react-query to manage the API call for usernames
  const usernameApiCall = useQuery({ queryKey: ['usernames'], queryFn: fetchUsernames });

  // Function to find a username by email
  const findUsername = async (theEmail: string) => {
    try {
      const res = await api.get(
        `Accounts-Api/get-user-through-email/${theEmail}`
      );
      setUserUsername(res.data[0].username);
      userID = res.data[0].id;
    } catch (error) {
      console.error("Error finding username:", error);
    }
  };

  // Handle form submission for login
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const email = data.get("email") as string;
    await findUsername(email);
    try {
      const res: AxiosResponse = await api.post("api/token/", {
        username: userUsername,
        password: data.get("password"),
      });
      if (res.status === 200) {
        // If login is successful, store tokens and user info
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        localStorage.setItem("UserID", userID.toString());
        setError(false);
        setPasswordErrorMessage("");
        setUsernameErrorMessage("");
        setOpen(true);
        // Redirect to home page after a short delay
        setTimeout(() => {
          window.location.href = "http://localhost:5173/";
        }, 3500);
      }
    } catch (error: any) {
      // Handle different error scenarios
      if (error.response?.status === 400) {
        setError(true);
        const foundUser: boolean = Boolean(
          userList.find((username) => username === userUsername)
        );
        setUsernameErrorMessage(foundUser ? "" : "User Not Found");
        setPasswordErrorMessage("Password Incorrect");
      }
      if (error.response?.status === 401) {
        setError(true);
        setUsernameErrorMessage("");
        setPasswordErrorMessage("Password Incorrect");
      }
    }
  };

  return (
    <Box
      className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"
      sx={{
        bgcolor: "background.default",
        color: "text.primary",
        height: "100vh",
      }}
    >
      <AlertMessage open={open} setOpen={setOpen} message="Login Successful" />
      <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
        Sign in to your account
      </h2>
      <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label
              htmlFor="email"
              className="block text-sm font-medium leading-6 text-gray-900"
            >
              Email address
            </label>
            <div className="mt-2">
              <TextField
                id="email"
                name="email"
                type="email"
                required
                autoComplete="email"
                error={error}
                helperText={usernameErrorMessage}
                autoFocus
                placeholder="someone@example.com"
                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between">
              <label
                htmlFor="password"
                className="block text-sm font-medium leading-6 text-gray-900"
              >
                Password
              </label>
              <div className="text-sm">
                <a
                  href="#"
                  className="font-semibold text-indigo-600 hover:text-indigo-500"
                >
                  Forgot password?
                </a>
              </div>
            </div>
            <div className="mt-2">
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                error={error}
                helperText={passwordErrorMessage}
                className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >
              Sign in
            </button>
          </div>
        </form>

        <p className="mt-10 text-center text-sm text-gray-500">
          Not a member?{" "}
          <a
            href="/register"
            className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
          >
            SignUp, Today
          </a>
        </p>
      </div>
      <Copyright />
    </Box>
  );
}

export default LoginForm;
