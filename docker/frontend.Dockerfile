# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY /app-front/package*.json .

# Install app dependencies
RUN npm install

# Copy the current directory contents into the container at /app
COPY ./app-front .

# Build the React app
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Run the app when the container launches
CMD ["npm", "start"]
