# Use Node.js as the base image
FROM node:18

# Install Firebase CLI globally
RUN npm install -g firebase-tools

# Set the working directory in the container
WORKDIR /app

# Copy local files to the container
COPY . /app

# Expose the port used by the Firebase Authentication Emulator
#EXPOSE 4000

# Default command to start the Firebase Emulator
CMD ["firebase", "emulators:start", "--only", "auth"]
