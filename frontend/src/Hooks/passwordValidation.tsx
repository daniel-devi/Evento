import React from "react";

type validatePasswordProps = {
  password: string;
  setErrorMessage: React.Dispatch<React.SetStateAction<string>>;
};

function validatePassword({
  password,
  setErrorMessage,
}: validatePasswordProps): boolean {
  // Default minimum and maximum password length
  const { minLength = 8, maxLength = 128 } = {};

  let isValid = true;

  if (password) {
    if (password.length < minLength) {
      setErrorMessage(
        `Password must be at least ${minLength} characters long.`
      );
      isValid = false;
    } else if (password.length > maxLength) {
      setErrorMessage(
        `Password cannot be longer than ${maxLength} characters.`
      );
      isValid = false;
    } else if (!/\d/.test(password)) {
      // Check if password contains at least one number
      setErrorMessage("Password must contain at least one number.");
      isValid = false;
    } else if (!/[A-Z]/.test(password)) {
      // Check if password contains at least one uppercase letter
      setErrorMessage("Password must contain at least one uppercase letter.");
      isValid = false;
    } else if (!/[a-z]/.test(password)) {
      // Check if password contains at least one lowercase letter
      setErrorMessage("Password must contain at least one lowercase letter.");
      isValid = false;
    } else if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
      // Check if password contains at least one special character
      setErrorMessage("Password must contain at least one special character.");
      isValid = false;
    }
  }

  return isValid;
}
export default validatePassword;
