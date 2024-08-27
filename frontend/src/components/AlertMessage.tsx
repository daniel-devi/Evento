import Alert from "@mui/material/Alert";
import IconButton from "@mui/material/IconButton";
import Collapse from "@mui/material/Collapse";
import CloseIcon from "@mui/icons-material/Close";

// Component for displaying an alert message with a close button
type AlertMessageProps = {
    open: boolean;
    setOpen: React.Dispatch<React.SetStateAction<boolean>>;
    message: string;
}
const AlertMessage = ({ open, setOpen, message }: AlertMessageProps) => {
  return (
    <Collapse in={open}>
      <Alert
        action={
          <IconButton
            aria-label="close"
            color="inherit"
            size="small"
            onClick={() => setOpen(false)} // Close the alert when button is clicked
          >
            <CloseIcon fontSize="inherit" />
          </IconButton>
        }
        sx={{ mb: 2 }}
      >
        {message} {/* Display the message passed as a prop */}
      </Alert>
    </Collapse>
  );
};

export default AlertMessage;