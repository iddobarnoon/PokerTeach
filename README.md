# PokerTeach - GTO Training App

A training-focused poker GTO application with gamification elements.

## Project Structure

```
PokerTeach/
├── backend/                    # Flask API backend
│   ├── app/
│   │   ├── models/            # Database models
│   │   ├── api/               # API endpoints
│   │   ├── services/          # Business logic
│   │   └── utils/             # Utility functions
│   ├── migrations/            # Database migrations
│   ├── tests/                 # Backend tests
│   ├── config.py              # Flask configuration
│   ├── requirements.txt       # Python dependencies
│   └── run.py                 # Application entry point
├── frontend/                  # React frontend
│   ├── src/
│   │   ├── components/        # React components
│   │   │   ├── training/      # Training components
│   │   │   ├── leaderboard/   # Leaderboard components
│   │   │   ├── play/          # Game components
│   │   │   └── common/        # Shared components
│   │   ├── pages/             # Page components
│   │   ├── services/          # API services
│   │   └── utils/             # Frontend utilities
│   ├── public/                # Static assets
│   └── package.json           # Node dependencies
├── src/                       # Original poker logic
│   ├── PokerPrimitives.py     # Poker primitives
│   └── PokerEngine.py         # Basic poker engine
└── docker-compose.yml         # Docker configuration
```

## Features

- **Training System**: Scenario-based GTO training with XP and leveling
- **Leaderboard**: Global rankings and achievements
- **Live Play**: Real-time poker simulation
- **Analytics**: Performance tracking and statistics

## Tech Stack

- **Backend**: Flask + SQLAlchemy + PostgreSQL + Redis
- **Frontend**: React + TypeScript + Material-UI
- **API Documentation**: Swagger/OpenAPI
- **Deployment**: Docker + Docker Compose