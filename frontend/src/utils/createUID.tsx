import { createdUID } from "./createdUID";

const generateUniqueId = () => {
    const length = 8;
    const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let id = '';

    // Generate a random string of specified length
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        id += characters[randomIndex];
    }
  
    // Check if the generated ID already exists, if so, recursively generate a new one
    if (createdUID.includes(id)) {
        return generateUniqueId();
    }

    // Add the new unique ID to the list of created IDs
    createdUID.push(id);
    return id;
};

export { generateUniqueId }