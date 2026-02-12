# 🔐 Biometric Face Security System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![Face Recognition](https://img.shields.io/badge/AI-Face%20Recognition-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

A **Real-Time Face Recognition & Access Control System** built with Python. This project simulates a corporate security environment where users are identified via webcam, and their entry is logged automatically.

> **🚀 Demo Ready:** The repository includes pre-trained face embeddings for **Cristiano Ronaldo** and **Jon Snow** for immediate testing!

---

## 🌟 Key Features

### 1. 👥 Multi-User Support
- Unlimited user registration.
- Dynamic database system using the `users/` directory.
- No retraining required when adding new users.

### 2. 📝 Automated Access Logging
- Automatically records entry events to a CSV file (`access_logs.csv`).
- Logs include **Name**, **Timestamp**, and **Access Status**.
- Features a "Cooldown Timer" to prevent spamming logs for the same person.

### 3. 🔒 Privacy-First Architecture (GDPR Friendly)
- **No Raw Images:** The system does **not** save user photos.
- **Vector Storage:** Faces are converted into **128-dimensional mathematical embeddings** and stored as `.npy` (NumPy) binary files.
- This ensures high security and fast processing.

### 4. ⚡ High Performance
- Optimized frame resizing (1/4 scale) for low-latency real-time processing.
- Uses **HOG (Histogram of Oriented Gradients)** and **Deep Learning** for state-of-the-art accuracy.

---

## 📂 Project Structure

```text
Face-Security-System/
├── main.py              # The core application script
├── users/               # Database containing .npy face signatures
│   ├── cristiano ronaldo.npy  # Demo user
│   └── jon snow.npy           # Demo user
├── access_logs.csv      # Log file (Auto-generated on first run)
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
