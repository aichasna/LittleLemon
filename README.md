# LittleLemon
This project is a Django-based REST API for managing menu items and table bookings at Little Lemon restaurant.

## API Endpoints: 

- **Menu API:**  
  GET, POST - `/restaurant/menu/`  
  GET, PUT, DELETE - `/restaurant/menu/<id>/`  

- **Authentication (Djoser):**  
  Register: `POST /auth/users/`  
  Login: `POST /auth/token/login/`  
  Logout: `POST /auth/token/logout/`  

## Testing with Insomnia/Postman:
1. Obtain a token using:  
   `POST /auth/token/login/`  
   Body:  
   ```json
   {
     "username": "testuser",
     "password": "password123"
   }
