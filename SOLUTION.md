# Solution Steps

1. Define an enum class OrderStatusEnum (using str and Enum) in both the models and schemas to centrally list allowed statuses: 'pending', 'shipped', 'delivered', 'cancelled'.

2. In models.py, define the Order database model, where the status column is an SQLAlchemy Enum using the OrderStatusEnum, and set default to 'pending'.

3. In schemas.py, define OrderUpdate (for request body) and OrderResponse (for output) Pydantic models, using the same OrderStatusEnum for validation and documentation.

4. In crud.py, implement update_order_status to find the order, validate existence, update its status, commit, and return the instance. If the order is not found, raise HTTP 404.

5. In main.py, define the FastAPI application, ensure database sessions are correctly handled, and create a PUT endpoint '/orders/{order_id}/status' that accepts only valid statuses as per the enum (validated by Pydantic), updates the order, and returns the updated order with the correct status.

6. Ensure all necessary files are included for Docker Compose: Dockerfile, requirements.txt, docker-compose.yml, and the app package structure. Set the environment variable DATABASE_URL to connect to the Postgres service.

7. Confirm that upon startup, tables are created if not existing (via Base.metadata.create_all).

8. With this structure, only valid statuses are accepted via API; invalid ones get clear 422 validation errors. The API docs list allowed statuses, and changes are persisted in the Postgres database.

