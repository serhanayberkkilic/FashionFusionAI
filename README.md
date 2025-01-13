# Fast Fashion AI Project

## Overview
The Fast Fashion AI Project is a full-stack application that leverages machine learning and computer vision to assist users in finding fashion items, creating outfit combinations, and recommending styles based on user-uploaded images. The application includes both a backend API built with FastAPI and a frontend built with modern web technologies.

## Features
- **Image Search**: Find the most similar fashion items from a database based on uploaded images.
- **Segmentation**: Analyze outfit images to identify and classify individual clothing items.
- **Outfit Recommendations**: Suggest outfits based on user preferences or existing wardrobe items.
- **Trend and Seasonal Advice**: Provide style suggestions based on current fashion trends and weather conditions.

## Project Structure
```
fast-fashion-ai/
│
├── backend/                   # Backend application (FastAPI)
│   ├── app/                   # API, models, services, and config
│   ├── tests/                 # Unit and integration tests
│   ├── requirements.txt       # Python dependencies
│   └── Dockerfile             # Backend Dockerfile
│
├── frontend/                  # Frontend application (React, Vue, etc.)
│   ├── src/                   # Frontend source code
│   ├── public/                # Static assets
│   ├── package.json           # Frontend dependencies
│   └── Dockerfile             # Frontend Dockerfile
│
├── data/                      # Data directory
│   ├── images/                # Training and test images
│   ├── models/                # Pre-trained AI models
│   └── datasets/              # Dataset files (e.g., CSV, JSON)
│
├── scripts/                   # Utility scripts
│   └── init_db.py             # Database initialization script
│
├── docs/                      # Project documentation
│   └── README.md              # Documentation files
│
├── docker-compose.yml         # Docker Compose configuration
├── .env                       # Environment variables
└── README.md                  # Main project README
```

## Prerequisites
- Python 3.9+
- Node.js 16+
- Docker & Docker Compose

## Installation

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

### Docker Setup
1. Build and run the containers:
   ```bash
   docker-compose up --build
   ```
2. Access the frontend at `http://localhost:3000` and the backend API at `http://localhost:8000`.

## Usage
1. Upload an image of a fashion item.
2. View similar items, segmentation results, or outfit recommendations.
3. Explore seasonal and trending fashion suggestions.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please contact serhan ayberk kilic.

## Acknowledgements
Special thanks to Edanur, my lovely wife, for her unwavering support throughout this project.