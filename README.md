# Equipment Rental Platform

A full-stack monorepo for an equipment rental platform supporting both user-to-user and business-to-user listings.

## Project Structure

```
renting/
├── backend/                 # Django backend
│   ├── apps/               # Django applications
│   │   ├── users/         # User management
│   │   ├── equipment/     # Equipment listings
│   │   ├── rentals/       # Rental management
│   │   ├── payments/      # Payment processing
│   │   └── notifications/ # Notification system
│   ├── config/            # Django settings
│   └── requirements/      # Python dependencies
├── frontend/              # Next.js frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Next.js pages
│   │   ├── store/        # Redux store
│   │   └── utils/        # Utility functions
│   └── public/           # Static assets
├── shared/               # Shared types and utilities
└── .github/             # GitHub Actions workflows
```

## Tech Stack

### Backend
- Django & Django REST Framework
- PostgreSQL
- Celery with Redis
- OAuth2 Authentication
- 2FA Support
- Google Login Integration

### Frontend
- Next.js with SSR
- React (ES6+)
- Redux Toolkit
- Axios
- Form handling with React Hook Form
- File/Image uploads
- Admin panels for users and platform admin

## Setup Instructions

### Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements/dev.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env.local
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Development Workflow

1. Backend development:
   - Create new Django apps in `backend/apps/`
   - Follow Django best practices for models, views, and serializers
   - Use Celery for background tasks

2. Frontend development:
   - Create new components in `frontend/src/components/`
   - Add new pages in `frontend/src/pages/`
   - Manage state with Redux Toolkit
   - Use Axios for API calls

## Deployment

The project is configured for VPS deployment without Docker. See deployment documentation in each module's README for specific instructions.

## Future Considerations

- PWA support
- Android APK export via React Native
- Docker containerization
- Kubernetes orchestration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 