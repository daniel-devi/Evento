import axios, { InternalAxiosRequestConfig, AxiosResponse } from "axios";
// Constants for localStorage keys
const ACCESS_TOKEN = "accessToken";

// Gets the authentication token from localStorage
const authToken = localStorage.getItem(ACCESS_TOKEN);

// Create an Axios Api instance with the base URL from environment variables
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000, // Set a timeout of 10 seconds
  headers: {
    "Content-Type": "application/json", // Default content type
    Accept: "application/json", // Expected response format
  },
});

// Add a request interceptor to attach the Authorization header
api.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // Ensure the token is added to the headers if it exists
    if (authToken) {
      config.headers.set("Authorization", `Bearer ${authToken}`);
    }
    return config;
  },
  (error: Promise<never>) => {
    // Handle the error before passing it on
    return Promise.reject(error);
  }
);

// Add a response interceptor to handle errors globally
api.interceptors.response.use(
  (response: AxiosResponse) => {
    // Handle the response
    return response;
  },
  (error: { response?: unknown; request?: unknown; message?: string }) => {
    // Handle errors globally
    if (error.response) {
      // Server responded with a status other than 200 range
      console.error("Error response:", error.response);
    } else if (error.request) {
      // No response was received
      console.error("Error request:", error.request);
    } else {
      // Other errors
      console.error("Error message:", error.message);
    }
    return Promise.reject(error);
  }
);

export default api;
