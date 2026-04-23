# Use official lightweight Apache image
FROM httpd:alpine

# Remove default files (optional)
RUN rm -rf /usr/local/apache2/htdocs/*

# Copy your website files into Apache's default directory
COPY . /usr/local/apache2/htdocs/

# Expose Apache port
EXPOSE 80

# Start Apache in the foreground (already default in httpd image)
CMD ["httpd-foreground"]