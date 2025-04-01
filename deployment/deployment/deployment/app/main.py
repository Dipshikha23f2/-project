from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import Optional
import pandas as pd
import numpy as np
import os
import joblib
from pydantic import BaseModel

# Define data models
class StudentData(BaseModel):
    maths: float
    physics: float
    english: float
    economics: float
    biology: float

# Initialize FastAPI app
app = FastAPI(title="Student Clustering API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Student Clustering API is running", "status": "active"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
