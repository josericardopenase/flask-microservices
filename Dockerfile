# Use the official Nginx image as the base image
FROM nginx

# Copy your Nginx configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

