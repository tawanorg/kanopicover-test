# Build Stage
FROM node:20 AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json for dependency installation
COPY package*.json ./

# Install all dependencies (including dev dependencies for building)
RUN npm install

# Copy the entire application code
COPY . .

# Build the application
RUN npm run build

# Production Stage
FROM node:20

# Install `serve` globally to serve the static files
RUN npm install -g serve

# Copy the build folder from the builder stage
COPY --from=builder /app/build /app/build

# Expose the app's running port
EXPOSE 3000

# Serve the built application on port 3000
CMD ["serve", "-s", "/app/build", "-l", "3000"]